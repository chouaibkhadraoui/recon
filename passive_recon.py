# passive_recon.py
# This script performs basic reconnaissance on a domain.
#
# 🔧 What it does:
# - Creates a folder named recon_example.com
# - Runs WHOIS, dig, and nslookup to gather domain information
# - Retrieves certificate transparency data from crt.sh
# - Saves all outputs into text/JSON files inside the created folder
#
# 🧪 Requirements:
# Ensure the following tools are installed on your system:
# - whois
# - dig (part of dnsutils)
# - nslookup
# - curl
# - Python 3.x
# - made by me :p 

import subprocess
import sys
import os

def run_command(command, description):
    print(f"\n[+] {description}")
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        print(result.strip())
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to run: {command}\n{e}")

def main(domain):
    print(f"=== Passive Recon for: {domain} ===")

    # Create output folder
    folder = f"recon_{domain}"
    os.makedirs(folder, exist_ok=True)

    # WHOIS Lookup
    run_command(f"whois {domain} > {folder}/whois.txt", "WHOIS Lookup")

    # DNS Lookup (A, MX, NS, TXT)
    run_command(f"dig {domain} any +short > {folder}/dns_records.txt", "DNS Records")
    run_command(f"nslookup {domain} > {folder}/nslookup.txt", "NSLookup")

    # crt.sh Lookup via curl
    print("\n[+] Fetching subdomains from crt.sh...")
    try:
        response = subprocess.check_output(
            f'curl -s "https://crt.sh/?q=%25.{domain}&output=json"', shell=True, text=True
        )
        with open(f"{folder}/crtsh_subdomains.json", "w") as f:
            f.write(response)
        print("[+] Saved crt.sh results.")
    except subprocess.CalledProcessError:
        print("[-] Failed to fetch data from crt.sh")

    print(f"\n✅ All results saved in: {folder}/")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python passive_recon.py example.com")
        sys.exit(1)

    target = sys.argv[1]
    main(target)
