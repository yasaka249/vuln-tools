# SQLi Framework (PoC)
This tool is a PoC framework for automatically detecting SQL injection vulnerabilities in a web application and verifying authentication bypasses.

## Disclaimer
- This tool is created solely for educational and research purposes, and for learning security assessments (penetration testing) in environments with legitimate authority.
- Execution on unauthorized targets (such as servers belonging to real third parties) is prohibited by law.
- The developers assume no responsibility whatsoever for any damages or legal liabilities arising from the use of this tool.

## Features
- **Automatic parameter scanning**: Automatically extracts input fields from forms and identifies vulnerable areas.
- **Multi-technique detection logic**: Supports **Error-based**, **Boolean-based**, and **Time-based** SQL injection detection. Combines similarity calculations (Length/Body) with response code analysis to minimize false positives.
- **Schema extraction (`extract` mode)**: Capable of extracting database schema information via Blind SQL injection and exporting the structured result to `schema_tree.json` (verified against PortSwigger Web Security Academy Blind SQLi labs).

- **Optimized HTTP client**: Caches form data instead of fetching it repeatedly, significantly reducing redundant network requests and improving scan speed.
- **Token auto-tracking**: Dynamically parses sessions and CSRF tokens, supporting stateful web applications.

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

# Schema extraction mode
python3 sqli.py -u "http://target-url" -m extract

python3 sqli.py -u "http://target-url" -m extract -p "email"
```

## Limitations / Roadmap
- **Record/Data extraction**: Currently supports database schema extraction only; full table record dumping is not yet implemented.
