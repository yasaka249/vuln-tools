# SQLi Framework (PoC)
This tool is a PoC framework for automatically detecting SQL injection vulnerabilities in a web application, verifying authentication bypasses and extracting database schemas and records.

## Disclaimer
- This tool is created solely for educational and research purposes, and for learning security assessments (penetration testing) in environments with legitimate authority.
- Execution on unauthorized targets (such as servers belonging to real third parties) is prohibited by law.
- The developers assume no responsibility whatsoever for any damages or legal liabilities arising from the use of this tool.

## Features
- **Automatic parameter scanning**: Automatically extracts input fields, URL query parameters, and cookies to identify vulnerable areas.
- **Multi-technique detection logic**: Supports **Error-based**, **Boolean-based**, and **Time-based** SQL injection detection. Combines similarity calculations (Length/Body) with response code analysis to minimize false positives.
- **Schema extraction (`schema` mode)**: Extracts database names, tables, and columns via Blind SQL injection (MySQL, PostgreSQL, SQLite) and exports the structured hierarchy to `schema_tree.json`.
- **Record data dumping (`data` mode)**: Extracts actual table records by specifying target tables and columns (`-T`, `-C`), or automatically loads column definitions from `schema_tree.json`. Outputs dumped records to `dump_<table_name>.json` (verified against PortSwigger Web Security Academy Blind SQLi labs).
- **Optimized HTTP client**: Caches form data instead of fetching it repeatedly, significantly reducing redundant network requests and improving scan speed.
- **Token auto-tracking**: Dynamically parses sessions and CSRF tokens, supporting stateful web applications.


## Setup
```bash
# Installing dependent libraries
pip install -r requirements.txt
```

## Usage
```bash
# Automatic scan & authentication bypass mode (default)
python3 sqli.py -u "http://target-url"

# Parameter specification mode
python3 sqli.py -u "http://target-url" -p "email"

# Schema extraction mode (outputs to schema_tree.json)
python3 sqli.py -u "http://target-url" -m extract
python3 sqli.py -u "http://target-url" -m extract -p "email"

# data dump mode (auto-loads columns from schema_tree.json if -C is omitted)
python3 sqli.py -u "http://target-url" -m data -T "users"

# data dump mode with explicit database, columns, and row limit
python3 sqli.py -u "http://target-url" -m data -D "public" -T "users" -C "username,password" --limit 10
```

## Limitations / Roadmap
- **Blind SQLi extraction engine**: Currently, 'schema' and 'data' mode rely on Boolean-based conditional responses. Support for Error-based and Time-based conditional extraction is planned.
- **Concurrent requests**: Implementing multi-threading('ThreadPoolExecutor') to accelerate character binary search extraction.
