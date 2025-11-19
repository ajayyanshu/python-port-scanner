import socket
import threading
from queue import Queue
import argparse
import sys

# Try to import colorama for cool visuals, but don't crash if it's missing
try:
    from colorama import init, Fore
    init()
    GREEN = Fore.GREEN
    RED = Fore.RED
    RESET = Fore.RESET
    CYAN = Fore.CYAN
except ImportError:
    # Fallback if colorama is not installed
    GREEN = ""
    RED = ""
    RESET = ""
    CYAN = ""

class PortScanner:
    def __init__(self):
        # We will store a list of dictionaries: [{'port': 80, 'service': 'http', 'banner': 'Apache'}]
        self.results = [] 
        self.port_queue = Queue()
        self.lock = threading.Lock() # Prevents threads from printing over each other

    def _get_banner(self, s):
        """Attempts to grab a banner from the socket."""
        try:
            # Some services wait for the client to speak first.
            # We can try sending a generic byte to trigger a response if reading fails.
            # For now, we just try to read.
            return s.recv(1024).decode().strip()
        except:
            return "No Banner"

    def _scan_port(self, target_host, port):
        """Scans a single port and attempts to identify the service."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1) # 1 second timeout
            s.connect((target_host, port))
            
            # 1. Identify Service Name (e.g., 'ssh', 'http')
            try:
                service_name = socket.getservbyport(port)
            except:
                service_name = "Unknown Service"

            # 2. Grab Banner
            # (Optional: Send a trigger for HTTP ports)
            if port == 80 or port == 443:
                try:
                    s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                except:
                    pass
            
            banner = self._get_banner(s)
            
            # 3. Save Results
            result_data = {
                "port": port,
                "service": service_name,
                "banner": banner
            }

            with self.lock:
                print(f"{GREEN}[+] Port {port} is OPEN | {service_name} | {banner}{RESET}")
                self.results.append(result_data)
            
            s.close()
            
        except:
            # Port is closed or filtered
            pass

    def _worker(self, target_host):
        """Worker thread to process the queue."""
        while not self.port_queue.empty():
            port = self.port_queue.get()
            self._scan_port(target_host, port)
            self.port_queue.task_done()

    def run_scan(self, target_host, start_port, end_port, thread_count=50):
        """
        Main function to start the scan.
        """
        self.results = [] # Reset results
        
        print(f"{CYAN}[*] Starting scan on {target_host} ({start_port}-{end_port})...{RESET}")
        
        # Fill Queue
        for port in range(start_port, end_port + 1):
            self.port_queue.put(port)

        # Start Threads
        thread_list = []
        for _ in range(thread_count):
            t = threading.Thread(target=self._worker, args=(target_host,))
            t.start()
            thread_list.append(t)

        # Wait for completion
        self.port_queue.join()
        
        print(f"{CYAN}[*] Scan Complete. Found {len(self.results)} open ports.{RESET}")
        
        # Return the structured data
        return sorted(self.results, key=lambda x: x['port'])

# ==========================================
# CLI INTERFACE (If running directly)
# ==========================================
if __name__ == "__main__":
    # This block handles command line arguments
    parser = argparse.ArgumentParser(description="Advanced Python Port Scanner for Sofia AI")
    
    parser.add_argument("target", help="Target IP Address (e.g., 192.168.1.1)")
    parser.add_argument("-sp", "--start_port", type=int, default=1, help="Start Port (default: 1)")
    parser.add_argument("-ep", "--end_port", type=int, default=1000, help="End Port (default: 1000)")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Number of threads (default: 50)")
    
    args = parser.parse_args()

    try:
        # Resolve hostname to IP if necessary
        target_ip = socket.gethostbyname(args.target)
        print(f"{CYAN}[*] Resolved {args.target} to {target_ip}{RESET}")
        
        scanner = PortScanner()
        scanner.run_scan(target_ip, args.start_port, args.end_port, args.threads)
        
    except socket.gaierror:
        print(f"{RED}[!] Error: Could not resolve hostname {args.target}{RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Scan interrupted by user.{RESET}")
        sys.exit()
