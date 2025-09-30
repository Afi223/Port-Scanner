import socket
import subprocess
import sys
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Define high-risk ports (commonly targeted by attackers)
HIGH_RISK_PORTS = {21, 22, 23, 25, 80, 110, 143, 445, 3389}


def port_scanner(ip, start_port, end_port, delay=0.2):
    print(f"[*] Scanning IP: {ip}, ports {start_port}-{end_port}")
    open_ports = []
    total_ports = end_port - start_port + 1
    scanned = 0

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()

            # Progress feedback
            scanned += 1
            if scanned % 50 == 0 or port == end_port:
                percent = (scanned / total_ports) * 100
                print(f"    Progress: {scanned}/{total_ports} ports scanned ({percent:.1f}%)")

            time.sleep(delay)  # to avoid hammering target too fast
        return open_ports
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()


def service_detection(ip, port):
    try:
        result = subprocess.check_output(['nmap', '-sV', '-p', str(port), ip])
        return result.decode()
    except Exception as e:
        return str(e)


def visualize_open_ports(ip, open_ports):
    if open_ports:
        services = []
        for port in open_ports:
            service_info = service_detection(ip, port)
            lines = service_info.split('\n')
            service = lines[1] if len(lines) > 1 else 'Unknown'
            services.append(service)

        colors = ["red" if port in HIGH_RISK_PORTS else "green" for port in open_ports]

        plt.figure(figsize=(14, 8))
        plt.bar([str(port) for port in open_ports],
                [1] * len(open_ports),
                color=colors, alpha=0.8, edgecolor='black')
        plt.xlabel('Port Numbers', fontsize=12, fontweight='bold')
        plt.ylabel('Status (1 = Open)', fontsize=12, fontweight='bold')
        plt.title(f'Open Ports and Services on {ip}', fontsize=14, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.6)

        for i, port in enumerate(open_ports):
            plt.text(str(port), 1.02, services[i], ha='center', fontsize=10, rotation=45, color='blue')

        plt.tight_layout()
        plt.show()
    else:
        print("No open ports to visualize.")


def main():
    print("=== Basic Vulnerability Scanner ===")
    target_ip = input("Enter the target IP address (e.g., scanme.nmap.org): ")
    start_port = int(input("Enter the start port (e.g., 1): "))
    end_port = int(input("Enter the end port (e.g., 65535): "))

    start_time = datetime.now()
    open_ports = port_scanner(target_ip, start_port, end_port, delay=0.1)

    print("\n[+] Scan completed in:", datetime.now() - start_time)
    print("Open Ports:")
    for port in open_ports:
        risk = " (HIGH-RISK)" if port in HIGH_RISK_PORTS else ""
        print(f"Port {port}: Open{risk}")
        service_info = service_detection(target_ip, port)
        print(service_info)

    visualize_open_ports(target_ip, open_ports)


if __name__ == "__main__":
    main()
