import socket
import threading
from queue import Queue

# Function to perform port scan on a single port
def port_scan(target_host, port):
    try:
        # Create socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout to 1 second
        s.settimeout(1)
        # Attempt to connect to the target port
        s.connect((target_host, port))
        print(f"[+] Port {port}/tcp is open")
    except:
        pass
    finally:
        # Close the socket
        s.close()

# Function to scan a range of ports
def scan_ports(target_host, ports):
    print(f"Scanning target {target_host} ...")
    # Create a queue to hold port numbers
    port_queue = Queue()
    # Put ports into the queue
    for port in ports:
        port_queue.put(port)

    # Create threads to perform port scanning
    def worker():
        while not port_queue.empty():
            port = port_queue.get()
            port_scan(target_host, port)
            port_queue.task_done()

    # Create 20 threads
    for _ in range(20):
        t = threading.Thread(target=worker)
        t.start()

    # Wait for all threads to finish
    port_queue.join()
    print("Scanning complete.")

def main():
    print("Port Scanner")
    print("-------------")
    print("This script scans for open ports on a specified target host.")
    print("Enter the target host and range of ports to scan when prompted.")

    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    ports = range(start_port, end_port + 1)
    scan_ports(target_host, ports)

if __name__ == "__main__":
    main()
