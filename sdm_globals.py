#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# Global variables for my custom SDM workflow for making RaspberryPi OS Images
# for clustering purposes.
########################################################################################################################
import os.path as path
from datetime import date
import update_os
#----------------------------------------------------------------------------------------------------------------------#

TODAY = date.today()
TODAYS_DATE = TODAY.strftime("%Y-%m-%d")

ADMIN_NAME          = 'aherlan'
ADMIN_PASS          = 'Tphtl4e!1mhaIwgc.'

USER_NAME           = 'orbitrix'
USER_PASS           = 'Tphtl4e!1mhaIwgc.'

WORKING_DIR         = '/home/aherlan/sdm-configs/'
SD_CARD_HANDLE      = '/dev/sda'

PLATFORM            = 'rp5-servers'
PLATFORM_PATH       = path.join(WORKING_DIR, PLATFORM)

KEYFILES_DIR        = 'keyfiles'
KEYFILES_PATH       = path.join(WORKING_DIR, KEYFILES_DIR)

FIRST_PIBOOT_DIR    = '1piboot'
FIRST_PIBOOT_PATH   = path.join(WORKING_DIR, FIRST_PIBOOT_DIR)

NMCONFIG_DIR        = 'nmconfig'
NMCONFIG_PATH       = path.join(WORKING_DIR, NMCONFIG_DIR)

OS_IMG_DIR          = 'os-images'
OS_IMG_PATH         = path.join(WORKING_DIR, OS_IMG_DIR)
IMG_FILETYPE        = '.img'

CONFIG_FILE_TYPE    = '.conf'
APPS_FILE_NAME      = 'apps' + CONFIG_FILE_TYPE
APPS_FILE_PATH      = path.join(PLATFORM_PATH, APPS_FILE_NAME)
APPS2_FILE_NAME     = 'apps-external' + CONFIG_FILE_TYPE
APPS2_FILE_PATH     = path.join(PLATFORM_PATH, APPS2_FILE_NAME)

USERS_FILE_NAME     = 'users.conf'
USERS_FILE_PATH     = path.join(PLATFORM_PATH, USERS_FILE_NAME)

CMDLINE_FILE_NAME   = 'cmdline.cmd'
CMDLINE_FILE_PATH   = path.join(PLATFORM_PATH, CMDLINE_FILE_NAME)

CONFIG_FILE_NAME    = 'config.txt'
CONFIG_FILE_PATH    = path.join(PLATFORM_PATH, CONFIG_FILE_NAME)

PLUGINS_FILE_NAME   = 'plugins.conf'
PLUGINS_FILE_PATH   = path.join(PLATFORM_PATH, PLUGINS_FILE_NAME)

BASE_IMG_PATH       = os.get_latest_image_path()
BASE_IMG_FILE_NAME  = os.get_latest_image_name()
BASE_IMG_FILE_NAME  = BASE_IMG_FILE_NAME.replace('.img','')
    

PLATFORM_DIR        = path.join(WORKING_DIR, PLATFORM)
WORKING_IMG_FILE    = BASE_IMG_FILE_NAME + '-' + PLATFORM + '-' + TODAYS_DATE + IMG_FILETYPE
WORKING_IMG_PATH    = path.join(PLATFORM_DIR, WORKING_IMG_FILE)
BOOT_SCRIPTS        = path.join(PLATFORM_DIR,"1piboot")
PLUGIN_LIST         = path.join(PLATFORM_DIR,"plugins.conf")
APPS_LIST           = path.join(PLATFORM_DIR,"apps.conf")

REMOTE_IMAGES_DIR   = 'https://downloads.raspberrypi.com/raspios_lite_arm64/images/'


########################################################################################################################
# Commandline decorations
########################################################################################################################
GREATINGS           = '''     __        __   _                               _    _
     \\ \\      / /__| | ___ ___  _ __ ___   ___     / \\  | | _____  __
      \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ \\` _ \\/ _ \\   / _ \\ | |/ _ \\ \\/ /
       \\ V  V /  __/ | (_| (_) | | | | | |  __/  / ___ \\| |  __/>  <
        \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___| /_/   \\_\\_|\\___/_/\\_\\
                                                                  '''+TODAYS_DATE
FAREWELL            = '''       ____                 _ _                     _    _           _ 
      / ___| ___   ___   __| | |__  _   _  ___     / \\  | | _____  _| |
     | |  _ / _ \\ / _ \\ / _` | '_ \\| | | |/ _ \\   / _ \\ | |/ _ \\ \\/ / |
     | |_| | (_) | (_) | (_| | |_) | |_| |  __/  / ___ \\| |  __/>  <|_|
      \\____|\\___/ \\___/ \\__,_|_.__/ \\__, |\\___| /_/   \\_\\_|\\___/_/\\_(_)
                                    |___/                              
                                                                  '''+TODAYS_DATE

HR_HEAD             = '\n'+('='*120)
HR_SPLIT            = ('-'*120)
HR_FOOT             = ('-'*120)+'\n'
########################################################################################################################