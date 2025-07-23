# Phish Detekt– A CLI Phishing Link Scanner

**Phish Detekt**-A powerful Command Line Interface (CLI) tool for scanning and detecting potentially malicious, fraudulent, or phishing links. Built as part of a Cybersecurity & Ethical Hacking internship project, this scanner integrates URL heuristics, pattern matching, simulated threat detection, and risk scoring for accurate link assessment.

> 🧠 Developed for the Cyber Security Internship at **Brainwave Matrix Solutions**  
> ⚡ Fast, lightweight, and tuned to catch suspicious links in real time

---

## 🚀 Features

- 🔍 URL structure analysis
- 🌐 Google Safe Browsing API (simulated)
- 🔡 Unicode & obfuscated character detection
- 🧬 Base64 pattern check in URL paths
- 📦 Malware delivery vector detection
- 🔢 Risk scoring system (0–100)
- 🧾 Clear final verdict label (Safe / Suspicious / Risky / Dangerous)
- 📝 Scan log saved in `scan_report.txt`
- ✅ Clean and user-friendly CLI interface

---
## 📂 Folder Structure

PHISH-DETEKT/
├── banner.py # CLI banner display
├── scanner.py # URL scanning and analysis logic
├── main.py # CLI interface entry point
├── requirements.txt # Python dependencies
├── regex_patterns.py #for suspicious regex patterns
├── report.py #report generator
├── gsb_api.py #for google safe browsing api
├── scan_report.txt #report text file
├── README.md # Project documentation

## 🎓 Internship Context

> Built during the **Cyber Security Internship** at  
> **Brainwave Matrix Solutions** 🧠  
> Project folder and GitHub repo name follow official guidelines:  
> `Brainwave_Matrix_Intern`

---

## ⚙️ Requirements

- Python 3.7+
- No third-party dependencies needed

---

##  📦 Quick Setup

```bash
git clone https://github.com/kunalll0/Brainwave_Matrix_Intern.git
cd Brainwave_Matrix_Intern
# For Windows
python -m venv venv
venv\Scripts\activate

# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
Open scanner.py and update:
API_KEY = "your_api_key_here"
python main.py

### 👨‍💻 Author

```markdown
Kunal Prajapati  
BCA Student | Cybersecurity & Web Development Enthusiast  
LinkedIn: [https://www.linkedin.com/in/kunall0/](https://www.linkedin.com/in/kunall0/)
```
