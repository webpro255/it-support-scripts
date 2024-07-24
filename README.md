# it-support-scripts
A collection of Python and Bash scripts for various IT support tasks, including monitoring, user management, and more.

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


