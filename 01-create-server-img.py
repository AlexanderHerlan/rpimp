#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# Routine to begin customizing a raspberrypi os .img file
# for a custom cluster environment
########################################################################################################################
import os
import subprocess
import shutil
import rpimp_globals as gv
import update_os as rpos

########################################################################################################################
# Main entry Point for application
if __name__ == '__main__':
    print(gv.HR_HEAD)
    print(gv.GREATINGS)
    print(gv.HR_SPLIT)
    print("Working In Directory: " + gv.WORKING_DIR)
    print(gv.HR_SPLIT)

    # Make sure we have the latest RaspberryPi Lite OS image
    rpos.update_os_images()

    # Get the path to the latest clean original RaspberryPi Lite OS image
    gv.BASE_IMG_PATH = rpos.get_latest_image_path()

    print(gv.HR_SPLIT)
    print("Current Settings: ")
    print("PLATFORM: " + gv.PLATFORM)
    print("BASE_IMG_FILE_NAME: " + gv.BASE_IMG_FILE_NAME)
    print("BASE_IMG_FILE: " + gv.BASE_IMG_FILE_NAME)
    print("BASE_IMG_PATH: " + gv.BASE_IMG_PATH)
    print("WORKING_DIR: " + gv.WORKING_DIR)
    print("WORKING_IMG_FILE: " + gv.WORKING_IMG_FILE)
    print("WORKING_IMG_PATH: " + gv.WORKING_IMG_PATH)
    print("BOOT_SCRIPTS: " + gv.BOOT_SCRIPTS)
    print("PLUGIN_LIST: " + gv.PLUGIN_LIST)
    print("APPS_LIST: " + gv.APPS_LIST)

    print(gv.HR_HEAD)
    print('Running SDM Command for headless ' + gv.PLATFORM + ' image creation')
    print(gv.HR_SPLIT)
    print('Working image path: \n' + gv.OS_IMG_PATH + '\n')
    print('Using OS base image: \n' + gv.BASE_IMG_FILE_NAME + '\n')
    if os.path.exists(gv.WORKING_IMG_PATH):
        print("Removing existing image: \n" + gv.WORKING_IMG_PATH)
        os.remove(gv.WORKING_IMG_PATH)
    print("Generating fresh image file to base our custom image on...")
    print(gv.BASE_IMG_PATH)
    print(gv.WORKING_IMG_PATH)

    shutil.copyfile(gv.BASE_IMG_PATH, gv.WORKING_IMG_PATH)

    print(gv.HR_HEAD)
    print("Now working on: \n" + gv.WORKING_IMG_FILE)
    print("In the directory: \n" + gv.WORKING_DIR)

    COMMAND1 = "sdm " \
              "--customize " + gv.WORKING_IMG_PATH + " " \
              "--logwidth 132 " \
              "--extend --xmb 4048 " \
              "--bootscripts " + gv.BOOT_SCRIPTS + " " \
              "--plugin @" + gv.PLUGIN_LIST + " " \
              "--plugin apps:apps=@" + gv.APPS_LIST + "|name=myapps " \
              "--reboot 20"
    
    # Show the final SDM command that we will be running
    print(gv.HR_SPLIT)
    print("Executing the fllowing SDM command: ")
    print("\n\n" + COMMAND1 + "\n\n")

    # Execute the main SDM image creation command with sudo
    cmd1 = subprocess.Popen(['echo', gv.ADMIN_PASS], stdout=subprocess.PIPE)
    cmd2 = subprocess.Popen(['sudo', '-S'] + COMMAND1.split(), stdin=cmd1.stdout, stdout=subprocess.PIPE)
    output1 = cmd2.stdout.read().decode()
    print(output1)

    print(gv.HR_SPLIT)

    # Execute the sdm shrink command on the final image to save disk space
    # COMMAND2 = "sdm --shrink " + gv.WORKING_IMG_PATH
    # cmd3 = subprocess.Popen(['echo', gv.ADMIN_PASS],stdout=subprocess.PIPE)
    # cmd4 = subprocess.Popen(['sudo', '-S'] + COMMAND2.split(), stdin=cmd3.stdout, stdout=subprocess.PIPE)
    # output2 = cmd4.stdout.read().decode()
    # print(output2)
    
    # Final Farewell
    print(gv.HR_SPLIT)
    print(gv.FAREWELL)
    print(gv.HR_SPLIT)
    print('Done.')