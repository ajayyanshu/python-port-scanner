### Port Scanner Usage

1. **Clone the Script**: Clone the Python script to your local machine.

2. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing the script, and run the following command:
    ```bash
    sudo apt-get install python3
    sudo python3 port_scanner.py
    ```

3. **Follow the Prompts**: You'll be prompted to enter the target host (IP address or domain) and the range of ports you want to scan.

4. **View Results**: After providing the necessary inputs, the script will start scanning for open ports on the specified target host. Once the scan is complete, it will display a list of open ports, if any.

### Example:

```bash
Port Scanner
-------------
This script scans for open ports on a specified target host.
Enter the target host and range of ports to scan when prompted.
Enter the target host: 192.168.1.100
Enter the starting port: 1
Enter the ending port: 1024
Scanning target 192.168.1.100 ...
[+] Port 22/tcp is open
[+] Port 80/tcp is open
Scanning complete.
```
## Contact with us

For inquiries and support, please contact us at [ajayyanshu@gmail.com](mailto:ajayyanshu@gmail.com).

### Note:

- Ensure you have the necessary permissions to perform network scans, especially if scanning remote hosts.
- Avoid scanning hosts without proper authorization, as it may be considered malicious activity.
- The script uses multithreading to speed up the scanning process, but adjust the number of threads according to your system's capabilities.
