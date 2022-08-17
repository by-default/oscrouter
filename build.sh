#!/usr/bin/env bash

mkdir -p build/usr/bin
mkdir -p build/etc/oscrouter
mkdir -p build/etc/systemd/system
cp oscrouter.py build/usr/bin/oscrouter
cp config.yaml.example build/etc/oscrouter
cp oscrouter.service build/etc/systemd/system
chmod +x build/usr/bin/oscrouter
