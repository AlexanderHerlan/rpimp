#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# Command Line Script for keeping my local Raspberry Pi OS images up to date.
########################################################################################################################
# Dependency declarations
import os
import sys
import sdm_globals as gv
import update_os as rpos
import argparse
import requests
import lzma
from bs4 import BeautifulSoup
#----------------------------------------------------------------------------------------------------------------------#
# Command line argument configuration

parser = argparse.ArgumentParser()
parser.add_argument("-l","--local", action="store_true", help="return latest local image.")
parser.add_argument("-r","--remote", action="store_true", help="return latest remote image.")
parser.add_argument("-ll","--list_local", action="store_true", help="list all local images.")
parser.add_argument("-lr","--list_remote", action="store_true", help="list all remote image.")
parser.add_argument("-u","--update", action="store_true", help="download latest OS image.")
args = parser.parse_args()

#----------------------------------------------------------------------------------------------------------------------#
# Function Definitions

# Get list of files and directories from an HTTPS directory
def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

    return parent


# List all the images currently stored locally
def list_local_images():
    filelist = []
    for (dirpath, dirnames, filenames) in os.walk(gv.OS_IMG_PATH):
        filelist = sorted(filenames)

    # Add the full path back to each filename in the OS directory
    filelist = [f"{gv.OS_IMG_PATH}/{s}" for s in filelist]

    return filelist


# List all the images available remotely
def list_remote_images():
    image_dirs = get_url_paths(gv.REMOTE_IMAGES_DIR)
    filelist = []
    
    del image_dirs[:5] # Get rid of unneccasary urls from HTML
    for image_url in image_dirs:
        current_path = get_url_paths(image_url, ext='.img.xz', params={})
        #del current_path[:5] # Get rid of unneccasary urls from HTML
        if current_path != []:
            filelist.append(current_path[0])

    return filelist


# Return the path to the latest local OS image
def get_latest_image_path():
    latest_images = list_local_images()
    if len(latest_images) > 0:
        return os.path.join(gv.OS_IMG_PATH, latest_images[-1])
    else:
        return None


# Return the name of the latest local OS image
def get_latest_image_name():
    latest_images = list_local_images()
    if len(latest_images) > 0:
        return os.path.join(gv.OS_IMG_PATH, latest_images[-1]).split('/')[-1]
    else:
        return os.path.join(gv.OS_IMG_PATH, "no_image.img")


# Return the name of the latest remote OS image
def get_latest_remote_image_name():
    return list_local_images()[-1].split('/')[-1]


# Return the URL to the latest remote OS image
def get_latest_remote_image():
    return list_remote_images()[-1]


# Check for the latest RaspberryPi OS image and download and extract if available
def update_os_images():
    print("Checking for updates to RaspberryPi Lite OS images...")
    latest_local_image = list_local_images()
    if len(latest_local_image) > 0:
        latest_local_image = latest_local_image[-1]
        latest_local_image_name = latest_local_image.split('/')[-1]
    else:
        latest_local_image_name = None
    
    latest_remote_image = list_remote_images()[-1]
    latest_remote_image_name = latest_remote_image.split('/')[-1].replace('.xz', '')
    latest_remote_archive = latest_remote_image_name + '.xz'
    archive_destination = os.path.join(gv.OS_IMG_PATH, latest_remote_archive)
    image_destination = os.path.join(gv.OS_IMG_PATH, latest_remote_image_name)

    if(latest_local_image_name == latest_remote_image_name):
        print("Your RaspberryPi OS Lite images are up to date.")
        print("Current image: " + latest_local_image)
    else:
        print("New image available: " + latest_remote_archive)
        print("Downloading... ")

        # Download the .xz file from the remote server
        response = requests.get(latest_remote_image, stream=True)
        with open(archive_destination,'wb') as output:
            output.write(response.content)

        print("Download complete.")
        print("Extracting... ")

        # Extract the .xz file to produce the final .img file
        with lzma.open(archive_destination) as f, open(image_destination, 'wb') as fout:
            file_content = f.read()
            fout.write(file_content)
        
        # Delete the original .xz file now that we have the .img file
        os.remove(archive_destination)

        print("Extraction Complete.")
        print("Your RaspberryPi OS Lite images are up to date.")
        print("Current image: " + list_local_images()[-1])


########################################################################################################################
# Main entry Point for application
if __name__ == '__main__':
    # Flag -l --local
    # Returns current latest OS image file path
    if args.local == True:
        print(get_latest_image_path())


    # Flag -r --remote 
    # Returns current latest OS image remote URL
    if args.remote == True:
        print(get_latest_remote_image())


    # Flag -ll --list_local
    # Lists all current local OS images
    if args.list_local == True:
        print(list_local_images())


    # Flag -lr --list_remote
    # Lists all current remote OS images
    if args.list_remote == True:
        print(list_remote_images())


    # Flag -u --update
    # Checks for updates to OS images
    if args.update == True:
        update_os_images()

    # If no command line arguments were provided, guide the user to the help menu
    if len(sys.argv)==1:
        print("No arguments provided. Use the -h or --help flag to see propper usage.")
