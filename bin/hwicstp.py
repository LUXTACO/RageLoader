import wmi
import platform
import subprocess
import re
import random
import string
import os
import time
from colored import fg
import sys,time,random

typing_speed = 40 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

color = fg('red')
color2 = fg('cyan')
color3 = fg('white')

print(color + """
$$\   $$\ $$\      $$\ $$$$$$\  $$$$$$\         $$$$$$\  $$$$$$$$\ $$$$$$$$\ $$\   $$\ $$$$$$$\  
$$ |  $$ |$$ | $\  $$ |\_$$  _|$$  __$$\       $$  __$$\ $$  _____|\__$$  __|$$ |  $$ |$$  __$$\ 
$$ |  $$ |$$ |$$$\ $$ |  $$ |  $$ /  \__|      $$ /  \__|$$ |         $$ |   $$ |  $$ |$$ |  $$ |
$$$$$$$$ |$$ $$ $$\$$ |  $$ |  $$ |            \$$$$$$\  $$$$$\       $$ |   $$ |  $$ |$$$$$$$  |
$$  __$$ |$$$$  _$$$$ |  $$ |  $$ |             \____$$\ $$  __|      $$ |   $$ |  $$ |$$  ____/ 
$$ |  $$ |$$$  / \$$$ |  $$ |  $$ |  $$\       $$\   $$ |$$ |         $$ |   $$ |  $$ |$$ |      
$$ |  $$ |$$  /   \$$ |$$$$$$\ \$$$$$$  |      \$$$$$$  |$$$$$$$$\    $$ |   \$$$$$$  |$$ |      
\__|  \__|\__/     \__|\______| \______/        \______/ \________|   \__|    \______/ \__|      
                                                                                                 
""")
print (color3 + "==================================================================================================")
print (color2 + """
""")
slow_type("Ïnstalling Dependencies...")
print("")
print("")
time.sleep(1)
os.system ("pip install wmi")
time.sleep(0.5)
os.system ("pip install platform")
time.sleep(0.5)
os.system ("pip install subprocess")
time.sleep(0.5)
os.system ("pip install re")
time.sleep(0.5)
print("")
slow_type(color + "All Done!")
time.sleep(0.5)
print("")
print(" ")
print(color3 + "======================================================================================")
print(color + " ")
os.system("pause")