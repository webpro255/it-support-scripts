# it-support-scripts
A collection of Python and Bash scripts for various IT support tasks, including monitoring, user management, and more.

Several scripts in this repository use positional parameters to accept arguments. Positional parameters are placeholders in the script that are replaced by actual values provided when the script is executed. This allows the scripts to be flexible and reusable for different inputs.

### Positional Parameters

- **$1**: Represents the first argument passed to the script.
- **$2**: Represents the second argument passed to the script.
- **$3**: Represents the third argument passed to the script, and so on.

## Scripts

### 1. Server Health Monitor
- **Description:** Monitors server health (CPU, memory, disk usage) and sends alerts if thresholds are exceeded.
- **File:** `server_health_monitor/server_health_monitor.py`
- **Usage:**
  ```bash
  python3 server_health_monitor/server_health_monitor.py
### 2. Network Connectivity Checker
- **Description:** Checks network connectivity and logs the results, sending alerts if issues are detected.
- **File:** `network_connectivity_checker/network_connectivity_checker.py`
- **Usage:**
  ```bash
  python3 network_connectivity_checker/network_connectivity_checker.py
### 3. User Management Script
- **Description:** Automates user account creation, deletion, and modification on a Linux system.
- **File:** `user_management/user_management.sh`
- **Usage:**
  ```bash
  bash user_management/user_management.sh {add|delete|modify} username [password]
  ```
### 4. Disk Usage Report
- **Description:** Generates a report of disk usage on a server and emails the report.
- **File:** `disk_usage_report/disk_usage_report.py`
- **Usage:**
  ```bash
  python3 disk_usage_report/disk_usage_report.py
### 5. Automated Backup Script
- **Description:** Automates the backup of important files and directories to a remote server.
- **File:** `automated_backup/automated_backup.sh`
- **Usage:**
  ```bash
  bash automated_backup/automated_backup.sh
### 6. Firewall Configuration Script
- **Description:** Automates the configuration of firewall rules on a Linux server.
- **File:** `firewall_configuration/firewall_configuration.sh`
- **Usage:**
  ```bash
  bash firewall_configuration/firewall_configuration.sh {add|delete|list} [port]
### Argument Usage in Scripts

For example, in the `firewall_configuration.sh` script:

```bash
sudo iptables -A INPUT -p tcp --dport "$1" -j ACCEPT
```
    $1 is add
    $2 is 8080

This command will add a rule to allow TCP traffic on port 8080.

When running the script example :
```bash
bash firewall_configuration.sh add 8080





