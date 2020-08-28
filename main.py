# Project Name: Telnet Patch Tool
# Project Author: VoidLSD
# Project Reason: Telnet Patch Tool is used to patch telnets from common attack vectors used by botnets like the Mirai.

import os
import subprocess
import time

intro = """
  ▄▄▄▄▄ ▄▄▄· ▄▄▄▄
  • █  ▐█ ▄█• █  
   ▐█.▪ ██▀· ▐█.▪
   ▐█▌·▐█▪·• ▐█▌·
   ▀▀▀ .▀    ▀▀▀ 
 Telnet Patch Tool
 Created by VoidLSD
"""

print(intro)
time.sleep(2)
print("Starting patch..")
os.system("iptables -t mangle -A PREROUTING -p icmp -j DROP")
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 23 -j DROP")
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 7547 -j DROP")
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 5555 -j DROP")
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 5358 -j DROP")
print("Your ioT device has now been secured from common ioT vectors.")
time.sleep(2)
print("Restarting ioT device to clean any previous infections..")
time.sleep(5)
os.system("reboot")
