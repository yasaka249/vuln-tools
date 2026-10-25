# SQLi Framework (PoC)
This tool is a PoC framework for automatically detecting SQL injection vulnerabilities in a web application and verifying authentication bypasses.

## Disclaimer
- This tool is created solely for educational and research purposes, and for learning security assessments (penetration testing) in environments with legitimate authority.
- Execution on unauthorized targets (such as servers belonging to real third parties) is prohibited by law.
- The developers assume no responsibility whatsoever for any damages or legal liabilities arising from the use of this tool.

## Features
- Automatic parameter scanning: It automatically extracts input fields from the form and identifies vulnerable areas.
- Detection logic: By combining similarity Calculations (Length/Body) with various response codes, false positives are minimized.
- Token auto-tracking: It dynamically parses sessions and tokens, supporting robust web applications.

## Setup
```bash
# Installing dependent libraries
pip install -r requirements.txt
```

## Usage
```bash
# Automatic scan mode
python3 sqli.py -u "http://target-url"

# Parameter specification mode
python3 sqli.py -u "http://target-url" -p "email"
```
