import datetime

def log_report(url, result):
    if result is None:
        result = "No scan result returned ❗"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("scan_report.txt", "a", encoding="utf-8") as file:

        file.write(f"[{timestamp}] URL: {url}\n")
        file.write(f"Scan Result: {result}\n")
        file.write("=" * 50 + "\n")