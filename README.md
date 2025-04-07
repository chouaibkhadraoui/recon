# recon
Tools &amp; scripts for information gathering

This section contains tools, scripts, and notes for **information gathering** — the first phase of any cybersecurity assessment, bug bounty, or penetration test. Recon helps map the target surface and find potential entry points.

---

### 🧰 Tools & Techniques

- **Passive Recon**  
  - `whois`, `nslookup`, `crt.sh`, `theHarvester`, `shodan`, `hunter.io`  
  - No direct interaction with the target

- **Active Recon**  
  - `nmap`, `dirsearch`, `nikto`, `ffuf`, `httpx`, `subfinder`  
  - Probes the target for open ports, directories, and services

---

### 📜 Example Scripts

- [`subdomain_enum.py`](https://github.com/chouaibkhadraoui/recon/blob/main/subdomain_enum.py)  – Automates subdomain discovery using public APIs  
- [`passive_recon.py`](https://github.com/chouaibkhadraoui/recon/blob/main/passive_recon.py) – Shell script combining `whois`, `dig`, and `nslookup`  
- `mass_scan_nmap.sh` – Mass scan targets and export clean reports

---

### 🧠 Notes

- Always begin with passive techniques to avoid detection  
- Check for exposed dev/staging subdomains (e.g., `dev.domain.com`, `test.api.domain.com`)  
- Screenshot large sets of URLs with tools like `gowitness` or `aquatone`

---

### 🔗 Useful Resources

- [Recon-ng](https://github.com/lanmaster53/recon-ng)  
- [Assetfinder](https://github.com/tomnomnom/assetfinder)  
- [Bug Bounty Recon Flowchart](https://github.com/nahamsec/recon_profile)

---

