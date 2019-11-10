# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
from deployer.deploy import Deploy

host = "rpi"
# host="172.28.240.122"
if __name__ == '__main__':
    Deploy(local_dir="/ICESX/workspace_rpi/raspberry-weigend",host=host,user="pi",remote_dir="/home/pi",
           password='raspberry').zip(excludes={"doc",".git"}).scp_file().ssh_unzip().clean()
