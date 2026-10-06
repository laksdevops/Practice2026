#!/bin/bash

SERVERS=("stapp01" "stapp02" "stapp03")
users=("tony" "steve" "banner")

for i in "${!SERVERS[@]}"
do
    SERVER="${SERVERS[$i]}"
    user="${users[$i]}"

    echo "======================================"
    echo "Configuring $SERVER using user $user"
    echo "======================================"

    ssh -t "$user@$SERVER" '
        echo "Removing existing PermitRootLogin entries..."

        sudo sed -i "/^[[:space:]]*#\?[[:space:]]*PermitRootLogin[[:space:]]/d" /etc/ssh/sshd_config

        echo "Adding PermitRootLogin no..."

        echo "PermitRootLogin no" | sudo tee -a /etc/ssh/sshd_config > /dev/null

        echo "Validating SSH configuration..."

        if sudo sshd -t
        then
            echo "SSH configuration is valid."

            sudo systemctl restart sshd

            if [ $? -eq 0 ]
            then
                echo "SSH service restarted successfully."
            else
                echo "Failed to restart SSH service."
                exit 1
            fi
        else
            echo "SSH configuration is INVALID."
            exit 1
        fi
    '

    if [ $? -eq 0 ]
    then
        echo "$SERVER completed successfully."
    else
        echo "$SERVER configuration failed."
    fi

    echo
done