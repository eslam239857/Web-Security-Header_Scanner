import sys
import requests


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]


def scan_website(url):

    # Add https if the user did not provide a protocol
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\n[*] Scanning: {url}\n")

    try:
        response = requests.get(
            url,
            timeout=10
        )

    except requests.RequestException as error:
        print(f"[!] Request failed: {error}")
        return

    print("=" * 50)
    print("       Web Security Header Scanner")
    print("=" * 50)

    print(f"Target: {response.url}")
    print(f"Status Code: {response.status_code}")

    print("\nSecurity Headers:")

    for header in SECURITY_HEADERS:

        if header in response.headers:
            print(f"[+] {header}: PRESENT")
        else:
            print(f"[-] {header}: MISSING")

    print("\n" + "=" * 50)


def main():

    if len(sys.argv) != 2:

        print("Usage:")
        print("python scanner.py <URL>")
        print("\nExample:")
        print("python scanner.py https://example.com")

        sys.exit(1)

    url = sys.argv[1]

    scan_website(url)


if __name__ == "__main__":
    main()