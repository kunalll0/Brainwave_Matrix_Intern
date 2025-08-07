import re
import requests
from urllib.parse import urlparse
from colorama import Fore, Style

API_KEY = ''  # Replace with your actual API key
SAFE_BROWSING_API_URL = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=' + API_KEY

PHISHING_KEYWORDS = [
    "login", "verify", "secure", "account", "bank", "update", "confirm", "password", "signin"
]
SUSPICIOUS_TLDS = [".xyz", ".top", ".info", ".click", ".support", ".live", ".site", ".online", ".store"]
SHORTENERS = ["bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "buff.ly"]
BRAND_TARGETS = ["paypal", "google", "amazon", "facebook", "apple", "microsoft"]

def check_google_safe_browsing(url):
    payload = {
        "client": {"clientId": "yourcompany", "clientVersion": "1.5.2"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    try:
        response = requests.post(SAFE_BROWSING_API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            if "matches" in result:
                return True, [match['threatType'] for match in result['matches']]
            else:
                return False, []
    except:
        pass
    return False, []

def enhanced_heuristic_analysis(url):
    score = 0
    reasons = []

    if "://" not in url:
        url = "http://" + url

    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    domain = parsed.netloc.lower()
    full = (parsed.netloc + parsed.path).lower()

    if scheme != "https":
        score += 20
        reasons.append("Uses HTTP (not secure)")

    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", domain):
        score += 25
        reasons.append("URL uses raw IP address")

    if any(short in domain for short in SHORTENERS):
        score += 25
        reasons.append("URL shortener detected")

    hits = sum(1 for kw in PHISHING_KEYWORDS if kw in full)
    if hits:
        score += 10 * hits
        reasons.append(f"{hits} phishing keyword(s) found")

    domain_hits = sum(1 for kw in PHISHING_KEYWORDS if kw in domain)
    if domain_hits:
        score += 10 * domain_hits
        reasons.append(f"{domain_hits} keyword(s) in domain")

    if any(domain.endswith(tld) for tld in SUSPICIOUS_TLDS):
        score += 30
        reasons.append("Suspicious top-level domain")

    if domain.count(".") >= 2:
        score += 10
        reasons.append("Multiple subdomains")

    hyphens = domain.count("-")
    if hyphens >= 2:
        score += 15
        reasons.append("Multiple hyphens in domain")

    if "%" in parsed.path:
        score += 10
        reasons.append("Obfuscated characters in URL path")

    for brand in BRAND_TARGETS:
        if brand in domain and not domain.startswith(brand):
            score += 20
            reasons.append(f"Potential brand spoofing: {brand}")
            break

    if len(full) > 60:
        score += 10
        reasons.append("URL is unusually long")

    if not all(ord(c) < 128 for c in domain):
        score += 25
        reasons.append("Suspicious Unicode characters (possible homograph attack)")

    if re.search(r'(?:[A-Za-z0-9+/]{8,}={0,2})', parsed.path):
        score += 15
        reasons.append("Potential Base64-encoded payload in path")

    if parsed.path.endswith(('.exe', '.zip', '.apk', '.scr', '.dll', '.bat')):
        score += 20
        reasons.append("URL ends with suspicious file type")

    return min(score, 100), reasons

def scan_url(url):
    print(f"\nScanning: {url}\n{'-' * 60}")

    is_unsafe, threats = check_google_safe_browsing(url)
    score, reasons = enhanced_heuristic_analysis(url)

    if is_unsafe:
        score = max(score, 85)
        threats_str = ", ".join(threats)
        print(Fore.RED + f"[ALERT] Google Safe Browsing flagged this URL as: {threats_str}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "[Google Check] URL not flagged by Safe Browsing." + Style.RESET_ALL)

    print("[Heuristic Analysis] Risk Score:", end=" ")
    if score > 50:
        print(Fore.RED + f"{score}% - HIGH RISK" + Style.RESET_ALL)
    elif score > 30:
        print(Fore.MAGENTA + f"{score}% - UNSAFE" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"{score}% - SAFE" + Style.RESET_ALL)

    if score >= 80:
        label = "🔴 Dangerous"
    elif score >= 50:
        label = "🟠 Risky"
    elif score >= 30:
        label = "🟡 Suspicious"
    else:
        label = "🟢 Safe"

    print(f"🔖 Final Verdict: {label}")

    if reasons:
        print("Reasoning:")
        for reason in reasons:
            print(" -", reason)

    print("-" * 60)

    # === Predicting Type of Phishing ===
    print(Fore.LIGHTBLUE_EX + "\n[>] Predicting type of phishing attack...")

    phishing_type = "Unknown"
    url_lc = url.lower()

    if any(kw in url_lc for kw in ["login", "signin", "verify", "update-account", "auth"]):
        phishing_type = "Credential Harvesting (Fake Login Page)"
    elif any(kw in url_lc for kw in ["download", "exe", "apk", "update-software", "setup"]):
        phishing_type = "Malware Delivery"
    elif any(kw in url_lc for kw in ["gift", "free", "giveaway", "win", "survey"]):
        phishing_type = "Scam / Fake Offer"
    elif any(kw in url_lc for kw in ["support", "helpdesk", "service", "resolve"]):
        phishing_type = "Tech Support Scam"

    print(Fore.WHITE + f"🔎 Possible Phishing Type: {Fore.RED + phishing_type}")
    # print(Fore.CYAN + f"[RESULT] {label} - {phishing_type}")

    return f"{label} - {phishing_type}"