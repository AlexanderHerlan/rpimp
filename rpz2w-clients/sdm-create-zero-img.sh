#!/bin/bash
echo 'Running SDM Command for headless rp-zero image creation'
echo 'Deleting old rp-zero image...'
rm /home/aherlan/sdm-configs/rp-zero/2024-03-15-raspios-bookworm-arm64-lite-zero-2-w.img
echo 'Copying fresh rp-zero image...'
cp /home/aherlan/sdm-configs/2024-03-15-raspios-bookworm-arm64-lite.img /home/aherlan/sdm-configs/rp-zero/2024-03-15-raspios-bookworm-arm64-lite-zero-2-w.img
echo 'Entering SDM rp-zero image modification routine...'
sudo sdm \
     --logwidth 132 \
     --extend --xmb 2048 \
     --customize /home/aherlan/sdm-configs/rp-zero/2024-03-15-raspios-bookworm-arm64-lite.img \
     --1piboot /home/aherlan/sdm-configs/rp-zero/1piboot/1piboot.conf \
     --bootscripts /home/aherlan/sdm-configs/rp-zero/1piboot/ \
     --plugin @/home/aherlan/sdm-configs/rp-zero/plugins.conf \
     --plugin apps:"apps=@/home/aherlan/sdm-configs/rp-zero/apps.conf|name=myzeroapps" \
     --reboot 20
