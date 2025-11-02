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

## Donations

If you find python port scanner useful and would like to support its development, please consider making a donation. Your contributions help us maintain and improve the project.

[![Donate](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd9o3K2CK9LObsNOok8nY4WYMSwKkhAzsz7NDxmO8eZU-d8dw4kEKW1Ycp3QpzVsT2okmWwoBXLXB757yQhoL0Xandlt3Wjwdw7tTlU4hTGdJcFH1tq1i0K6o7uTTGK-20fKi7DQhgoYEZkHI1-Y9UPBWAjiNhtn8TceqHS4O6kTaaeNweZe6OBJ0Ve0ou/s424/download.png)](https://buymeacoffee.com/ajayyanshu)

[![Donate](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMgW12teTME3e1Ap4Lc6MuQ7mFoEfyKINWAQ8dDx0vRR6XXNXGNXSaOgFdFhB2kTv8d6r5TiMIpRqJv9EnrM2YU1Syrvq4KO32YcmjiJk-GLuxHGMwfTPIO1Zz1JE2lCSMTRcrY1JJues1jpC4qotBNumo3d3dC79uRFulGasM8vzSdneJmzunxKDiUKI2/s386/upi.PNG)]()
## Contact with us

For inquiries and support, please contact us at [ajayyanshu@gmail.com](mailto:ajayyanshu@gmail.com).

### Note:

- Ensure you have the necessary permissions to perform network scans, especially if scanning remote hosts.
- Avoid scanning hosts without proper authorization, as it may be considered malicious activity.
- The script uses multithreading to speed up the scanning process, but adjust the number of threads according to your system's capabilities.
