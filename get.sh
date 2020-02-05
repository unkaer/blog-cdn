#!/data/data/com.termux/files/usr/bin/bash

# 本文件地址https://cdn.jsdelivr.net/gh/unkaer/blog-cdn/get.sh
# 哈鱼Termux脚本
# curl -s https://cdn.jsdelivr.net/gh/unkaer/blog-cdn/get.sh -o get.sh && bash get.sh ph_r1J0HFOARUlydx0= 0 && rm -f get.sh

phone=$1
mode=$2
unamestr=`uname`
downurl=""
mkdir -p hashfish
cd hashfish
if [[ "$unamestr" == 'Linux' ]]; then
   echo "linux"
   downurl="http://cli.hashfish.net/linux.tar.gz"
elif [[ "$unamestr" == 'Darwin' ]]; then
   echo "osx"
   downurl="http://cli.hashfish.net/darwin.tar.gz"
fi

curl -o down.tar.gz $downurl
tar -xvzf down.tar.gz
rm down.tar.gz
chmod a+x hashfish
hashfish -g -p $phone -m $mode
hashfish
