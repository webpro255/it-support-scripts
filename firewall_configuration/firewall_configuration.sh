#!/bin/bash

# Function to add a firewall rule
add_rule() {
    sudo iptables -A INPUT -p tcp --dport "$1" -j ACCEPT
    echo "Rule added to allow TCP traffic on port $1."
}

# Function to delete a firewall rule
delete_rule() {
    sudo iptables -D INPUT -p tcp --dport "$1" -j ACCEPT
    echo "Rule deleted for TCP traffic on port $1."
}

# Function to list all firewall rules
list_rules() {
    sudo iptables -L -v -n
}

# Main script
case "$1" in
    add)
        add_rule "$2"
        ;;
    delete)
        delete_rule "$2"
        ;;
    list)
        list_rules
        ;;
    *)
        echo "Usage: $0 {add|delete|list} [port]"
        exit 1
        ;;
esac
