from flask import Flask, request
from apis import shodan, abuseipdb, virustotal, urlscan
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    ...

@app.route("/search")
def search():
    domain = request.args.get("domain")
    ip = request.args.get("ip")

    results = {}

    if ip:
        print("IP SCAN")
        results["scan_type"] = "IP"
        results["details"] = {
            "shodan": shodan.query_shodan_api(ip),
            "abuse_ip_db": abuseipdb.check_ip(ip),
            "virus_total": virustotal.check_ip(ip),
        }
    elif domain:
        print("DOMAIN SCAN")
        results["scan_type"] = "Domain"
        results["details"] = {
            "virus_total": virustotal.check_domain(domain),
            "urlscan": urlscan.check_domain(domain),
        }
    else:
        return {"error": "No IP or domain provided"}, 400

    return results

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)