#!/usr/bin/env python
import os

# Define the path to the netplan configuration file
netplan_path = "/etc/netplan/"

# Get the list of netplan configuration files
netplan_files = [filename for filename in os.listdir(netplan_path) if filename.endswith(".yaml")]

# Display available netplan configuration files
print("Available netplan configuration files:")
for i, filename in enumerate(netplan_files):
    print(f"{i+1}. {filename}")

# Ask the user to select a netplan configuration file
selection = input("Enter the number of the netplan configuration file you want to modify: ")
selected_file = None

try:
    selection = int(selection)
    if 1 <= selection <= len(netplan_files):
        selected_file = netplan_files[selection - 1]
    else:
        print("Invalid selection.")
except ValueError:
    print("Invalid input.")

if selected_file:
    # Ask the user for IP, gateway, and DNS information
    ip_address = input("Enter the static IP address: ")
    gateway = input("Enter the gateway address: ")
    dns_servers = input("Enter DNS server addresses (comma-separated): ").split(",")

    # Generate the new netplan configuration content
    netplan_content = f"""
network:
  ethernets:
    enp3s0:
      dhcp4: no
      addresses: [{ip_address}/24]
      gateway4: {gateway}
      nameservers:
        addresses: {dns_servers}
  version: 2
"""

    # Write the new content to the selected netplan configuration file
    selected_file_path = os.path.join(netplan_path, selected_file)
    with open(selected_file_path, "w") as file:
        file.write(netplan_content)

    # Apply the netplan configuration
    os.system("sudo netplan apply")
    print("Netplan configuration updated and applied.")
else:
    print("Exiting.")
