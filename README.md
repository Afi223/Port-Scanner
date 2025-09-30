# Basic Port Scanner

**Scanner.py** — a small, educational port scanner (python).  
This repository contains a simple port scanner for learning and testing network behavior on systems you own or have written permission to test.

---

## Features
- Scans a range of TCP ports on a target host.
- Performs simple service detection using `nmap` (if installed) or a banner-grab fallback.
- Prints progress while scanning.
- Highlights a small set of common high-risk ports in output/visualization.
- Includes an optional Matplotlib visualization of open ports.

---

## Requirements
- Python 3.8+
- (Optional) `nmap` binary installed and available in `PATH` for enhanced service detection
- Python packages (if using visualization):
  - `matplotlib`

Install Python deps:
```bash
python3 -m pip install matplotlib
