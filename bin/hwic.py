"""
1. Get Motherboard, CPU, RAM, SSD and GPU HWID
2. Print the data onscreen
"""

import wmi
import platform
import subprocess
import re
import random
import string
import os
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
$$\   $$\ $$\      $$\ $$$$$$\ $$$$$$$\        $$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\  
$$ |  $$ |$$ | $\  $$ |\_$$  _|$$  __$$\       \_$$  _|$$$\  $$ |$$  _____|$$  __$$\ 
$$ |  $$ |$$ |$$$\ $$ |  $$ |  $$ |  $$ |        $$ |  $$$$\ $$ |$$ |      $$ /  $$ |
$$$$$$$$ |$$ $$ $$\$$ |  $$ |  $$ |  $$ |        $$ |  $$ $$\$$ |$$$$$\    $$ |  $$ |
$$  __$$ |$$$$  _$$$$ |  $$ |  $$ |  $$ |        $$ |  $$ \$$$$ |$$  __|   $$ |  $$ |
$$ |  $$ |$$$  / \$$$ |  $$ |  $$ |  $$ |        $$ |  $$ |\$$$ |$$ |      $$ |  $$ |
$$ |  $$ |$$  /   \$$ |$$$$$$\ $$$$$$$  |      $$$$$$\ $$ | \$$ |$$ |       $$$$$$  |
\__|  \__|\__/     \__|\______|\_______/       \______|\__|  \__|\__|       \______/ 
                                                                                     
""")
print (color3 + "======================================================================================")
print (color2 + """
""")
def get_cpu_info():
    cpu_info = {}
    if platform.system() == "Windows":
        cpu_info = get_cpu_info_windows()
    elif platform.system() == "Linux":
        cpu_info = get_cpu_info_linux()
    elif platform.system() == "Darwin":
        cpu_info = get_cpu_info_macos()
    return cpu_info

def get_cpu_info_windows():
    cpu_info = {}
    w = wmi.WMI()
    for cpu in w.Win32_Processor():
        cpu_info['name'] = cpu.Name
        cpu_info['identifier'] = cpu.ProcessorId.strip()
        cpu_info['description'] = cpu.Description
        cpu_info['number_of_cores'] = cpu.NumberOfCores
        cpu_info['number_of_logical_processors'] = cpu.NumberOfLogicalProcessors
    return cpu_info

def get_cpu_info_linux():
    cpu_info = {}
    command = "lscpu"
    all_info = subprocess.check_output(command, shell=True).strip()
    for line in all_info.split("\n"):
        if ":" in line:
            key, value = line.split(":")
            cpu_info[key.strip()] = value.strip()
    return cpu_info

def get_cpu_info_macos():
    cpu_info = {}
    command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
    all_info = subprocess.check_output(command, shell=True).strip()
    cpu_info['name'] = all_info
    return cpu_info

def get_ram_info():
    ram_info = {}
    if platform.system() == "Windows":
        ram_info = get_ram_info_windows()
    elif platform.system() == "Linux":
        ram_info = get_ram_info_linux()
    elif platform.system() == "Darwin":
        ram_info = get_ram_info_macos()
    return ram_info

def get_ram_info_windows():
    ram_info = {}
    w = wmi.WMI()
    for memory in w.Win32_PhysicalMemory():
        ram_info['capacity'] = int(memory.Capacity) / 1024 / 1024 / 1024
    return ram_info

def get_ram_info_linux():
    ram_info = {}
    command = "cat /proc/meminfo"
    all_info = subprocess.check_output(command, shell=True).strip()
    for line in all_info.split("\n"):
        if ":" in line:
            key, value = line.split(":")
            ram_info[key] = value
    return ram_info

def get_ram_info_macos():
    ram_info = {}
    command = "system_profiler SPHardwareDataType | grep Memory"
    all_info = subprocess.check_output(command, shell=True).strip()
    ram_info['capacity'] = int(re.findall(r'\d+', all_info)[0]) / 1024 / 1024 / 1024
    return ram_info

def get_motherboard_info():
    motherboard_info = {}
    if platform.system() == "Windows":
        motherboard_info = get_motherboard_info_windows()
    elif platform.system() == "Linux":
        motherboard_info = get_motherboard_info_linux()
    elif platform.system() == "Darwin":
        motherboard_info = get_motherboard_info_macos()
    return motherboard_info

def get_motherboard_info_windows():
    motherboard_info = {}
    w = wmi.WMI()
    for motherboard in w.Win32_BaseBoard():
        motherboard_info['manufacturer'] = motherboard.Manufacturer
        motherboard_info['product'] = motherboard.Product
        motherboard_info['serial_number'] = motherboard.SerialNumber
    return motherboard_info

def get_motherboard_info_linux():
    motherboard_info = {}
    command = "sudo dmidecode -t 2"
    all_info = subprocess.check_output(command, shell=True).strip()
    for line in all_info.split("\n"):
        if ":" in line:
            key, value = line.split(":")
            motherboard_info[key.strip()] = value.strip()
    return motherboard_info

def get_motherboard_info_macos():
    motherboard_info = {}
    command = "system_profiler SPHardwareDataType | grep 'Model Identifier'"
    all_info = subprocess.check_output(command, shell=True).strip()
    motherboard_info['product'] = all_info.split(":")[1].strip()
    return motherboard_info

def get_gpu_info():
    gpu_info = {}
    if platform.system() == "Windows":
        gpu_info = get_gpu_info_windows()
    elif platform.system() == "Linux":
        gpu_info = get_gpu_info_linux()
    elif platform.system() == "Darwin":
        gpu_info = get_gpu_info_macos()
    return gpu_info

def get_gpu_info_windows():
    gpu_info = {}
    w = wmi.WMI()
    for gpu in w.Win32_VideoController():
        gpu_info['name'] = gpu.Name
        gpu_info['driver_version'] = gpu.DriverVersion
    return gpu_info

def get_gpu_info_linux():
    gpu_info = {}
    command = "lspci | grep VGA"
    all_info = subprocess.check_output(command, shell=True).strip()
    gpu_info['name'] = all_info.split(":")[2].strip()
    return gpu_info

def get_gpu_info_macos():
    gpu_info = {}
    command = "system_profiler SPDisplaysDataType | grep Chipset"
    all_info = subprocess.check_output(command, shell=True).strip()
    gpu_info['name'] = all_info.split(":")[1].strip()
    return gpu_info

def get_ssd_info():
    ssd_info = {}
    if platform.system() == "Windows":
        ssd_info = get_ssd_info_windows()
    elif platform.system() == "Linux":
        ssd_info = get_ssd_info_linux()
    elif platform.system() == "Darwin":
        ssd_info = get_ssd_info_macos()
    return ssd_info

def get_ssd_info_windows():
    ssd_info = {}
    w = wmi.WMI()
    for ssd in w.Win32_DiskDrive():
        ssd_info['name'] = ssd.Name
        ssd_info['serial_number'] = ssd.SerialNumber
    return ssd_info

def get_ssd_info_linux():
    ssd_info = {}
    command = "sudo hdparm -i /dev/sda | grep Model"
    all_info = subprocess.check_output(command, shell=True).strip()
    ssd_info['name'] = all_info.split(":")[1].strip()
    return ssd_info

def get_ssd_info_macos():
    ssd_info = {}
    command = "system_profiler SPStorageDataType | grep 'Media Name'"
    all_info = subprocess.check_output(command, shell=True).strip()
    ssd_info['name'] = all_info.split(":")[1].strip()
    return ssd_info

def get_hwid():
    hwid = {}
    hwid['cpu'] = get_cpu_info()
    hwid['ram'] = get_ram_info()
    hwid['motherboard'] = get_motherboard_info()
    hwid['gpu'] = get_gpu_info()
    hwid['ssd'] = get_ssd_info()
    return hwid

def print_hwid(hwid):
    print("CPU:")
    for key, value in hwid['cpu'].items():
        print("\t{}: {}".format(key, value))
    print("RAM:")
    for key, value in hwid['ram'].items():
        print("\t{}: {}".format(key, value))
    print("Motherboard:")
    for key, value in hwid['motherboard'].items():
        print("\t{}: {}".format(key, value))
    print("GPU:")
    for key, value in hwid['gpu'].items():
        print("\t{}: {}".format(key, value))
    print("SSD:")
    for key, value in hwid['ssd'].items():
        print("\t{}: {}".format(key, value))

if __name__ == "__main__":
    hwid = get_hwid()
    print_hwid(hwid)
    print(" ")
    print(color3 + "======================================================================================")
    print(color2 + " ")
    os.system("pause")