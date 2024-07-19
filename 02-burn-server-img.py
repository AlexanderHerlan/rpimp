#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# Burn a bunch of SSDs/SD Cards from the same image
# Each will have a unique hostname as well as any other customizations
# Required on a per-system basis
########################################################################################################################
import os
import subprocess
import shutil
import sys
import rpimp_globals as gv
import update_os as rpos
#----------------------------------------------------------------------------------------------------------------------#

print(gv.HR_HEAD)
print("Attempting to burn image: " + gv.BASE_IMG_PATH)
print("To device: " + gv.SD_CARD_HANDLE)
print(gv.BASE_IMG_PATH)

server_list = ['rp-server-blue', 'rp-server-green', 'rp-server-red', 'rp-server-white']

image_to_burn = ""

print("Which server image would you like to burn?: ")

i = 1
for server in server_list:
    print(str(i) + ") " + server)
    i = i + 1

image_to_burn = input("Select server by number: ")

server_host_name = server_list[int(image_to_burn)-1]
print(server_host_name)

burn_directory = gv.WORKING_DIR + "rp5-servers/" + server_host_name + "/"
burn_file = burn_directory + server_host_name + "-" + gv.TODAYS_DATE + ".img"
nm_path = "/home/aherlan/rpimp/rp5-servers/" + server_host_name + "/NetworkManager/system-connections/"
config_path = "/home/aherlan/rpimp/rp5-servers/config.txt"
cmdline_path = "/home/aherlan/rpimp/rp5-servers/" + server_host_name + "/cmdline.txt"
user_path = "/home/aherlan/rpimp/rp5-servers/users.conf"

if (os.path.isfile(burn_file)):
    os.remove(burn_file)
    
# COMMAND1 =  "sdm " \
#             "--burn " + gv.SD_CARD_HANDLE + " " \
#             "--hostname " + server_host_name + " " \
#             "--plugin network:\"netman=nm|noipv6|nmconn=/home/aherlan/rpimp/rp-server/" + server_host_name + "/NetworkManager/system-connections/DesertDigital_5G.nmconnection,/home/aherlan/rpimp/rp-server/" + server_host_name + "/NetworkManager/system-connections/Wired-connection-eth0.nmconnection\" " \
#             "--plugin runatboot:\"script=/home/aherlan/rpimp/rp-server/" + server_host_name + "/initial_local_setup.sh\" " \
#             "--expand-root " + gv.WORKING_IMG_PATH + " " \

# COMMAND1 =  "sdm " \
#             "--burnfile " + gv.WORKING_IMG_PATH + " " \
#             "--host " + server_host_name + " " \
#             "--plugin network:\"netman=nm|noipv6|nmconn=/home/aherlan/rpimp/rp-server/" + server_host_name + "/NetworkManager/system-connections/DesertDigital_5G.nmconnection,/home/aherlan/rpimp/rp-server/" + server_host_name + "/NetworkManager/system-connections/Wired-connection-eth0.nmconnection\" " \
#             "--plugin runatboot:\"script=/home/aherlan/rpimp/rp-server/" + server_host_name + "/initial_local_setup.sh\" " \
#             "--expand-root " + "~/rpimp/rp5-servers/" + server_host_name + "/" + server_host_name + ".img "



# COMMAND1 = "sudo sdm " \
#            "--burnfile " + burn_file + " " \
#            "--plugin network:netman=nm|noipv6|nmconn=" + nm_path + "DesertDigital_5G.nmconnection," + nm_path + "Wired-connection-eth0.nmconnection|wifissid=DesertDigital_5G|wifipassword=LetMeIn69!|wificountry=US " \
#            "--plugin runatboot:script=/home/aherlan/rpimp/rp5-servers/" + server_host_name + "/initial_local_setup.sh " \
#            "--plugin copyfile:from="+config_path+"|to=/boot/firmware/|chown=aherlan:rp-server-group|chmod=744 " \
#            "--host " + server_host_name + " " + gv.WORKING_IMG_PATH + " " \
#            "--plugin copyfile:from="+cmdline_path+"|to=/boot/firmware/|chown=aherlan:rp-server-group|chmod=744 "


COMMAND1 = "sudo sdm " \
           "--burnfile " + burn_file + " " \
           "--host " + server_host_name + " " + gv.WORKING_IMG_PATH + " " \
           "--plugin @" + user_path + " " \
           "--plugin network:netman=nm|noipv6|nmconn=" + nm_path + "DesertDigital_5G.nmconnection," + nm_path + "Wired-connection-eth0.nmconnection|wifissid=DesertDigital_5G|wifipassword=LetMeIn69!|wificountry=US " \
           "--plugin copyfile:from="+config_path+"|to=/boot/firmware/|chown=aherlan:rp-server-group|chmod=744 " \
           "--plugin runatboot:script=/home/aherlan/rpimp/rp5-servers/" + server_host_name + "/initial_local_setup.sh " \
#           "--plugin copyfile:from="+cmdline_path+"|to=/boot/firmware/|chown=aherlan:rp-server-group|chmod=744 "


# cmd1 = subprocess.Popen(['echo', gv.ADMIN_PASS],stdout=subprocess.PIPE)
# cmd2 = subprocess.Popen(['sudo', '-S', 'fdisk', '-l'], stdin=cmd1.stdout, stdout=subprocess.PIPE)
# fdisk_output = cmd2.stdout.read().decode()
# print(fdisk_output)


# Show the final SDM command that we will be running
print(gv.HR_SPLIT)
print("Executing the fllowing SDM burn command: ")
print("\n\n" + COMMAND1 + "\n\n")

# Execute the image burn command
cmd1 = subprocess.Popen(['echo', gv.ADMIN_PASS], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(['sudo', '-S'] + COMMAND1.split(), stdin=cmd1.stdout, stdout=subprocess.PIPE)
output1 = cmd2.stdout.read().decode()
print(output1)

# # Unmount the SD Card
# COMMAND2 = "umount " + gv.SD_CARD_HANDLE
# cmd3 = subprocess.Popen(['echo', gv.ADMIN_PASS],stdout=subprocess.PIPE)
# cmd4 = subprocess.Popen(['sudo', '-S'] + COMMAND2.split(), stdin=cmd3.stdout, stdout=subprocess.PIPE)
# output2 = cmd4.stdout.read().decode()
# print(output2)

