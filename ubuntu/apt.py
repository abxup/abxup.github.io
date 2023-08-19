#!/usr/bin/env python

# Define the new mirror URLs
new_mirror_urls = [
    "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ lunar main restricted universe multiverse",
    "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ lunar-updates main restricted universe multiverse",
    "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ lunar-backports main restricted universe multiverse",
    "deb http://security.ubuntu.com/ubuntu/ lunar-security main restricted universe multiverse",
    "# deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ lunar-proposed main restricted universe multiverse",
    "# # deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ lunar-proposed main restricted universe multiverse"
]

# Define the path to the sources.list file
sources_list_path = "/etc/apt/sources.list"

# Write the new mirror URLs to sources.list
with open(sources_list_path, "w") as file:
    file.write("\n".join(new_mirror_urls))

print("Ubuntu镜像源已成功替换为清华大学镜像源！")
