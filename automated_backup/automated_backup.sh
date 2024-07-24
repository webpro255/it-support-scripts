#!/bin/bash

# Variables
backup_source="/path/to/important/files"
backup_dest="/path/to/backup/location"
remote_server="user@remote-server:/path/to/remote/backup"

# Create a backup
tar -czf "$backup_dest/backup-$(date +%F).tar.gz" "$backup_source"

# Copy the backup to a remote server
scp "$backup_dest/backup-$(date +%F).tar.gz" "$remote_server"

# Cleanup old backups (older than 7 days)
find "$backup_dest" -type f -name "*.tar.gz" -mtime +7 -exec rm {} \;

echo "Backup completed successfully."
