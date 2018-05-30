#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
cor = ['\033[95m', '\033[96m', '\033[92m','\033[93m','\033[91m','\033[0m']
colors = cor[randint(0,5)]
banner = colors + """\
================================================================================================
 ██████╗   > Python For Security            ██████╗   > We Are Anonymous Arab           ███████╗ 
██╔════╝   > github.com/Oseid               ██╔══██╗  > We Are Legion                   ██╔════╝ 
██║        > Control Panel Finder           ██████╔╝  > We Don't Forget                 █████╗   
██║        > By: Oseid Aldary               ██╔═══╝   > We Don't forgive                ██╔══╝   
╚██████╗   > Ve: 1.0                        ██║       > Expect Us                       ██║      
 ╚═════╝                                    ╚═╝                                         ╚═╝      
                                                                                                 """

def examples():
 print(banner)
 print(cor[5]+"""==================================================================================================

[#] Examples [#]

[1] To Scan Website Without Use proxy and set page source code :> python CPFinder.py -w www.google.com

This Command take a lot of time because you not selected the page source code so he try all source code links > [asp,aspx,brf,cfm,cgi,js,php]
===================================================

[2] To Scan Website with select page source code :> python CPFinder.py -w www.google.com -c php

This Command Better than firs comand and this take many minute to stop :)
===================================================

[3] To Scan Website With Select page source code and use proxy :> python CPFinder.py -w www.google.com -c php -p

Use This Command for Bypass Website Bloked attack and to hedding you Ip Addr
==================================================

[#] So You Have 3 Command You Can Use:

1> python CPFinder.py -w target website
2> python CPFinder.py -w target website -c page source code
3> python CPFinder.py -w target website -c page source code -p
==================================================

Note: You Can Change The Links in Files in Core Folder If you Have Some Links To Scan Add it In The Files :)

[#] Thanks For Usage :)


""")

## Tool Examples Done ! :)
