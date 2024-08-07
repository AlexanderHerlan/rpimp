#!/bin/bash
#
# Burn a bunch of SSDs/SD Cards from the same image
# Each will have a unique hostname 
#

function askyn() {
    #
    # $1: Prompt string
    # $2: default answer: "y" or "n"
    #
    local ans
    echo -n "$1 " ; read -n 1 ans
    [ "$ans" == "" ] && ans="$2" || echo ""
    case "${ans,,}" in
        y*) return 0 ;;
        *) return 1 ;;
    esac
}

# Change this to be the name of the device you want to burn to
odev="/dev/sda"
# Change this to be the full path to the IMG you want to burn
img="/home/aherlan/sdm-configs/rp-zero/2024-03-15-raspios-bookworm-arm64-lite.img"

# Change the host names to suit your needs. You'll need one SSD/SD Card
# for each of the hosts
#
for hn in rp-zero-blue rp-zero-green rp-zero-red rp-zero-white 
do
    echo "* Insert SSD/SD Card in $odev then press Enter to burn rp-zero images"
    if askyn "Burn host '$hn' on $odev? [y/n]:" "y"
    then
        echo -ne "Burning custom settings for ${hn}...\n"
        sudo sdm --burn $odev \
                 --hostname $hn \
                 --plugin network:"netman=nm|noipv6|nmconn=/home/aherlan/sdm-configs/rp-zero/${hn}/NetworkManager/system-connections/DesertDigital_5G.nmconnection,/home/aherlan/sdm-configs/rp-zero/${hn}/NetworkManager/system-connections/Wired_LAN.nmconnection" \
                 --plugin runatboot:"script=/home/aherlan/sdm-configs/rp-zero/${hn}/initial_local_setup.sh" \
                 --expand-root $img
    fi
    umount /dev/sda
done
