#!/bin/bash
echo "Expanding root file system of the rp-zero to fit the entire drive's space"
raspi-config --expand-rootfs
echo "... file system expanded."
