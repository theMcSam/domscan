'''
https://urlscan.io/api/v1/search/?q=domain:urlscan.io
'''
import requests

BASE_URL= "https://urlscan.io/api/v1"

def check_domain(domain: str):
    resp = requests.get(
        f"{BASE_URL}/search",
        params={"q":f"domain:{domain}"}
    )
    return format_response_data(resp.json())

def format_response_data(resp_data: dict):
    final_result = {"domains": []}
    resp = resp_data["results"]

    for res in resp:
        final_result["domains"].append(res["page"]["domain"])
        print(f"PAGE: {res['page']}")
        final_result[res["page"].get("domain", "unknown")] = {
        "ip": res["page"].get("ip", "N/A"),
        "server": res["page"].get("server", "N/A"),
        "title": res["page"].get("title", "N/A"),
        "tlsAgeDays": res["page"].get("tlsAgeDays", 0),  # Default to 0 for numerical fields
        "tlsIssuer": res["page"].get("tlsIssuer", "N/A"),
        "tlsValidDays": res["page"].get("tlsValidDays", 0),
        "tlsValidFrom": res["page"].get("tlsValidFrom", "N/A")
    }
    
    return final_result