import requests
import json

API_KEY = "" 

def check_safe_browsing(url):
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
    
    payload = {
        "client": {
            "clientId": "phish-scanner",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    response = requests.post(endpoint, json=payload)
    
    try:
        matches = response.json().get("matches", [])
        if matches:
            threat_types = [match["threatType"] for match in matches]
            return False, threat_types  # Unsafe, with threats
        else:
            return True, []  # Safe
    except Exception:
        return False, ["UNKNOWN_ERROR"]