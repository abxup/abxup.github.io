#!/usr/bin/env python
import subprocess

# Update package lists
subprocess.run(["sudo", "apt-get", "update"])

# Install necessary packages
subprocess.run(["sudo", "apt-get", "install", "ca-certificates", "curl", "gnupg"])

# Create directory for keyrings
subprocess.run(["sudo", "install", "-m", "0755", "-d", "/etc/apt/keyrings"])

# Download and install Docker GPG key
subprocess.run(["curl", "-fsSL", "https://download.docker.com/linux/ubuntu/gpg", "|", "sudo", "gpg", "--dearmor", "-o", "/etc/apt/keyrings/docker.gpg"])
subprocess.run(["sudo", "chmod", "a+r", "/etc/apt/keyrings/docker.gpg"])

# Get Ubuntu version codename
version_codename = subprocess.check_output("source /etc/os-release && echo $VERSION_CODENAME", shell=True).decode("utf-8").strip()

# Add Docker repository to sources list
docker_repository = f"deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu {version_codename} stable"
with open("/etc/apt/sources.list.d/docker.list", "w") as docker_list:
    docker_list.write(docker_repository)

# Update package lists again
subprocess.run(["sudo", "apt-get", "update"])

# Install Docker
subprocess.run(["sudo", "apt-get", "install", "docker-ce", "docker-ce-cli", "containerd.io", "docker-buildx-plugin", "docker-compose-plugin"])

print("Docker安装完成")
