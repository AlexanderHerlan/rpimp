#!/bin/bash
#
# Burn a bunch of SSDs/SD Cards from the same image
# Each will have a unique hostname 
#

print(SDM_SD_CARD_HANDLE)

# Change this to be the name of the device you want to burn to
odev = SDM_SD_CARD_HANDLE
# Change this to be the full path to the IMG you want to burn
img="/home/aherlan/sdm-configs/rp-server/2024-03-15-raspios-bookworm-arm64-lite.img"

# Change the host names to suit your needs. You'll need one SSD/SD Card
# for each of the hosts
#
for hn in rp-server-blue rp-server-green rp-server-red rp-server-white 
do
    echo "* Insert SSD/SD Card in $odev then press Enter to burn rp-server images"
    if askyn "Burn host '$hn' on $odev? [y/n]:" "y"
    then
        echo -ne "Burning custom settings for ${hn}...\n"
        sudo sdm --burn $odev \
                 --hostname $hn \
                 --plugin network:"netman=nm|noipv6|nmconn=/home/aherlan/sdm-configs/rp-server/${hn}/NetworkManager/system-connections/DesertDigital_5G.nmconnection,/home/aherlan/sdm-configs/rp-server/${hn}/NetworkManager/system-connections/Wired_LAN.nmconnection" \
                 --plugin runatboot:"script=/home/aherlan/sdm-configs/rp-server/${hn}/initial_local_setup.sh" \
                 --expand-root $img
    fi
    umount /dev/sda
done
