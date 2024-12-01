import requests

def query_shodan_api(ip_address: str):
    base_url = "https://internetdb.shodan.io/"

    
    ip_request = requests.get(f"{base_url}/{ip_address}")
        
    return ip_request.json()
