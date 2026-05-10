import os
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "./config", "uix_kit"))

import json
import random
import socket
import time
import subprocess
import platform
import datetime
import nmap
#from scrcpy_utils import banner
#from scrcpy_utils import color
import adbutils

#from terminaltables import DoubleTable
#from tabulate import tabulate


#-------------------------------------------------------------------------#

################################ Main Menu Section ##############################

#-------------------------------------------------------------------------#
class color:

    RED = "\033[91m"
    GREEN = "\033[92m"
    ORANGE = '\033[33m'
    YELLOW = "\033[93m"
    # BLUE = '\033[94m'
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


    color_list = [RED, GREEN, YELLOW, PURPLE, CYAN, WHITE]



class banner:



    main_menu = f"""

    {color.ORANGE}[Menu]

    {color.WHITE}1. scan            -{color.GREEN} Scan Network for Devices             
    {color.WHITE}2. connect         -{color.GREEN} Connect a Device                             
    {color.WHITE}3. disconnect      -{color.GREEN} Disconnect All Devices           
    {color.WHITE}4. devices         -{color.GREEN} List Connected Devices
    {color.WHITE}5. xdroid          -{color.GREEN} Android adb command center{color.WHITE}


    {color.ORANGE}Usage:{color.WHITE} enter the number or type the name on the menu display
    {color.ORANGE}example:{color.WHITE} enter 1 or type scan - to scan devices on the network                                    
    """

    android_adb_command_menu = f"""

    {color.ORANGE}[Menu]

    {color.WHITE}1. scrcpy_noaudio  -{color.GREEN} Mirror the device using screencopy - no audio 
    {color.WHITE}2. scrcpy          -{color.GREEN} Mirror the device using screencopy  
    {color.WHITE}3. screensr        -{color.GREEN} Screen Shot/Recorder
    {color.WHITE}4. camera          -{color.GREEN} Camera access
    {color.WHITE}5. syscom          -{color.GREEN} Android system Commands {color.WHITE}          


    {color.ORANGE}Usage:{color.WHITE} enter the number or type the name on the menu display
    {color.ORANGE}example:{color.WHITE} enter 1 or type scrcpy - to use screencopy                                    
    """

    screensr_menu = f"""

    {color.ORANGE}[Menu]

    {color.WHITE}1. screenshot      -{color.GREEN} Screen Shot menu
    {color.WHITE}2. recordscreen    -{color.GREEN} Screen Recorder Menu{color.WHITE}


    {color.ORANGE}Usage:{color.WHITE} enter the number or type the name on the menu display
    {color.ORANGE}example:{color.WHITE} enter 1 or type screenshot - for screenshot menu                                    
    """ 
    audio_menu = f"""
    {color.ORANGE}[Menu]

    {color.WHITE}1. r-audio-m       -{color.GREEN} Record Audio{color.YELLOW}(Mic)
    {color.WHITE}2. r-audio-d       -{color.GREEN} Record Audio{color.YELLOW}(Device)
    {color.WHITE}3. s-audio-m       -{color.GREEN} Sream Audio{color.YELLOW}(Mic)
    {color.WHITE}4. s-audio-d       -{color.GREEN} Sream Audio{color.YELLOW}(Device){color.WHITE}


    {color.ORANGE}Usage:{color.WHITE} enter the number or type the name on the menu display
    {color.ORANGE}example:{color.WHITE} enter 3 or type s-audio-m - to stream audio via mic                                    
    """ 

    sys_action_menu = f"""
    {color.ORANGE}[Menu]

    {color.WHITE}1. shell           -{color.GREEN} android shell                  
    {color.WHITE}2. lock            -{color.GREEN} Lock device                               
    {color.WHITE}3. unlock          -{color.GREEN} Unlock Devices                   
    {color.WHITE}4. rebootmenu      -{color.GREEN} Reboot Menu                
    {color.WHITE}5. device-info     -{color.GREEN} Device info 
    {color.WHITE}6. battery-info    -{color.GREEN} Battery info
    {color.WHITE}7. power-off       -{color.GREEN} Power off {color.WHITE}


    {color.ORANGE}Usage:{color.WHITE} enter the number or type the name on the menu display
    {color.ORANGE}example:{color.WHITE} enter 2 or type lock - to lock the device/emulator                                   
    """ 

    reboot_menu = f"""
    {color.ORANGE}[Menu]

    {color.WHITE}1. s-reboot        -{color.GREEN} System reboot                  
    {color.WHITE}2. a-reboot        -{color.GREEN} Advanced reboot{color.WHITE}                              
    """ 
    android_screenshot_menu = f"""
    {color.ORANGE}[Menu]

    {color.WHITE}1. s-shot          -{color.GREEN} Normal Screen shot                               
    {color.WHITE}2. anon-s-shot     -{color.GREEN} Anonymous screenshot


    {color.ORANGE}Usage:{color.WHITE} enter the number or type the name on the menu display
    {color.ORANGE}example:{color.WHITE} enter 1 or type s-shot - to take screenshot                                     
    """

    android_screenrecord_menu = f"""
    {color.ORANGE}[Menu]

    {color.WHITE}1. s-record          -{color.GREEN} Normal screen recorder                              
    {color.WHITE}2. anon-s-record     -{color.GREEN} Anonymous screen recorder{color.WHITE}


    {color.ORANGE}Usage:{color.WHITE} enter the number or type the name on the menu display
    {color.ORANGE}example:{color.WHITE} enter 1 or type s-record - to record screen                                     
    """



    droid_toolkit = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                    █▀▄▀█ ▄▀█ █ █▄░█ ░ █▀▄▀█
                [X] █ ▀ █ █▀█ █ █░▀█ ▀ █ ▀ █enu

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Main Menu    >>>>                                    █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
    android_adb_command = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                    █▀ █▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▄
                [X] █▄ █▄█ █ ▀ █ █▀█ █░▀█ █▄▀ Center

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |ADB Command Center    >>>>                           █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """


    android_reboot = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                        █▀ ░ ▄▀█ ░ █▀█
                [X]     ▄█ ▀ █▀█ ▀ █▀▄

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |System/Advanced Reboot    >>>>                       █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """



    android_connect = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                        █▀ █▀█ █▄░█ █▄░█
                [X]     █▄ █▄█ █░▀█ █░▀█ect

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |ADB Wireless Connect    >>>>                         █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """

    android_devlist = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                    █▀▄░░ ░ █░ █ █▀ ▀█▀
                [X] █▄▀ev ▀ █▄ █ ▄█ ░█░

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Connected USB/Wireless Device List    >>>>           █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """


    bannerx = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Metasploit Exploitation    >>>>                      █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m 
    """


    android_scrcpy = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


            █▀ █▀ █▀█ █▀ █▀█ █ █
            ▄█ █▄ █▀▄ █▄ █▀▀ █▀
    """

    android_sys = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                        █▀ █ █ █▀
                [X]     ▄█ █▀  ▄█tem

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |ADB System Commands    >>>>                          █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
    android_nav = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                        █▄░█ ▄▀█ █  █
                        █░▀█ █▀█ ▀▄▀ igation

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Scrcpy ADB Navigation    >>>>                        █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
    android_screensr = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                        █▀ █▀ █▀█ ░ █▀ ░ █▀█
                [X]     ▄█ █▄ █▀▄ ▀ ▄█ ▀ █▀▄


    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |ADB Screen Shot/Record    >>>>                       █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
    android_screenshot = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                        █▀ █▀ █▀█ ░ █▀
                [X]     ▄█ █▄ █▀▄ ▀ ▄█hot

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Screen Shot    >>>>                                  █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
    android_screenrecorder = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                        █▀ █▀ █▀█ ░ █▀█
                [X]     ▄█ █▄ █▀▄ ▀ █▀▄ecorder

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Screen Recorder    >>>>                              █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
    android_audio_kit = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                    ▄▀█ █ █ █▀▄ █ █▀█
            [X]     █▀█ █▄█ █▄▀ █ █▄█ Kit

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Audio Recorder    >>>>                               █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
    android_audio_recorder = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                ▄▀█ █ █ █▀▄ █ █▀█ ░ █▀█
            [X] █▀█ █▄█ █▄▀ █ █▄█ ▀ █▀▄ecorder

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Audio Recorder    >>>>                               █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
    android_audio_stream = f"""

    ▄▀█ █▄░█ █▀▄ █▀█ █▀█ █ █▀▄    
    █▀█ █░▀█ █▄▀ █▀▄ █▄█ █ █▄▀ \033[33m</ToolKit >


                ▄▀█ █ █ █▀▄ █ █▀█ ░ █▀
            [X] █▀█ █▄█ █▄▀ █ █▄█ ▀ ▄█tream

    ┌══════════════════════════════════════════════════════════┐
    █                                                          █
    █    |Audio Stream    >>>>                                 █
    █                                                          █
    └══════════════════════════════════════════════════════════┘

    \033[37m[X] Multipurpose Android PenTesting Toolkit  [X]
    \033[36m[✔] ADB x Msf \033[35m [✔] Version 1.0 [✔]
    \033[91m[!] Disclaimer [!]\033[33m For Educational Purpose only
    \033[97m     
    """
"""
Copyright © 2023 Mohd Azeem (github.com/AzeemIdrisi)
"""


def main():
    option = input(f"""    
    [{color.CYAN}99.{color.ORANGE} Clear screen                                      {color.CYAN}0.{color.ORANGE} Exit{color.WHITE}]
    {color.WHITE}[scan | connect | disconnect | devices | xdroid | clear | exit] \n
    {color.YELLOW}[Main Menu]{color.WHITE} Enter selection {color.GREEN}>>>{color.WHITE} """).lower()
    match option:
        case "0"|"exit":
            exit_phonesploit_pro()
            os.system(clear)
        case "99"|"clear"|"cls":
            clear_screen()
        case "1"|"scan":
            network_scan()
        case "2"|"connect":
            xconnect()
        case "3"|"disconnect":
            main_disconnect()
        case "4"|"devices":
            main_list_devices()
        case "5"|"xdroid":
            adb_command_center()

        case "terminal":
            terminal()
            display_main_menu()
        case "caja":
            caja()
            display_main_menu()
        case "banner":
            bannerfile()
            display_main_menu()
        case "adb_file":
            adbxcom()
            display_main_menu()
        case other:
            print(f"\n{color.RED}       [X] Invalid selection\n{color.YELLOW}       Please enter a valid option on menu above\n")
            time.sleep(3)
            display_main_menu()


#-------------------------------------------------------------------------#

################################ ToolKit Section ##############################

#-------------------------------------------------------------------------#

def start():

    try:
        
        os.mkdir("./config/media-files")

    except:
        pass

    # Checking OS
    global operating_system, opener
    operating_system = platform.system()
    if operating_system == "Windows":
        # Windows specific configuration
        windows_config()
    else:
        # macOS only
        if operating_system == "Darwin":
            opener = "open"

def windows_config():
    global clear, opener  # , move
    clear = "cls"
    opener = "start"

    # move = 'move'
# Clear function like always

def clear():
    windows = "cls"
    linux = "clear"
    if platform.system() == "Windows":
        os.system(windows)
    else:
        os.system(linux)
def caja():
    caja = "./"
    cajaopener = "caja"
    if platform.system() == "Linux":
        os.system(f"{cajaopener} {caja}")
def bannerfile():
    bannerdir = "./config/uix_kit/scrcpy_utils/banner.py"
    if platform.system() == "Linux":
        os.system(f"{opener} {bannerdir}")
def adbxcom():
    adbxcom = "adb_connect.py"
    if platform.system() == "Linux":
        os.system(f"{opener} {adbxcom}")

def terminal():
    adbxcom = "mate-terminal"
    if platform.system() == "Linux":
        os.system(adbxcom)

"""Displays banner and menu"""
def screensr_menu():
    """Displays banner and menu"""
    os.system(clear)
    print(droid_screensr_banner,banner.screensr_menu)
def droid_adb_command_menu():
    """Displays banner and menu"""
    os.system(clear)
    print(droid_adb_command,banner.android_adb_command_menu)

def droid_sys_menu():
    """Displays banner and menu"""
    os.system(clear)
    print(droid_sys_banner,banner.sys_action_menu)

def droid_screenshot_menu():
    os.system(clear)
    print(droid_screenshot_banner,banner.android_screenshot_menu)

def droid_screenrecorder_menu():
    os.system(clear)
    print(droid_screenrecorder_banner,banner.android_screenrecord_menu)

def droid_reboot_menu():
    """Displays banner and menu"""
    os.system(clear)
    print(droid_reboot_banner,banner.reboot_menu)

def display_main_menu():
    """Displays banner and menu"""
    os.system(clear)
    print(main_banner,banner.main_menu)


def clear_screen():
    """Clears the screen and display menu"""
    os.system(clear)
    display_main_menu()

def exit_phonesploit_pro():
    global run_phonesploit_pro
    run_phonesploit_pro = False
    print(f'\n{color.WHITE}[Info]{color.GREEN} Stopping MSF-ADB Server.....{color.WHITE}\n', end='')

#-------------------------------------------------------------------------#

####################### ADB Connection Section ############################

#-------------------------------------------------------------------------#

def xconnect():
    try:
        phone_ip = get_adb_android_ip("-d")
        start_debugging_server()
        if phone_ip is None:
            return
        connect_to_wireless(phone_ip)
    except:
        connect()

#------------------------ Auto IP Selection ------------------------------#

def check_if_ip(possible_ip: str) -> bool:
    os.system(clear)
    print(droid_connect_banner)
    
    ip_parts = possible_ip.split(".")
    try:
        [int(part) for part in ip_parts]
        if len(ip_parts) == 4:
            return True

    except:
        time.sleep(0.8)
        print(f"{color.CYAN}    [Info]{color.WHITE} Auto Connect >> {color.RED}Failed ! {color.WHITE}>> No USB Connection\n")
        time.sleep(1.2)
        print(f"{color.GREEN}    << Going User input mode ")
        time.sleep(2.4)

    return False


def get_adb_android_ip(connection_type_flag: str | None = None):
    """
    connection_type_flag is either -d for usb of -e for ip
    Not yet:
        or -s ip:port to specif port
    """

    ip_args = ["adb"]
    if connection_type_flag is not None:
        ip_args += [connection_type_flag]
    ip_args += ["shell", "ip", "route"]
    ret = subprocess.run(ip_args, capture_output=True)  # only uses usb
    if "device unauthorized" in ret.stderr.decode():
        print("try pairing the device first")
        return
    possible_ip = ret.stdout.decode().strip().split(" ")[-1]
    is_ip = check_if_ip(possible_ip)
    if is_ip == True:
        return possible_ip
    else:
        raise ValueError


def connect_to_wireless(ip: str, port: str | int = "5555"):
    os.system(clear)
    print(droid_connect_banner)
    port = str(port)
    if ip is None:
        return
    print(f"\n{color.CYAN}    [Info] {color.GREEN} Device Found >> {color.YELLOW}{ip}\n")
    os.system("adb kill-server > ./config/sys_logs/syslog.txt 2>&1&&adb start-server > ./config/sys_logs/syslog.txt 2>&1")
    print(f'{color.CYAN}    [Info] {color.YELLOW}Restarting adb server ......\n')
    time.sleep(0.8)
    print(f'{color.CYAN}    [Info]{color.ORANGE} Connecting.....\n{color.WHITE}')
    time.sleep(1.2)
    subprocess.run(
        ["adb", "connect", f"{ip}:{port}"],
        capture_output=True,
    )
    auto_con_devices = adbutils.adb.device_list()
    for d in auto_con_devices:
        auto_con_dev = d.serial
        if auto_con_dev.count(".") == 3:
            display_main_menu()
            print(f"{color.ORANGE}    [{color.GREEN}✔{color.ORANGE}] {color.WHITE} Connection Successfull\n")
            print(f'{color.CYAN}    [Info]{color.ORANGE} Connected to{color.WHITE} {ip}{color.ORANGE} on port{color.WHITE} {port}{color.WHITE}\n')
        else:
            os.system(clear)
            display_main_menu()
            print(f"{color.WHITE}    [{color.RED}X{color.WHITE}]{color.ORANGE} Connection Failed{color.WHITE}")
        

def start_debugging_server():
    try:
        subprocess.run(
            "adb -d tcpip 5555".split(" "),
            capture_output=True,
        )
    except subprocess.CalledProcessError as e:
        print(F"COMMAND FAILED, maybe try pairing?. Error: {e}")




#------------------------ User IP Selection ----------------------------------#


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def network_scan():
    network_scanner()
    os.system(clear)
    display_main_menu()
    with open('./config/json_files/net_devs.json', 'r') as dev_ips:
        data = json.load(dev_ips)
        print(f"{color.WHITE}    [{color.GREEN}+{color.WHITE}]{color.WHITE} Scanned Devices{color.WHITE}\n    -----------------------\n")
        try:
            for dev_key in data:
                for dev_addr in [data[dev_key]]:
                    if dev_addr == "0.0.0.0":
                        print(f"{color.WHITE}       [No Device Found]\n")
                    else:
                        raise ValueError
        except:
            for dev_key in data:
                for dev_addr in [data[dev_key]]:
                    print(f"    {color.WHITE}[{color.GREEN}{dev_key}{color.WHITE}]{color.WHITE}. {color.YELLOW}{dev_addr}")
            print("\n")


def scan_network():
    
    net_devs_ip = {}
    count = 0
    print(f"\n{color.CYAN}    [Info]{color.ORANGE} Scanning network ......{color.WHITE}\n")
    time.sleep(1.2)
    try:
        ip = get_ip_address()
        ip += "/24"
        scanner = nmap.PortScanner()
        scanner.scan(hosts=ip, arguments="-sn")
    
        for host in scanner.all_hosts():

            if scanner[host]["status"]["state"] == "up":

                try:
                    if len(scanner[host]["vendor"]) == 0:
                        socket.gethostbyaddr(host)[0]
                    else:
                        scanner[host]['vendor']
                        socket.gethostbyaddr(host)[0]
                except:
                    scanner[host]['vendor']
                count = count+1
                while True:
                    if count < 10:
                        net_devs_ip[count] = host
                        with open('./config/json_files/net_devs.json', 'w') as f:
                            json.dump(net_devs_ip, f, indent=count)
                    break
    except:

        net_devs_ip = {"0": "0.0.0.0"}
        with open('./config/json_files/net_devs.json', 'w') as f:
            json.dump(net_devs_ip, f)
        raise ConnectionError

    print("\n") 

def network_scanner():
    try:
        scan_network()
    except:
        time.sleep(1.2)
        print(f"\n{color.RED}       Network is unreachable \n")
        time.sleep(1.2)
        try:
            print(f"\n{color.YELLOW}        Retrying ......... \n")
            time.sleep(0.8)
            scan_network()

        except:
            time.sleep(1.2)
            print(f"\n{color.RED}       Network is unreachable \n")
            time.sleep(1.2)
   
            try:
                print(f"\n{color.YELLOW}        Retrying ......... \n")
                time.sleep(0.8)
                scan_network()
            except:
                time.sleep(1.2)
                print(f"\n{color.RED}       Network is unreachable \n")
                time.sleep(1.2)
                print(f"""
                    \n{color.ORANGE}    [Please Check your network connection before retrying]\n 
                    \n{color.GREEN}    << Going Back to Main Menu  \n
                    """)
                time.sleep(2.4)
                os.system(clear)
                
                display_main_menu()



def connect():

    network_scanner()
    os.system(clear)
    print(droid_connect_banner)
    with open('./config/json_files/net_devs.json', 'r') as dev_ips:
        data = json.load(dev_ips)
        try:
            
            for key in data:
                for ip in [data[key]]:
                    if ip == "0.0.0.0":
                        print(f"{color.WHITE}    [{color.GREEN}-{color.WHITE}]{color.WHITE} Scanned Devices{color.WHITE}\n    -----------------------\n")
                        print(f"{color.WHITE}       [No Device Found]\n")
                    else:
                        raise ValueError
        except:
            print(f"{color.WHITE}    [{color.GREEN}+{color.WHITE}]{color.WHITE} Scanned Devices{color.WHITE}\n    -----------------------\n")
            for key in data:
                for ip in [data[key]]:
                    print(f"    {color.WHITE}[{color.GREEN}{key}{color.WHITE}]{color.WHITE}. {color.YELLOW}{ip}")
            print("\n")
            ip_input=input(f"{color.YELLOW}    [IP-select]{color.WHITE} Enter selection {color.GREEN}>>>{color.WHITE} ").lower()
            match ip_input:
                case ip_input:
                    try:
                
                        os.system(clear)
                        print(droid_connect_banner)
                        
                        if data[ip_input].count(".") == 3:
                            print(f"{color.CYAN}    [Info]{color.GREEN} Selected Device >> {color.YELLOW}{data[ip_input]}\n")
                            os.system("adb kill-server > ./config/sys_logs/syslog.txt 2>&1&&adb start-server > ./config/sys_logs/syslog.txt 2>&1")
                            print(f'{color.CYAN}    [Info]{color.YELLOW} Restarting adb server ......\n')
                            time.sleep(0.8)
                            print(f'{color.CYAN}    [Info]{color.ORANGE} Connecting.....\n{color.WHITE}')
                            time.sleep(1.2)
                            subprocess.run(['adb', 'connect', data[ip_input] + ':5555'], capture_output=True)
                            con_devices = adbutils.adb.device_list()
                            if len(con_devices) != 0:
                                os.system(clear)
                                time.sleep(0.8)
                                display_main_menu()
                                print(f"\n{color.ORANGE}    [{color.GREEN}✔{color.ORANGE}] {color.WHITE} Connection Successfull\n")
                                print(f'{color.CYAN}    [Info]{color.ORANGE} Connected to{color.WHITE} {data[ip_input]}{color.ORANGE} on port{color.WHITE} 5555{color.WHITE}\n\n')
                            else:
                                os.system(clear)
                                display_main_menu()
                                print(f"{color.WHITE}    [{color.RED}X{color.WHITE}]{color.ORANGE} Connection Failed\n{color.WHITE}")  
                        else:
                            time.sleep(0.8)
                            display_main_menu()
                            print(f"\n{color.RED}     Invalid IP Address\n{color.GREEN}     << Going back to Main Menu{color.WHITE}")
                    except:
                        if ip_input == '':
                            time.sleep(0.8)
                            display_main_menu()
                            print(f"\n{color.ORANGE}    Null Input | No selection made\n{color.GREEN}     << Going back to Main Menu{color.WHITE}")
                        else:
                            time.sleep(0.8)
                            display_main_menu()
                            print(f"{color.WHITE}    [{color.ORANGE}X{color.WHITE}]{color.ORANGE}    Device IP Not Found\n{color.GREEN}     << Going back to Main Menu{color.WHITE}")


def list_devices():
    print(f'\n{color.CYAN}    [Info]{color.ORANGE} Scanning for connected devices.....{color.WHITE}')
    time.sleep(1.2)
    adb_device_scanner()

def main_list_devices():
    os.system(clear)
    print(droid_devlist_banner)
    print(f'\n{color.CYAN}    [Info]{color.ORANGE} Scanning for connected devices.....{color.WHITE}')
    time.sleep(1.2)
    os.system(clear)
    display_main_menu()
    adb_device_scanner()
    

def adb_device_scanner():

    con_devices_list = adbutils.adb.device_list()
    if len(con_devices_list) == 0:
        print(f"\n{color.WHITE}    [{color.GREEN}-{color.WHITE}]{color.WHITE} Connected Devices{color.WHITE}\n    -----------------------\n")
        print(f"{color.WHITE}       [No Device Found]\n")
    else:

        for d in con_devices_list:
            con_dev = d.serial
            net_device =f"""
    {color.YELLOW}Device            :{color.WHITE} {d.prop.device}
    {color.YELLOW}Serial ip:port    :{color.CYAN} {d.serial}
    {color.YELLOW}Device Model      :{color.WHITE} {d.prop.model}
    {color.YELLOW}Device Name       :{color.WHITE} {d.prop.name}

    """
            if con_dev.count(".") != 3:
                print(f"{color.WHITE}    [{color.GREEN}+{color.WHITE}]{color.ORANGE} ADB USB Connection{color.WHITE}\n    -----------------------")
                print(net_device)
            elif con_dev.count(".") == 3:
                print(f"\n{color.WHITE}    [{color.GREEN}+{color.WHITE}]{color.ORANGE} ADB WiFi Connection {color.WHITE}\n    -----------------------")
                print(net_device)

def disconnect():
    con_devices = adbutils.adb.device_list()    
    if len(con_devices) == 0:
        print(f"\n{color.WHITE}      [No Device Connected]\n")
    else:
        try:
            subprocess.run(["adb", "disconnect"], capture_output=True)
            print(f'\n{color.CYAN}    [Info]{color.YELLOW} Disconnecting ......\n')
            time.sleep(1.2)
            print(f"{color.CYAN}    [Info]{color.WHITE} All Devices/Emulators Disconnected\n")
        except:
            print(f'\n{color.CYAN}    [Info]{color.YELLOW}Error occured while trying to disconnect\n')


def main_disconnect():
    try:
        subprocess.run(["adb", "disconnect"], capture_output=True)
        os.system(clear)
        display_main_menu()
        print(f'{color.CYAN}    [Info]{color.YELLOW} Disconnecting ......\n')
        time.sleep(1.2)
        print(f"{color.CYAN}    [Info]{color.WHITE} All Devices/Emulators Disconnected\n")
    except:
        print(e)
        os.system(clear)
        display_main_menu()
        print(f'{color.CYAN}    [Info]{color.YELLOW}Error occured while trying to disconnect\n')  
#-------------------------------------------------------------------------#

####################### Android Control Center ############################

#-------------------------------------------------------------------------#

def adb_command_center():
    droid_adb_command_menu()
    while True:
        adb_com = input(f"""    
    [{color.CYAN}99.{color.ORANGE} Clear screen                           {color.CYAN}0.{color.ORANGE} Back{color.WHITE}]
    {color.WHITE}[scrcpy_noaudio | scrcpy | screensr | camera | syscom | clear | back] \n
    {color.YELLOW}[ADB command]{color.WHITE} Enter selection {color.GREEN}>>>{color.WHITE} """).lower()

        match adb_com:
            
            case "terminal":
                terminal()
                droid_adb_command_menu()
            case "caja":
                caja()
                droid_adb_command_menu()
            case "banner":
                bannerfile()
                droid_adb_command_menu()
            case "adb_file":
                adbxcom()
                droid_adb_command_menu()
            case "0"|"back"|"cd ..":
                display_main_menu()
                break
            case "99"|"clear":
                droid_adb_command_menu()
            case "1"|"scrcpy_noaudio":
                screencopy_noaudio()
            case "2"|"scrcpy":
                screencopy()
            case "3"|"screensr":
                screensr() 
            case "4"|"camera":
                pass
                droid_adb_command_menu()
                print(f"\n{color.YELLOW}    [X] This feature is Not available Yet !!\n")
            case "5"|"syscom":
                android_sys() 
            case "devices":
                droid_adb_command_menu()
                list_devices()
            case "disconnect":
                droid_adb_command_menu()
                disconnect()            
            case other:
                print(f"\n{color.RED}       [X] Invalid selection\n{color.YELLOW}       Please enter a valid option on menu above\n")
                time.sleep(3)
                droid_adb_command_menu()



#--------------------------------------------------------------------------#
#--------------------- Screen Copy Section --------------------------------#
#--------------------------------------------------------------------------#


def screencopy_noaudio():

    def screencopy_noaudiokit():
        os.system(clear)
        print(droid_scrcpy_banner)
        print(f'{color.CYAN}    [Info]{color.YELLOW} Starting scrcpy  No audio ......\n')
        time.sleep(0.5)
        os.system("scrcpy --no-audio")
        os.system(clear)
        time.sleep(0.8)
        print(droid_adb_command)
        print(banner.android_adb_command_menu)

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        print("\n")
        print(f"\n{color.WHITE}      [No Device Connected]\n")
        time.sleep(0.8)
        print(f"\n{color.WHITE}      Checking for connection ......\n")
        time.sleep(1.2)
        xconnect()
        time.sleep(1.2)
        con_devx = adbutils.adb.device_list()
        if len(con_devx) == 0:
            droid_adb_command_menu()
        else:
            screencopy_noaudiokit()
    else:
        screencopy_noaudiokit()

def screencopy():

    def screencopykit():
        os.system(clear)
        print(droid_scrcpy_banner)
        print(f'{color.CYAN}    [Info]{color.YELLOW} Starting scrcpy ......\n')
        time.sleep(0.5)
        os.system("scrcpy")
        os.system(clear)
        time.sleep(0.8)
        print(droid_adb_command)
        print(banner.android_adb_command_menu)

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        print("\n")
        print(f"\n{color.WHITE}      [No Device Connected]\n")
        time.sleep(0.8)
        print(f"\n{color.WHITE}      Checking for connection ......\n")
        time.sleep(1.2)
        xconnect()
        time.sleep(1.2)
        con_devx = adbutils.adb.device_list()
        if len(con_devx) == 0:
            droid_adb_command_menu()
        else:
            screencopykit()
    else:
        screencopykit()

#----------------------------------------------------------------------------#
#------------------- Multimedia Section -------------------------------------#
#----------------------------------------------------------------------------#


def screensr():
    screensr_menu()
    while True:
        multi_m_option = input(f"""    
    [{color.CYAN}99.{color.ORANGE} Clear screen                 {color.CYAN}0.{color.ORANGE} Back{color.WHITE}]
    {color.WHITE}[screenshot | recordscreen | clear | back] \n
    {color.YELLOW}[Screensr]{color.WHITE} Enter selection {color.GREEN}>>>{color.WHITE} """).lower()

        match multi_m_option:
            
            case "terminal":
                terminal()
                screensr_menu()
            case "caja":
                caja()
                screensr_menu()
            case "banner":
                bannerfile()
                screensr_menu()
            case "adb_file":
                adbxcom()
                screensr_menu()
            case "0"|"back"|"cd ..":
                droid_adb_command_menu()
                break
            case "99"|"clear":
                screensr_menu()
            case "1"|"screenshot":
                get_screenshot()
            case "2"|"recordscreen":
                screenrecorder()
            case "devices":
                screensr_menu()
                list_devices()
            case "disconnect":
                screensr_menu()
                disconnect()
            case other:
                print(f"\n{color.RED}       [X] Invalid selection\n{color.YELLOW}       Please enter a valid option on menu above\n")
                time.sleep(3)
                screensr_menu()


#-------------------------------- ScreenShot ---------------------------------------#

def get_screenshot():
    def screenshotkit():
        droid_screenshot_menu()
        while True:
            global screenshot_location
            # Getting a temporary file name to store time specific results
            screenshot_mode = input(f"""
    [{color.CYAN}99.{color.ORANGE} Clear screen            {color.CYAN}0.{color.ORANGE} Back{color.WHITE}]
    {color.WHITE}[s-shot | anon-s-shot | clear | back] \n
    {color.ORANGE}[Screen-shot-mode]{color.WHITE} Select Mode >>> """).lower()
            instant = datetime.datetime.now()
            file_name = f"screenshot-{instant.year}-{instant.month}-{instant.day}-{instant.hour}-{instant.minute}-{instant.second}.png"

            def shotkitdata():
                con_devices = adbutils.adb.device_list()
                if len(con_devices) == 0:
                    droid_screenshot_menu()
                    print(f"\n{color.WHITE}      [No Device Connected]\n")
                else:
   
                    global screenshot_location
                    try:
                        os.system(f"adb shell screencap -p /sdcard/{file_name}")
                        if screenshot_location == "":
                            print(f"\n{color.YELLOW}    Type in the Location or Press 'Enter' for default{color.WHITE}\n")
                            screenshot_location = input(f"{color.ORANGE}    [Screenshot]{color.WHITE} Location Entry >>> ")
                        if screenshot_location == "":
                            screenshot_location = "./config/media-files/screenshot"
                            print(f"\n{color.PURPLE}    Saving screenshot to {color.WHITE}{screenshot_location}\n{color.WHITE}")
                        else:
                            print(f"\n{color.PURPLE}    Saving screenshot to {color.WHITE}{screenshot_location}\n{color.WHITE}")
                        if screenshot_mode == "1":
                            os.system(f"adb pull /sdcard/{file_name} {screenshot_location}")
                        elif screenshot_mode == "s-shot":
                            os.system(f"adb pull /sdcard/{file_name} {screenshot_location}")
                        elif screenshot_mode == "anon-s-shot":
                            os.system(f"adb pull /sdcard/{file_name} {screenshot_location}")
                            print(f"\n{color.YELLOW}    Deleting screenshot from Target device\n{color.WHITE}")
                            os.system(f"adb shell rm /sdcard/{file_name}")
                        elif screenshot_mode == "2":
                            os.system(f"adb pull /sdcard/{file_name} {screenshot_location}")
                            print(f"\n{color.YELLOW}    Deleting screenshot from Target device\n{color.WHITE}")
                            os.system(f"adb shell rm /sdcard/{file_name}")
                        choice = input(f"\n{color.GREEN}    Do you want to Open the file? Y / N {color.WHITE}> ").lower()
                        if choice == "y" or choice == "":
                            os.system(f"{opener} {screenshot_location}/{file_name}")
                        elif not choice == "n":
                            while choice != "y" and choice != "n" and choice != "":
                                choice = input(f"\n{color.RED}    Invalid choice!,{color.WHITE} Press Y or N > ").lower()
                                if choice == "y" or choice == "":
                                    os.system(f"{opener} {screenshot_location}/{file_name}")
                        droid_screenshot_menu() 
                    except:
                        print(f"\n{color.RED}  Invalid Location!")

            match screenshot_mode:
                
                case "terminal":
                    terminal()
                    droid_screenshot_menu()
                case "caja":
                    caja()
                    droid_screenshot_menu()
                case "banner":
                    bannerfile()
                    droid_screenshot_menu()
                case "adb_file":
                    adbxcom()
                    droid_screenshot_menu()
                case "0"|"back"|"cd ..":
                    screensr_menu()
                    break
                case "99"|"clear":
                    droid_screenshot_menu()        
                case "1"|"s-shot":
                    shotkitdata()
                case "2"|"anon-s-shot":
                    shotkitdata()
                case "devices":
                    droid_screenshot_menu() 
                    list_devices()
                case "disconnect":
                    droid_screenshot_menu() 
                    disconnect()
                case other:
                    print(f"\n{color.RED}       [X] Invalid selection\n{color.YELLOW}       Please select a valid mode\n")
                    time.sleep(3)
                    droid_screenshot_menu() 
                                

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        print("\n")
        print(f"\n{color.WHITE}      [No Device Connected]\n")
        time.sleep(0.8)
        print(f"\n{color.WHITE}      Checking for connection ......\n")
        time.sleep(1.2)
        xconnect()
        time.sleep(1.2)
        con_devx = adbutils.adb.device_list()
        if len(con_devx) == 0:
            screensr_menu()
        else:
            screenshotkit()
    else:
        screenshotkit()

#-------------------------------- Screen Record --------------------------------------#

def screenrecorder():
    def screenrecorderkit():
        droid_screenrecorder_menu()
        while True:
            
            # Getting a temporary file name to store time specific results
            screenrecord_mode = input(f"""
    [{color.CYAN}99.{color.ORANGE} Clear screen                {color.CYAN}0.{color.ORANGE} Back{color.WHITE}]
    {color.WHITE}[s-record | anon-s-record | clear | back] \n
    {color.ORANGE}[Screen-recorder-mode]{color.WHITE} Select Mode >>> """).lower()
    
    # Getting a temporary file name to store time specific results
            instant = datetime.datetime.now()
            file_name = f"vid-{instant.year}-{instant.month}-{instant.day}-{instant.hour}-{instant.minute}-{instant.second}.mp4"
            def recorderkit():
                con_devices = adbutils.adb.device_list()
                if len(con_devices) == 0:
                    droid_screenrecorder_menu()
                    print(f"\n{color.WHITE}      [No Device Connected]\n")
                else:
                    global screenrecord_location
                    try:
                        duration = input(f"\n{color.CYAN}    Enter the recording duration (in seconds) > {color.WHITE}")
                        print(f"\n{color.YELLOW}    Starting Screen Recording...\n{color.WHITE}")
                        os.system(f"adb shell screenrecord --verbose --time-limit {duration} /sdcard/{file_name}")
                        if screenrecord_location == "":
                            print(f"\n{color.YELLOW}    Type in the Location or Press 'Enter' for default{color.WHITE}\n")
                            screenrecord_location = input(f"{color.ORANGE}    [Screen-r-file]{color.WHITE} Enter storage location >>> ")
                        if screenrecord_location == "":
                            screenrecord_location = "./config/media-files/screenrecord"
                            print(f"\n{color.PURPLE}    Saving video to {color.WHITE}{screenrecord_location}\n{color.WHITE}")
                        else:
                            print(f"\n{color.PURPLE}    Saving  video to {color.WHITE}{screenrecord_location}\n{color.WHITE}")
                        if screenrecord_mode == "1":
                            os.system(f"adb pull /sdcard/{file_name} {screenrecord_location}")
                        elif screenrecord_mode == "s-record":
                            os.system(f"adb pull /sdcard/{file_name} {screenrecord_location}")
                        elif screenrecord_mode == "anon-s-record":
                            os.system(f"adb pull /sdcard/{file_name} {screenrecord_location}")
                            print(f"\n{color.YELLOW}    Deleting video from Target device\n{color.WHITE}")
                            os.system(f"adb shell rm /sdcard/{file_name}")
                        elif screenrecord_mode == "2":
                            os.system(f"adb pull /sdcard/{file_name} {screenrecord_location}")
                            print(f"\n{color.YELLOW}    Deleting video from Target device\n{color.WHITE}")
                            os.system(f"adb shell rm /sdcard/{file_name}")
                        choice = input(f"\n{color.GREEN}    Do  you want to Open the file?     Y / N {color.WHITE}> ").lower()
                        if choice == "y" or choice == "":
                            os.system(f"{opener} {screenrecord_location}/{file_name}")
                        elif not choice == "n":
                            while choice != "y" and choice != "n" and choice != "":
                                choice = input(f"\n{color.RED}    Invalid choice!, Press Y or N > ").lower()
                                if choice == "y" or choice == "":
                                    os.system(f"{opener} {screenrecord_location}/{file_name}")
                        droid_screenrecorder_menu()
                    except: 
                        print(f"\n{color.RED}  Location/File Not Found !")

            match screenrecord_mode:
                
                case "terminal":
                    terminal()
                    droid_screenrecorder_menu()
                case "caja":
                    caja()
                    droid_screenrecorder_menu()
                case "banner":
                    bannerfile()
                    droid_screenrecorder_menu()
                case "adb_file":
                    adbxcom()
                    droid_screenrecorder_menu()
                case "0"|"back"|"cd ..":
                    screensr_menu()
                    break
                case "99"|"clear":
                    droid_screenrecorder_menu()
                    #print(banner.audio_menu)
                case "1"|"s-record":
                    recorderkit()
                case "2"|"anon-s-record":
                    recorderkit()
                case "devices":
                    droid_screenrecorder_menu()
                    list_devices()
                case "disconnect":
                    droid_screenrecorder_menu()
                    disconnect()
                case other:
                    print(f"\n{color.RED}       [X] Invalid selection\n{color.YELLOW}       Please select a valid mode\n")
                    time.sleep(3)
                    droid_screenrecorder_menu()


    con_devices = adbutils.adb.device_list()                
    if len(con_devices) == 0:
        print("\n")
        print(f"\n{color.WHITE}      [No Device Connected]\n")
        time.sleep(0.8)
        print(f"\n{color.WHITE}      Checking for connection ......\n")
        time.sleep(1.2)
        xconnect()
        time.sleep(1.2)
        con_devx = adbutils.adb.device_list()
        if len(con_devx) == 0:
            screensr_menu()
        else:
            screenrecorderkit()
    else:
        screenrecorderkit()

#-------------------------------------------------------------------------#
#------------------------- Android System --------------------------------#
#-------------------------------------------------------------------------#


def android_sys():
    droid_sys_menu()
    while True:
        sys_action_option = input(f"""    
    [{color.CYAN}99.{color.ORANGE} Clear screen                       {color.CYAN}0.{color.ORANGE} Back{color.WHITE}]
    {color.WHITE}[shell  |  lock  | unlock  | rebootmenu  | back]
    {color.WHITE}[device-info | battery-info | power-off | clear] \n
    {color.YELLOW}[Sys-command]{color.WHITE} Enter selection {color.GREEN}>>>{color.WHITE} """).lower()

        match sys_action_option:

            case "terminal":
                terminal()
                droid_sys_menu()
            case "caja":
                caja()
                droid_sys_menu()
            case "banner":
                bannerfile()
                droid_sys_menu()
            case "adb_file":
                adbxcom()
                droid_sys_menu()
            case "0"|"back"|"cd ..":
                droid_adb_command_menu()
                break
            case "99"|"clear":
                droid_sys_menu()
            case "1"|"shell":
                get_shell()
            case "2"|"lock":
                lock_device()
            case "3"|"unlock":
                unlock_device()                
            case "4"|"rebootmenu":
                android_reboot()
            case "5"|"device-info":
                get_device_info()
            case "6"|"battery-info":
                battery_info()
            case "7"|"power-off":
                power_off()
            case "devices":
                droid_sys_menu()
                list_devices()
            case "disconnect":
                droid_sys_menu()
                disconnect()
            case other:
                print(f"\n{color.RED}       [X] Invalid selection\n{color.YELLOW}       Please enter a valid option on menu above\n")
                time.sleep(3)
                droid_sys_menu()

def get_shell():
    def shellkit():
        os.system(clear)
        print(droid_sys_banner)
        print("\n")
        os.system("adb shell")

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        print("\n")
        print(f"\n{color.WHITE}      [No Device Connected]\n")
        time.sleep(0.8)
        print(f"\n{color.WHITE}      Checking for connection ......\n")
        time.sleep(1.2)
        xconnect()
        time.sleep(1.2)
        con_devx = adbutils.adb.device_list()
        if len(con_devx) == 0:
            droid_sys_menu()
        else:
            shellkit()
            droid_sys_menu()
    else:
        shellkit()
        droid_sys_menu()

def lock_device():

    def lockkit():
        droid_sys_menu()
        os.system("adb shell input keyevent 26")
        print(f"{color.GREEN}\n     Device locked{color.WHITE}")

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        droid_sys_menu()
        print(f"\n{color.WHITE}      [No Device Connected]\n")
    else:
        lockkit()

def unlock_device():
    def unlockkit():
        droid_sys_menu()
        try:
            # First, verify device is still connected
            verify_device = os.system("adb devices | grep -w 'device$' > /dev/null 2>&1")
            if verify_device != 0:
                print(f"{color.RED}\n    [X] Device disconnected during operation{color.WHITE}")
                return
            
            password = input(f"{color.YELLOW}\n    Enter password or Press 'Enter' for blank{color.WHITE} > ")
            # Wake up device - multiple attempts for reliability
            os.system("adb shell input keyevent 26 2>/dev/null")
            # Swipe up to reveal lock screen
            os.system("adb shell input swipe 300 1000 300 300 2>/dev/null")
            # Enter password if provided
            if password.strip():
                # Clear any existing text first
                os.system("adb shell input keyevent 123 2>/dev/null")  # KEYCODE_MOVE_END
                os.system("adb shell input keyevent 67 2>/dev/null")   # KEYCODE_DEL
                # Enter the password
                os.system(f'adb shell input text "{password}" 2>/dev/null')
                # Press enter/ok
                os.system("adb shell input keyevent 66 2>/dev/null")   # KEYCODE_ENTER
                os.system("adb shell input keyevent 23 2>/dev/null")   # KEYCODE_DPAD_CENTER (alternative)
            else:
                # For swipe-only unlock (no password)
                os.system("adb shell input keyevent 66 2>/dev/null")
            # Final check: verify device is unlocked by checking if screen is responsive
            os.system("adb shell input keyevent 3 2>/dev/null")  # HOME button press
            
            print(f"{color.GREEN}\n    [✓] Device unlocked successfully{color.WHITE}")
            
        except Exception as e:
            print(f"{color.RED}\n    [X] Unlock failed: {str(e)}{color.WHITE}")
            print(f"{color.YELLOW}    Tip: Ensure screen is visible and device is responsive{color.WHITE}")

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        droid_sys_menu()
        print(f"\n{color.WHITE}      [No Device Connected]\n")
        print(f"{color.YELLOW}      Please connect a device first{color.WHITE}")
    else:
        unlockkit()


def android_reboot():
    def rebootkit():
        droid_reboot_menu()
        def reboot(key):
            con_devices = adbutils.adb.device_list()
            if len(con_devices) == 0:
                droid_reboot_menu()
                print(f"\n{color.WHITE}      [No Device Connected]\n")
            else:
                droid_reboot_menu()
                print(f"\n{color.RED}    [Warning]{color.YELLOW} Restarting will disconnect the device{color.WHITE}")
                choice = input(f"{color.GREEN}\n    Do you want to continue?     Y / N > ").lower()
                if choice == "y" or choice == "":
                    pass
                elif choice == "n":
                    return
                else:
                    while choice != "y" and choice != "n" and choice != "":
                        choice = input("\nInvalid choice!, Press Y or N > ").lower()
                        if choice == "y" or choice == "":
                            pass
                        elif choice == "n":
                            return

                if key == "system":
                    os.system("adb reboot")
                    droid_reboot_menu()
                else:
                    os.system(clear)
                    print(droid_reboot_banner)
                    print(f"""
    {color.WHITE}1.{color.GREEN} Reboot to Recovery Mode
    {color.WHITE}2.{color.GREEN} Reboot to Bootloader
    {color.WHITE}3.{color.GREEN} Reboot to Fastboot Mode
    {color.WHITE}"""
        )
                    mode = input(f"{color.YELLOW}   [Advanced reboot mode]{color.WHITE} Enter selection {color.GREEN}>>>{color.WHITE} ").lower()
                    if mode == "1":
                        os.system("adb reboot recovery")
                    elif mode == "2":
                        os.system("adb reboot bootloader")
                    elif mode == "3":
                        os.system("adb reboot fastboot")
                    elif mode =="0":
                        droid_reboot_menu()
                    else:
                        print(f"\n{color.RED}       [X] Invalid selection\n{color.YELLOW}       Going back to Main Menu{color.WHITE}")
                        time.sleep(3)
                        droid_reboot_menu()
                        return

        while True:
            sys_action_option = input(f"""    
    [{color.CYAN}99.{color.ORANGE} Clear screen           {color.CYAN}0.{color.ORANGE} Back{color.WHITE}]
    {color.WHITE}[s-reboot | a-reboot | back | clear] \n
    {color.RED}[Reboot]{color.WHITE} Enter selection {color.GREEN}>>>{color.WHITE} """).lower()

            match sys_action_option:

                case "terminal":
                    terminal()
                    droid_reboot_menu()
                case "caja":
                    caja()
                    droid_reboot_menu()
                case "banner":
                    bannerfile()
                    droid_reboot_menu()
                case "adb_file":
                    adbxcom()
                    droid_reboot_menu()
                case "0"|"back"|"cd ..":
                    droid_sys_menu()
                    break
                case "99"|"clear":
                    droid_reboot_menu()              
                case "1"|"s-reboot":
                    reboot("system")
                case "2"|"a-reboot":
                    reboot("advanced")
                case "devices":
                    droid_reboot_menu()
                    list_devices()
                case "disconnect":
                    droid_reboot_menu()
                    disconnect()
                case other:
                    print(f"\n{color.RED}       [X] Invalid selection\n{color.YELLOW}       Please enter a valid option on menu above\n")
                    time.sleep(3)
                    droid_reboot_menu()

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        droid_sys_menu()
        print(f"\n{color.WHITE}      [No Device Connected]\n")
    else:
        rebootkit()

def power_off():
    def poweroffkit():
        droid_sys_menu()
        print(f"\n{color.RED}    [Warning]{color.YELLOW} Powering off device will disconnect the device{color.WHITE}")
        choice = input(f"{color.GREEN}\n    Do you want to continue?     Y / N > ").lower()
        if choice == "y" or choice == "":
            droid_sys_menu()
            pass
        elif choice == "n":
            droid_sys_menu()
            return
        else:
            while choice != "y" and choice != "n" and choice != "":
                droid_sys_menu()
                choice = input(f"\n{color.RED}    Invalid choice!,{color.CYAN} Press Y or N > ").lower()
                if choice == "y" or choice == "":
                    pass
                elif choice == "n":
                    droid_sys_menu()
                    return
        os.system(f"adb shell reboot -p")
        print("\n")

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        droid_sys_menu()
        print(f"\n{color.WHITE}      [No Device Connected]\n")
    else:
        poweroffkit()

def battery_info():
    def batterykit():
        droid_sys_menu()
        battery = os.popen(f"adb shell dumpsys battery").read()
        print(f"""
    {color.YELLOW}Battery Information :
    {color.WHITE}{battery}
    """)
    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        droid_sys_menu()
        print(f"\n{color.WHITE}      [No Device Connected]\n")
    else:
        batterykit()

def get_device_info():
    def device_infokit():
        droid_sys_menu()
        model = os.popen(f"adb shell getprop ro.product.model").read()
        manufacturer = os.popen(f"adb shell getprop ro.product.manufacturer").read()
        chipset = os.popen(f"adb shell getprop ro.product.board").read()
        android = os.popen(f"adb shell getprop ro.build.version.release").read()
        security_patch = os.popen(f"adb shell getprop ro.build.version.security_patch").read()
        device = os.popen(f"adb shell getprop ro.product.vendor.device").read()
        sim = os.popen(f"adb shell getprop gsm.sim.operator.alpha").read()
        encryption_state = os.popen(f"adb shell getprop ro.crypto.state").read()
        build_date = os.popen(f"adb shell getprop ro.build.date").read()
        sdk_version = os.popen(f"adb shell getprop ro.build.version.sdk").read()
        wifi_interface = os.popen(f"adb shell getprop wifi.interface").read()
        abi = os.popen(f"adb shell getprop ro.product.cpu.abi").read()

        print(
        f"""
    {color.YELLOW}Model :{color.WHITE} {model}\
    {color.YELLOW}Manufacturer :{color.WHITE} {manufacturer}\
    {color.YELLOW}Chipset :{color.WHITE} {chipset}\
    {color.YELLOW}Android Version :{color.WHITE} {android}\
    {color.YELLOW}Security Patch :{color.WHITE} {security_patch}\
    {color.YELLOW}Device :{color.WHITE} {device}\
    {color.YELLOW}SIM :{color.WHITE} {sim}\
    {color.YELLOW}Encryption State :{color.WHITE} {encryption_state}\
    {color.YELLOW}Build Date :{color.WHITE} {build_date}\
    {color.YELLOW}SDK Version :{color.WHITE} {sdk_version}\
    {color.YELLOW}WiFi Interface :{color.WHITE} {wifi_interface}\
    {color.YELLOW}Device Abi  :{color.WHITE} {abi}\
"""
    )

    con_devices = adbutils.adb.device_list()
    if len(con_devices) == 0:
        droid_sys_menu()
        print(f"\n{color.WHITE}      [No Device Connected]\n")
    else:
        device_infokit()

#----------------------------------------------------------------------------#
#------------------- Metasploit Section -------------------------------------#
#----------------------------------------------------------------------------#

# Global variables
run_phonesploit_pro = True
operating_system = ""
clear = "clear"
opener = "xdg-open"


# Locations
screenshot_location = ""
screenrecord_location = ""
pull_location = ""

# Concatenating banner color with the selected banner
main_banner = random.choice(color.color_list) + banner.droid_toolkit
droid_adb_command = random.choice(color.color_list) + banner.android_adb_command
droid_connect_banner = random.choice(color.color_list) + banner.android_connect
droid_devlist_banner = random.choice(color.color_list) + banner.android_devlist
msf_banner = random.choice(color.color_list) + banner.bannerx
droid_scrcpy_banner = random.choice(color.color_list) + banner.android_scrcpy
droid_sys_banner = random.choice(color.color_list) + banner.android_sys
droid_nav_banner = random.choice(color.color_list) + banner.android_nav
droid_screensr_banner = random.choice(color.color_list) + banner.android_screensr
droid_screenshot_banner = random.choice(color.color_list) + banner.android_screenshot
droid_screenrecorder_banner = random.choice(color.color_list) + banner.android_screenrecorder
droid_reboot_banner = random.choice(color.color_list) + banner.android_reboot
droid_audio_kit = random.choice(color.color_list) + banner.android_audio_kit
droid_audio_recorder = random.choice(color.color_list) + banner.android_audio_recorder
droid_audio_stream = random.choice(color.color_list) + banner.android_audio_stream
start()

if run_phonesploit_pro:
    print(f'\n{color.ORANGE}    [{color.GREEN}+{color.ORANGE}]{color.WHITE} Starting MSF-ADB Server ..... ')
    #os.system("adb start-server")
    subprocess.run(['adb', 'start-server'], capture_output=True)
    time.sleep(1)
    print(f"{color.ORANGE}    [{color.GREEN}+{color.ORANGE}] {color.GREEN}Ok")
    time.sleep(1)
    print(f'{color.ORANGE}    [{color.GREEN}+{color.ORANGE}]{color.WHITE} Initiating services ....')
    time.sleep(1)
    print(f"{color.ORANGE}    [{color.GREEN}+{color.ORANGE}] {color.GREEN}Ok\n")
    time.sleep(1.8)
    print(f'{color.ORANGE}    [{color.GREEN}🚀{color.ORANGE}]{color.WHITE} Welcome to Android {color.YELLOW} Command Center   {color.ORANGE}\n')
    time.sleep(2)
    clear_screen()
    while run_phonesploit_pro:
        try:
            main()
        except KeyboardInterrupt:
            exit_phonesploit_pro()
