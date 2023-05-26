#!/bin/bash
# This script is useful for updating python version on Ubuntu 18.04 .
# Because my default python version is v3.6.9 on my Ubuntu 18.04
# refer to https://tecadmin.net/how-to-install-python-3-9-on-ubuntu-18-04/
# refer to https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-9-0-on-ubuntu-18-04-lts/
sudo apt -y update
sudo apt-get -y install software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt -y update
sudo apt-get -y install python3.9
sudo apt-get -y install python3-pip

sudo update-alternatives --list python3

sudo update-alternatives --remove-all python3
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 0
sudo update-alternatives --config python3

sudo update-alternatives --list python3

# to fix issue
# ImportError: Cannot import name 'sysconfig' from 'distutils'
sudo apt-get -y install python3.9-distutils

#
pip3 install --upgrade setuptools
pip3 install --upgrade pip
pip3 install --upgrade distlib
