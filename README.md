# it-support-scripts
A collection of Python and Bash scripts for various IT support tasks, including monitoring, user management, and more.

## Prerequisites

Ensure you have the following software installed on your system before running the scripts:

- **Python 3.x** (for Python scripts)
- **Bash** (for Bash scripts)
- **pip3** (Python package installer)
- **smtplib** (for email notifications in Python scripts)
- **psutil** (for system health monitoring)

You can install `psutil` using pip:
```bash
pip3 install psutil
```
### Installation
 **Clone the repository:**
   ```bash
   git clone https://github.com/webpro255/it-support-scripts.git
   cd it-support-scripts
   ```
**Navigate to the respective script folder:**
   ```bash
   cd server_health_monitor  # Example for the server health monitor script
   ```
**Install required Python packages:**
  ```bash
  pip3 install -r requirements.txt
  ```
### Configuration

Some scripts require configuration before they can be used.

Several scripts in this repository also use positional parameters to accept arguments. Positional parameters are placeholders in the script that are replaced by actual values provided when the script is executed. This allows the scripts to be flexible and reusable for different inputs.

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
  ```
- **Configuration:**
  Update the email configuration section in the script with your email server details:
  ```python
  smtp_server = 'smtp.your-email-provider.com'
  smtp_port = 587
  email_user = 'your-email@example.com'
  email_password = 'your-email-password'
  email_to = 'alert-recipient@example.com'
  ```
- **Example Output:**
  ```csharp
  CPU usage is 85%
  High CPU usage: 85%
  ```
### 2. Network Connectivity Checker
- **Description:** Checks network connectivity and logs the results, sending alerts if issues are detected.
- **File:** `network_connectivity_checker/network_connectivity_checker.py`
- **Usage:**
  ```bash
  python3 network_connectivity_checker/network_connectivity_checker.py
  ```
- **Configuration:**
  Update the email configuration section in the script with your email server details:
  ```python
  smtp_server = 'smtp.your-email-provider.com'
  smtp_port = 587
  email_user = 'your-email@example.com'
  email_password = 'your-email-password'
  email_to = 'alert-recipient@example.com'
  ```
 - **Example Output:**
  ```csharp
  8.8.8.8 is down!
  Network Connectivity Alert: 8.8.8.8 is down!
  ```

### 3. User Management Script
- **Description:** Automates user account creation, deletion, and modification on a Linux system.
- **File:** `user_management/user_management.sh`
  
- **Configuration:**
  No specific configuration is required for this script other than having the necessary permissions to add, delete, and modify user accounts. Ensure that you run this script with sudo or as a user with sufficient privileges

- **Usage:**
  ```bash
  bash user_management/user_management.sh {add|delete|modify} username [password]
  ```
- **Add a user:** ```bash user_management/user_management.sh add username password```
- **Delete a user:** ```bash user_management/user_management.sh delete username```
- **Modify a user’s password:** ```bash user_management/user_management.sh modify username new_password```

### 4. Disk Usage Report
- **Description:** Generates a report of disk usage on a server and emails the report.
- **File:** `disk_usage_report/disk_usage_report.py`
- **Usage:**
  ```bash
  python3 disk_usage_report/disk_usage_report.py
- **Configuration**
  ```python
  smtp_server = 'smtp.your-email-provider.com'
  smtp_port = 587
  email_user = 'your-email@example.com'
  email_password = 'your-email-password'
  email_to = 'alert-recipient@example.com'
  ```
- **Example Output:**
  ```bash
  Subject: Disk Usage Report

  Filesystem      Size  Used Avail Use% Mounted on
  /dev/sda1        50G   20G   28G  42% /
  tmpfs            32G     0   32G   0% /dev/shm
  /dev/sdb1       100G   70G   30G  70% /data
   ```
### 5. Automated Backup Script
- **Description:** Automates the backup of important files and directories to a remote server.
- **File:** `automated_backup/automated_backup.sh`
- **Usage:**
  ```bash
  bash automated_backup/automated_backup.sh
  ```
- **Configuration:**
  Update the paths and remote server details in the automated_backup.sh script:
  ```bash
  backup_source="/path/to/important/files"
  backup_dest="/path/to/backup/location"
  remote_server="user@remote-server:/path/to/remote/backup"
  ```
### 6. Firewall Configuration Script
- **Description:** Automates the configuration of firewall rules on a Linux server.
- **File:** `firewall_configuration/firewall_configuration.sh`
- **Usage:**
  ```bash
  bash firewall_configuration/firewall_configuration.sh {add|delete|list} [port]

- **When running the script example :**
  ```bash
  bash firewall_configuration.sh add 8080
  ```
### Contributing
Feel free to fork this repository and contribute by submitting a pull request.

### License
This project is licensed under the MIT License.





