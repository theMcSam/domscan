'''
curl --request GET \
     --url https://www.virustotal.com/api/v3/ip_addresses/ip \
     --header 'accept: application/json'
'''
import requests
import os

BASE_URL = "https://www.virustotal.com/api/v3"

def check_ip(ip_address: str):
    resp = requests.get(
        f"{BASE_URL}/ip_addresses/{ip_address}",
        headers={
            "accept":"application/json",
            "x-apikey": os.environ.get("VIRUS_TOTAL_API_KEY")
        },
    )

    return format_response_data(resp.json())

def check_domain(domain: str):
    resp = requests.get(
        f"{BASE_URL}/domains/{domain}",
        headers={
            "accept":"application/json",
            "x-apikey": os.environ.get("VIRUS_TOTAL_API_KEY")
        },
    )
    return format_response_data(resp.json())

def format_response_data(resp_data: dict):
    resp = resp_data['data']

    scanners_and_detection_categories = {}
    for scanner, detection  in resp['attributes']['last_analysis_results'].items():
        scanners_and_detection_categories[scanner] = detection["category"]

    return scanners_and_detection_categories