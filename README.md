# PortGuard

**Scanner.py** — a educational port scanner (python).  
This repository contains a  port scanner for learning and testing network behavior on systems you own or have written permission to test.

---
## ⚠️ Warning

- **Unauthorized use of port scanners may be illegal.** Many networks and service providers treat port scanning as hostile activity.
- Running this scanner against systems you **do not own** or do **not have explicit written permission** to test can result in **account suspension, IP bans, legal action, or other consequences**.
- Always obtain **explicit written authorization** from the system/network owner before performing any scan.
- Use this tool **only** on your own machines, in isolated lab environments, or on publicly provided test targets (for example: `scanme.nmap.org`).
- By using this code you accept **full responsibility** for your actions and any consequences that may follow.

**If you are unsure, stop and ask for permission.**
---
## Features
- Scans a range of TCP ports on a target host.
- Performs simple service detection using `nmap` (if installed) or a banner-grab fallback.
- Prints progress while scanning.
- Highlights a set of common high-risk ports in output/visualization.
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
