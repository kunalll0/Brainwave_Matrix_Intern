# === regex_patterns.py ===

regex_heuristics = [
    (r"https?:\/\/[\w\-]+(\.[\w\-]+)*\.\w{2,}(\/.*)?\?.*(login|verify|secure)", "Suspicious query in URL"),
    (r"(login|signin|secure|account).*(\.php|\.html|\.asp)", "Phishing-style page name"),
    (r"\/\/(bit\.ly|tinyurl\.co|ow\.ly|t\.co)", "URL shortener used"),
    (r"\@\w+", "Possible attempt to mislead with @ symbol"),
    (r"(\/\/)?[\w\-]+(\.[\w\-]+){1,}\.\w{2,}(\/)?[a-z0-9%\/\.\?\&\=]*", "Generic suspicious structure"),
]