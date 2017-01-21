#!/bin/bash

sudo apt-get install -y git emacs python-dev build-essential python-pip python-setuptools python-gobject libbluetooth-dev bluez python-bluez ofono dbus-x11 libdbus-glib-1-dev
sudo apt-get install -y autoconf libtool intltool libsndfile1-dev libcap-dev libsystemd-daemon0 libdbus-1-dev libspeex-dev libspeexdsp-dev libudev-dev libsbc-dev libbluetooth-dev libasound2-dev libjson-c-dev
sudo apt-get install -y pulseaudio
sudo apt-get install -y alsa-base alsa-utils bluez-alsa
sudo pip install pyalsaaudio
git clone https://github.com/littlecraft/phony.git
sudo python setup.py install
