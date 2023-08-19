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

# Read the current content of sources.list
with open(sources_list_path, "r") as file:
    current_content = file.readlines()

# Find the starting and ending indexes of the block to be replaced
start_index = -1
end_index = -1
for i, line in enumerate(current_content):
    if line.startswith("# deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/"):
        start_index = i
    if line.startswith("# # deb-src http://mirrors.tuna.tsinghua.edu.cn/ubuntu/"):
        end_index = i
        break

# Replace the block with new mirror URLs
if start_index != -1 and end_index != -1:
    new_content = current_content[:start_index] + new_mirror_urls + current_content[end_index+1:]
    
    # Write the updated content back to sources.list
    with open(sources_list_path, "w") as file:
        file.writelines("\n".join(new_content))
    
    print("Ubuntu镜像源已成功替换为清华大学镜像源！")
else:
    print("未找到要替换的镜像源块。请检查源列表文件。")
