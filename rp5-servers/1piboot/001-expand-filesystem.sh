#!/bin/bash

echo "Expanding file system of the rp-server to fit the entire drive's space..."
raspi-config --expand-rootfs
echo "... file system expanded."
