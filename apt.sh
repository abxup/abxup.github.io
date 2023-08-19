############换国内清华大学源
#!/bin/bash

# 下载sources.list文件
wget https://abxup.github.io/ubuntu/sources.list

# 做个备份
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

# 替换sources.list
sudo cp sources.list /etc/apt/sources.list

# 删除下载的临时文件
rm sources.list

apt update
