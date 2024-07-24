#!/bin/bash

# Function to add a user
add_user() {
    username=$1
    password=$2
    sudo useradd -m -s /bin/bash "$username"
    echo "$username:$password" | sudo chpasswd
    echo "User $username added successfully."
}

# Function to delete a user
delete_user() {
    username=$1
    sudo userdel -r "$username"
    echo "User $username deleted successfully."
}

# Function to modify a user (e.g., change password)
modify_user() {
    username=$1
    new_password=$2
    echo "$username:$new_password" | sudo chpasswd
    echo "User $username's password changed successfully."
}

# Main script
case "$1" in
    add)
        add_user "$2" "$3"
        ;;
    delete)
        delete_user "$2"
        ;;
    modify)
        modify_user "$2" "$3"
        ;;
    *)
        echo "Usage: $0 {add|delete|modify} username [password]"
        exit 1
        ;;
esac
