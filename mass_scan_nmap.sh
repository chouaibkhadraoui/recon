#!/bin/bash

# mass_scan_nmap.sh
# Description: Mass scan a list of targets using nmap and save organized results

INPUT_FILE="$1"
OUTPUT_DIR="nmap_scans_$(date +%F_%H-%M-%S)"

# Basic sanity check
if [ -z "$INPUT_FILE" ]; then
    echo "Usage: ./mass_scan_nmap.sh targets.txt"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo "[+] Starting mass scan..."
while IFS= read -r TARGET; do
    if [ -z "$TARGET" ]; then
        continue
    fi

    echo "[+] Scanning $TARGET..."
    nmap -sS -sV -T4 -Pn -oN "$OUTPUT_DIR/$TARGET.txt" "$TARGET"
done < "$INPUT_FILE"

echo "[+] All scans saved in: $OUTPUT_DIR/"
