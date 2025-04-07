import requests
import sys

def get_subdomains(domain):
    print(f"[+] Searching for subdomains of: {domain}")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("[-] Error fetching data from crt.sh")
            return []
        data = response.json()
        subdomains = set()
        for entry in data:
            name = entry['name_value']
            for sub in name.split('\n'):
                if sub.endswith(domain):
                    subdomains.add(sub.strip())
        return sorted(subdomains)
    except Exception as e:
        print(f"[-] Exception occurred: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python subdomain_enum.py example.com")
        sys.exit(1)

    target = sys.argv[1]
    subs = get_subdomains(target)

    if subs:
        print(f"[+] Found {len(subs)} subdomains:")
        for s in subs:
            print(f" - {s}")
    else:
        print("[-] No subdomains found.")
