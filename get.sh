#!/data/data/com.termux/files/usr/bin/bash

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
./hashfish -g -p $phone -m $mode
./hashfish
