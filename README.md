# IP Checker API

A lightweight FastAPI-based service that checks the geolocation and proxy/VPN status of any IP address.

Developed by **Agenics N.V.**, a tech-driven iGaming solutions provider focused on compliance, scalability, and operational transparency.

---

## 🔍 Features

- Returns IP address, location, region, and ISP/org
- Detects potential VPN/proxy usage from org data
- Supports auto-detection or explicit IP query
- Simple JSON output for easy integration

---

## 🚀 Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
uvicorn ip_checker:app --reload
```

### Endpoints:

- `GET /check` — auto-detect your own IP
- `GET /check/{ip}` — check any IP explicitly

---

## 🔐 Optional: IPInfo Token

To enhance accuracy, you can use an [ipinfo.io](https://ipinfo.io) token:

```bash
export IPINFO_TOKEN=your_token_here
```

---

## 📦 Example Response

```json
{
  "ip": "8.8.8.8",
  "city": "Mountain View",
  "region": "California",
  "country": "US",
  "org": "Google LLC",
  "hostname": "dns.google",
  "location": "37.3860,-122.0838",
  "is_proxy_or_vpn": false
}
```

---

## 🧾 License
MIT

---

**Agenics N.V.** — powering secure and scalable technology for online gaming.
Visit us at [https://agenics.org](https://agenics.org)
