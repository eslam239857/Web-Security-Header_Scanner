# 🔐 Web Security Header Scanner

A lightweight Python tool that analyzes HTTP responses and checks for common web security headers.

## 🚀 Features

* 🔍 HTTP response analysis
* 🛡️ Security header detection
* 🔐 HTTPS/HSTS detection
* ⚠️ Identifies missing security headers
* 📊 Simple terminal-based results
* ⚡ Lightweight Python implementation

## 🛠️ Technologies

* Python
* Requests
* HTTP
* Web Security Headers

## 📋 Security Headers Checked

* `Strict-Transport-Security`
* `Content-Security-Policy`
* `X-Frame-Options`
* `X-Content-Type-Options`
* `Referrer-Policy`

## ⚙️ Installation

```bash
git clone https://github.com/eslam239857/Web-Security-Header-Scanner.git
cd Web-Security-Header-Scanner

python -m venv venv
```

### Windows

```powershell
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## ▶️ Usage

```bash
python scanner.py https://example.com
```

Example output:

```text
==================================================
       Web Security Header Scanner
==================================================

Target: https://example.com/
Status Code: 200

Security Headers:
[+] Strict-Transport-Security: PRESENT
[+] Content-Security-Policy: PRESENT
[-] X-Frame-Options: MISSING
[+] X-Content-Type-Options: PRESENT
[+] Referrer-Policy: PRESENT
```

## ⚠️ Disclaimer

This tool is intended for educational purposes, authorized security testing, and systems you own or have explicit permission to assess.

Do not scan systems without authorization.
