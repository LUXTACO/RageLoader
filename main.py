import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mBox
import customtkinter
import urllib.request
from pystyle import Colorate, Colors, Center
import os
import time
from colorama import Fore, Back, Style
from PIL import Image
from threading import *

# Load
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/")
logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "RaLd_Logo.png")), size=(100, 100))

# Commands / Defs
def title():
    os.system("cls")
    banner = Center.XCenter(Colorate.Vertical(Colors.cyan_to_green, """

                    ██████╗  █████╗  ██████╗ ███████╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
                    ██╔══██╗██╔══██╗██╔════╝ ██╔════╝██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                    ██████╔╝███████║██║  ███╗█████╗  ██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
                    ██╔══██╗██╔══██║██║   ██║██╔══╝  ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
                    ██║  ██║██║  ██║╚██████╔╝███████╗███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
                    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                  
    """))
    print(banner)
    print(Center.XCenter(f"""{Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Made By Taquito & NotRageJustGood {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Version 1.0 {Fore.LIGHTRED_EX}

    """))

def quit_app():
    """Close the window and terminate the application."""
    win.destroy()

def save_last_click_pos(event):
    """Save the position of the last mouse click."""
    global last_click_x, last_click_y
    last_click_x = event.x
    last_click_y = event.y

def dragging(event):
    """Move the window with the mouse."""
    x, y = event.x - last_click_x + win.winfo_x(), event.y - last_click_y + win.winfo_y()
    win.geometry("+%s+%s" % (x , y))

def osiris():
    """Download Osiris"""
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download1346.mediafire.com/ucsoymnbmchg/umx0drrvj2e8do7/Osiris.dll'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/osiris.dll')
    print("Done!\n")
    time.sleep(2)
    start = input("Do you want to start the injector? (Y/N): ")
    if start == 'Y' or start == 'y':
        print("Starting Injector!")
        os.system("start ./bin/injector")
        os.system("start .\downloads")
    else:
        print("\nGot it!")
        time.sleep(2)
        print("Opening Download Folder...")
        time.sleep(2)
        print("Opened!\n")
        os.system("start .\downloads")

def sakara():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download1979.mediafire.com/o4n0i6qb1leg/u5pmo9417o01ynk/sakara.dll'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/sakara.dll')
    print("Done!\n")
    time.sleep(2)
    start = input("Do you want to start the injector? (Y/N): ")
    if start == 'Y' or start == 'y':
        print("Starting Injector!")
        os.system("start ./bin/injector")
        os.system("start .\downloads")
    else:
        print("\nGot it!")
        time.sleep(2)
        print("Opening Download Folder...")
        time.sleep(2)
        print("Opened!\n")
        os.system("start .\downloads")

def zenox():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download1526.mediafire.com/une3dqovg3eg/l37jepvlklgpvv6/zenox.dll'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/zenox.dll')
    print("Done!\n")
    time.sleep(2)
    start = input("Do you want to start the injector? (Y/N): ")
    if start == 'Y' or start == 'y':
        print("Starting Injector!")
        os.system("start ./bin/injector")
        os.system("start .\downloads")
    else:
        print("\nGot it!")
        time.sleep(2)
        print("Opening Download Folder...")
        time.sleep(2)
        print("Opened!\n")
        os.system("start .\downloads")

def configosiris():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download1484.mediafire.com/r29mugmvaozg/1ly337297q5dch1/LegitV3'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/configs/osiris')
    print("Done!\n")
    time.sleep(2)
    os.system("start .\downloads\configs")

def configzenox():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download1509.mediafire.com/kwo8vcwomj2g/c7ydddz3kkvjufb/rage.cfg'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/configs/zenox.cfg')
    print("Done!\n")
    time.sleep(2)
    os.system("start .\downloads\configs")

def configsakara():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download1484.mediafire.com/8h8blgm9ghmg/pu8wjv031wuaokb/SuperLegit'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/configs/sakara')
    print("Done!\n")
    time.sleep(2)
    os.system("start .\downloads\configs")

def kiddons():
    option1 = input("Do you want to download Kiddons? (Y/N): ")
    if option1 == 'Y' or option1 == 'y':
        print("\nDirectory Set!")
        time.sleep(2)
        url = 'https://calamitymod.net/Kiddions/modest-menu_v0.9.6_[kiddionsmodmenu.com]_.zip'
        print("Fetching URL...")
        time.sleep(2)
        print("Downloading...")
        urllib.request.urlretrieve(url, './bin/kiddons-gta.zip')
        print("Done!\n")
        time.sleep(2)
        option = input("Do you want to run Kiddons? (Y/N): ")
        if option == 'Y' or option == 'y':
            print("\nDirectory Set!")
            time.sleep(1)
            os.system("cd ./bin")
            print("Unzipping...")
            time.sleep(1)
            os.system("unzip.bat")
            print("\nDeleting temp file...")
            time.sleep(1)
            os.system("delete.bat")
            print("\n\nStarting Kiddons...")
            os.system("start ./bin/modest-menu.exe")
            print("Done!")
        else: 
            print("\nGot it!\n")
            print("Kiddons is located on the bin folder!")
    else:
        print("\nGot it!")
        print("Starting Kiddons...")
        os.system("start ./bin/modest-menu.exe")
        print("Done!\n")

def meteor():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download2266.mediafire.com/obh5d3atw91g/r516k05bx4yizwk/meteor-client-0.5.1.jar'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/meteor(fabric).jar')
    print("Done!")
    time.sleep(2)
    os.system("start .\downloads")

def inertia():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download1514.mediafire.com/5euym42t5xvg/qan3e51hlqwxpvi/Inertia+Client+3.1.3+-+1.16.5.jar'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/inertia(fabric).jar')
    print("Done!")
    time.sleep(2)
    os.system("start .\downloads")

def impact():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download1594.mediafire.com/0bc3yp0fds8g/ja88oe1za7yo3l1/ImpactInstaller-0.9.5.jar'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/Impact(execute_me!).jar')
    print("Done!")
    time.sleep(2)
    os.system("start .\downloads")
    
def xamp():
    print("\nDirectory Set!")
    time.sleep(2)
    url = 'https://download857.mediafire.com/ppjz8kxveocg/f553b80dw48zqig/yhBCG0Za.exe'
    print("Fetching URL...")
    time.sleep(2)
    print("Downloading...")
    urllib.request.urlretrieve(url, './downloads/Xamp.exe')
    print("Done!")
    time.sleep(2)
    os.system("start .\downloads")
    print("")

def get_help():
    print("Fetching URL...")
    time.sleep(2)
    print("Opening...")
    time.sleep(2)
    print("Opened!")
    os.system("start https://discord.gg/vT94d7XNmf")

def folder():
    print("Opening Download Folder...")
    time.sleep(2)
    print("Opened!\n")
    os.system("start .\downloads")

def injector():
    print("Starting Injector!")
    os.system("start ./bin/injector")

def hwic():
    setup= input("Run setup? (Y/N): ")
    if setup == 'Y' or setup == 'y':
        os.system("python ./bin/hwicstp.py")
        print(f"{Fore.LIGHTRED_EX}")
        run = input("Run HWIC? (Y/N): ")
        if run == 'Y' or run == 'y':
            os.system("python ./bin/hwic.py")
        else:
            print("\nGot it!")
    else:
        print("\nGot It!")
        time.sleep(1)
        print("Running...")
        os.system("python ./bin/hwic.py")
    print(f"{Fore.LIGHTRED_EX}\nDone!")

# Threaded

def thosiris():
    t1=Thread(target=osiris)
    t1.start()

def thhelp():
    t2=Thread(target=get_help)
    t2.start()

def thfolder():
    t3=Thread(target=folder)
    t3.start()

def thinjector():
    t4=Thread(target=injector)
    t4.start()

def thsakara():
    t5=Thread(target=sakara)
    t5.start()

def thzenox():
    t6=Thread(target=zenox)
    t6.start()

def thconos():
    t7=Thread(target=configosiris)
    t7.start()

def thconzen():
    t8=Thread(target=configzenox)
    t8.start()

def thconsak():
    t9=Thread(target=configsakara)
    t9.start()

def thhwic():
    t10=Thread(target=hwic)
    t10.start()

def thkiddo():
    t11=Thread(target=kiddons)
    t11.start()
    
def thmeteor():
    t12=Thread(target=meteor)
    t12.start()

def thinertia():
    t13=Thread(target=inertia)
    t13.start()

def thimpact():
    t14=Thread(target=impact)
    t14.start()
    
def thxamp():
    t15=Thread(target=xamp)
    t15.start()

# Theme Settings
customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue") 

# Window Settings
title()
win = customtkinter.CTk()
win.title("RageLoader")
win.iconbitmap("")
win.resizable(False, False)
win.geometry("800x520")
win.overrideredirect(True)
win.bind('<Button-1>', save_last_click_pos)
win.bind('<B1-Motion>', dragging)
win.attributes("-topmost", True)

# Window Content
title = customtkinter.CTkLabel(win ,text=" RageLoader", image=logo, compound="left", width= 800, height= 115, fg_color=("#141414", "#141414"), corner_radius=20, font=("Arial Rounded MT Bold", 30))
title.place(x= 0, y= -15)

""" Tabs """ 

tabview = customtkinter.CTkTabview(win)
tabview.pack(padx=20, pady=100)
tabview.configure(width= 800, height= 800)

tabview.add("CSGO")
tabview.add("VALO")
tabview.add("GTAV")
tabview.add("MINE")
tabview.add("TOOLS")
tabview.add("CONFIGS")
tabview.set("CSGO")

# CS:GO 
button = customtkinter.CTkButton(tabview.tab("CSGO"), text= "Osiris MultiHack", command= thosiris)
button.pack(padx=20, pady=20)
button = customtkinter.CTkButton(tabview.tab("CSGO"), text= "Sakara MultiHack", command= thsakara)
button.pack(padx=20, pady=20)
button = customtkinter.CTkButton(tabview.tab("CSGO"), text= "Zenox RageHack", command= thzenox)
button.pack(padx=20, pady=20)
button = customtkinter.CTkButton(tabview.tab("CSGO"), text= "Xamp LegitHack", command= thxamp)
button.pack(padx=20, pady=20)

# Valorant
button = customtkinter.CTkButton(tabview.tab("VALO"), text= "Coming Soon!")
button.pack(padx=20, pady=20)

# GTAV
button = customtkinter.CTkButton(tabview.tab("GTAV"), text= "Kiddons Moddest Menu", command= thkiddo)
button.pack(padx=20, pady=20)

# Minecraft
button = customtkinter.CTkButton(tabview.tab("MINE"), text= "Meteor 1.19.2", command= thmeteor)
button.pack(padx=20, pady=20)
button = customtkinter.CTkButton(tabview.tab("MINE"), text= "Inertia 1.16.5", command= thinertia)
button.pack(padx=20, pady=20)
button = customtkinter.CTkButton(tabview.tab("MINE"), text= "Impact 1.12.2", command= thimpact)
button.pack(padx=20, pady=20)

# Tools 
button = customtkinter.CTkButton(tabview.tab("TOOLS"), text= "HWIC", command= thhwic)
button.pack(padx=20, pady=20)

# Configs
button = customtkinter.CTkButton(tabview.tab("CONFIGS"), text= "Zenox - Rage", command= thconzen)
button.pack(padx=20, pady=20)
button = customtkinter.CTkButton(tabview.tab("CONFIGS"), text= "Osiris - Legit", command= thconos)
button.pack(padx=20, pady=20)
button = customtkinter.CTkButton(tabview.tab("CONFIGS"), text= "Sakara - SuperLegit", command= thconsak)
button.pack(padx=20, pady=20)

# TextBox 
textbox = customtkinter.CTkTextbox(win)
textbox.place(x= 20, y= 420)
textbox.configure(width= 760, height= 80)

textbox.insert("0.0", "Welcome to RageLoader©\nA really cool loader with a whole repo of cheats for: Minecraft, Valorant, CS:GO, GTAV and also TOOLS for cheating! \n\nMade with ♡ by Taquito & NotRageJustGood")
text = textbox.get("0.0", "end")

textbox.configure(state="disabled")

#############

close_button = customtkinter.CTkButton(win, text="X", command=quit_app, width=40, height= 40, font=("Arial Rounded MT Bold", 15))
close_button.place(x= 750, y= 25)
help_button = customtkinter.CTkButton(win, text="?", command=thhelp, width=40, height= 40, font=("Arial Rounded MT Bold", 15))
help_button.place(x= 700, y= 25)
foldr_button = customtkinter.CTkButton(win, text="📁", command=thfolder, width=40, height= 40, font=("Arial Rounded MT Bold", 15))
foldr_button.place(x= 10, y= 25)
injector_button = customtkinter.CTkButton(win, text="💉", command=thinjector, width=40, height= 40, font=("Arial Rounded MT Bold", 15))
injector_button.place(x= 60, y= 25)

win.mainloop()