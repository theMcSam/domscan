'''
curl -G https://api.abuseipdb.com/api/v2/check \
  --data-urlencode "ipAddress=118.25.6.39" \
  -d maxAgeInDays=90 \
  -d verbose \
  -H "Key: " \
  -H "Accept: application/json"
'''
import requests
import os

BASE_URL="https://api.abuseipdb.com/api/v2"

def check_ip(ip_address: str):
    resp = requests.get(
        f"{BASE_URL}/check", 
        headers={
            "Key": os.environ.get("ABUSE_IPDB_API_KEY"), 
            "Accept": "application/json"
        },
        params={'ipAddress': ip_address}
    )

    return resp.json()['data']