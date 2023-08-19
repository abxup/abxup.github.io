#!/usr/bin/env python
import os
import shutil
import subprocess
import tarfile
import urllib.request

# JDK download URL
jdk_url = "https://download.oracle.com/java/17/archive/jdk-17.0.8_linux-x64_bin.tar.gz"

# Define installation paths
download_path = "/tmp/jdk-17.tar.gz"
extracted_path = "/tmp/jdk-17.0.8"
install_path = "/opt/java/jdk-17.0.8"
profile_path = "/etc/profile"

# Download JDK
urllib.request.urlretrieve(jdk_url, download_path)
print("JDK 17压缩包下载完成")

# Extract JDK
with tarfile.open(download_path, "r:gz") as tar:
    tar.extractall(path=extracted_path)
print("JDK 17压缩包解压完成")

# Move to install location
if os.path.exists(install_path):
    shutil.rmtree(install_path)
shutil.move(extracted_path, install_path)
print("JDK 17安装到/opt/java目录")

# Update environment variables in /etc/profile
java_env_vars = """
##JDK-17
export JAVA_HOME=/opt/java/jdk-17.0.8
export CLASSPATH=.:$JAVA_HOME/lib/
export PATH=.:$JAVA_HOME/bin:$PATH
"""

with open(profile_path, "a") as profile:
    profile.write(java_env_vars)
print("环境变量已添加到/etc/profile末尾")

# Reload /etc/profile
subprocess.run(["source", profile_path], shell=True)
print("已重新加载/etc/profile")

print("JDK 17安装完成并配置好环境变量")
