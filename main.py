# ip_checker.py
# A simple FastAPI-based IP checker for geolocation and proxy/VPN status

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI(title="Agenics IP Checker API")

IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")  # optional, if using ipinfo.io

@app.get("/check")
async def check_ip(request: Request):
    client_ip = request.client.host
    return await get_ip_data(client_ip)

@app.get("/check/{ip}")
async def check_ip_explicit(ip: str):
    return await get_ip_data(ip)

async def get_ip_data(ip: str):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        headers = {"Authorization": f"Bearer {IPINFO_TOKEN}"} if IPINFO_TOKEN else {}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return JSONResponse(status_code=502, content={"error": "Failed to fetch IP info"})

        data = response.json()
        return {
            "ip": ip,
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "org": data.get("org"),
            "hostname": data.get("hostname"),
            "location": data.get("loc"),
            "is_proxy_or_vpn": any(x in str(data.get("org", "")).lower() for x in ["vpn", "proxy", "hosting", "cloud"])
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
