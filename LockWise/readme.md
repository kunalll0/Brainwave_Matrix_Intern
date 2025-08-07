# LockWise– A CLI Password Strength Checker

**LockWise**A command-line tool designed to evaluate the strength and security of user-provided passwords. Developed during my Cybersecurity & Ethical Hacking Internship at Brainwave Matrix Solutions, this tool leverages entropy scoring, pattern analysis, and online breach detection using API key of Pwned_passwords from their site to determine whether a password is Strong, Moderate, or Weak — and whether it's been exposed in known leaks.


---

## 🚀 Features

- 🔍 User Input
- 🌐 Pwned_passwords API to detect breaches
- 🔡 Also checks offline commom passwords
- 🧾 Clear final verdict label (strong/ moderate / weak)
- ✅ Clean and user-friendly CLI interface

---
## 📂 Folder Structure

Brainwave_Matrix_Intern/Brainwave_Matrix_Intern/LockWise
├── banner.py # CLI banner display
├── checker.py # URL scanning and analysis logic
├── main.py # CLI interface entry point
├── common.txt # common passwords
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
cd Brainwave_Matrix_Intern/Brainwave_Matrix_Intern/LockWise
# For Windows
python -m venv venv
venv\Scripts\activate
python main.py

```

---
## 👨‍💻 Author

**Kunal Prajapati**  
BCA Student | Cybersecurity & Web Development Enthusiast  

🔗 [LinkedIn](https://www.linkedin.com/in/kunall0/)