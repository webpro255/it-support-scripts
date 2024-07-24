# it-support-scripts
A collection of Python and Bash scripts for various IT support tasks, including monitoring, user management, and more.

Several scripts in this repository use positional parameters to accept arguments. Positional parameters are placeholders in the script that are replaced by actual values provided when the script is executed. This allows the scripts to be flexible and reusable for different inputs.

## Prerequisites

Ensure you have the following software installed on your system before running the scripts:

- **Python 3.x** (for Python scripts)
- **Bash** (for Bash scripts)
- **pip** (Python package installer)
- **smtplib** (for email notifications in Python scripts)
- **psutil** (for system health monitoring)

You can install `psutil` using pip:
```bash
pip install psutil
```

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

When running the script example :
  ```bash
  bash firewall_configuration.sh add 8080
  ```
### Contributing
Feel free to fork this repository and contribute by submitting a pull request.

### License
This project is licensed under the MIT License.





