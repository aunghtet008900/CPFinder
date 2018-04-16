#!/usr/bin/python
# -*- coding: utf-8 -*-
#[>] Find Control Panel Tool Coded In Python
#[>] I LOVE PYTHON :)
#[>] Coded By : Oseid Aldary
#[>] 15/4/2018
#============== START ==============

# IMPORT LIBRARIES..:)
import optparse,datetime,socket
from time import sleep
from random import randint
from urllib2 import urlopen, Request, URLError, HTTPError,install_opener,build_opener,ProxyHandler
from Core.examples import examples
### Import Library Done!

# Colors #
cor = ['\033[95m', '\033[96m', '\033[92m','\033[93m','\033[91m','\033[0m']
colors = cor[randint(0,5)]
# Set Colors Done!

## Checking Internet Connection....
server = "www.google.com"
def check():
  try:
     ip = socket.gethostbyname(server)
     con = socket.create_connection((ip, 80), 2)
     return True
  except:
   return False
## Check internet Done !

## SHOW TIME NOW
now = datetime.datetime.now()
hour = now.hour
min = now.minute
sec = now.second
timenow = "{}:{}:{}".format(hour,min,sec)
## SHOW TIME DONE!

## TOOL BANNER
banner = colors + """
================================================================================================
 ██████╗   > Python For Security            ██████╗   > We Are Anonymous Arab           ███████╗ 
██╔════╝   > github.com/Oseid               ██╔══██╗  > We Are Legion                   ██╔════╝ 
██║        > Control Panel Finder           ██████╔╝  > We Don't Forget                 █████╗   
██║        > By: Oseid Aldary               ██╔═══╝   > We Don't forgive                ██╔══╝   
╚██████╗   > Ve: 1.0                        ██║       > Expect Us                       ██║      
 ╚═════╝                                    ╚═╝                                         ╚═╝      
                                                                                                 """
####

## PROXY FOR USAGE
def proxy():

	p1 = "185.53.179.29:80" #netherlands
        p2 = "162.255.119.250:80" #US
	p3 = "193.111.63.208:80" #netherlands
      	p4 = "104.28.20.2:80" #US
	p5 = "62.210.105.242:80" #FR
	p6 = "162.255.119.250:80" #US
	p7 = "103.224.212.222:80" #UK
	p8 = "104.28.20.2:80" #US
	p9 = "93.191.169.211:80" #UK
	p10 = "69.64.147.10:80" #US
	p11 = "62.149.128.160:80" #netherlands
	p12 = "46.4.207.219:80" #FR

	proxys = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
	randproxy = proxys[randint(0,11)]
	return randproxy
proxyy = proxy()

## Tool Menu Options
parse = optparse.OptionParser(cor[4]+banner+cor[5]+"""
Usage: python ./CPFinder.py [OPTIONS...]

OPTIONS:
	-w --website      ::> Set Target Website.

	-c --source-code  ::> Set Web Page Source Code example:php.

	-p --use-proxy    ::> Use this Option if you Want To use proxy with scan.
------------------
-v --version	::> Show Tool Version.
-e --examples	::> Show Tool Examples.

""",version="\n[+] Tool Version: 1.0")
#############


## Main Function :)

def Main():
  parse.add_option("-w","--website",dest="website",type="string")
  parse.add_option("-c","--source-code",dest="sourcecode",type="string")
  parse.add_option("-p","--use-proxy",action="store_true",dest="proxy",default=False)
  parse.add_option("-e","--examples",action="store_true",dest="examples",default=False)
  parse.add_option("-v",action="store_true",dest="ver",default=False)

  (options,args) = parse.parse_args()

# START :)
  def sourcecode():
   if options.sourcecode !=None:
    return True
   else:
    return False
  checksource = sourcecode()

  def checkproxy():
   if options.proxy:
    return True
   else:
    return False
  webproxy = checkproxy()
  if options.website !=None:
   if check() ==True:
 	 target = options.website
	 def checkwebsite():
 	  try:
             if target[:7]=="http://":
              host = socket.gethostbyname(target[7:])
             elif target[:8]=="https://":
              host = socket.gethostbyname(target[8:])
             else:
                host = socket.gethostbyname(target)
                conn = socket.create_connection((host, 80), 2)
                return True
          except:
               pass
          return False

	 if checkwebsite() !=True:
	  print(cor[3]+"\n[!]:Error:404: Server [ "+cor[4]+target+cor[3]+" ] Not Found!.")
          exit(1)
         try:
	  if webproxy == True:
	   prostatus = cor[2]+"ON"+cor[5]
	   proxy = proxyy
	  else:
	   prostatus = cor[4]+"OFF"+cor[5]
	   proxy = ""
	  if checksource == True:
	    pagecode = options.sourcecode
	    sources = ["php","asp","cfm","js","cgi"]
	    if pagecode in sources:
	     if pagecode ==sources[0]:
		links = open("Core/php.txt", "r")
		name = "Core/php.txt"
	     elif pagecode ==sources[1]:
		links = open("Core/asp.txt", "r")
		name = "Core/asp.txt"
	     elif pagecode ==sources[2]:
		links = open("Core/cfm.txt", "r")
		name = "Core*cfm.txt"
             elif pagecode ==sources[3]:
                links = open("Core/js.txt", "r")
		name = "Core/js.txt"
             elif pagecode ==sources[4]:
                links = open("Core/cgi.txt", "r")
		name = "Core/cgi.txt"
	    else:
		links = open("Core/all.txt", "r")
		name = "Core/all.txt"
	  else:
	     pagecode = "Not Selected"
	     links = open("Core/all.txt", "r")
	     name = "Core/all.txt"
	  print(cor[1]+banner)
	  sleep(1.5)
	  print(cor[2]+"\n[+]:=================> CONFIG <=================:[+]\n"+cor[5])
	  print("[#]:Start At         : [ "+str(timenow)+" ]")
	  print("[+]:Website          : [ "+str(target)+" ]")
	  print("[>]:Source Code      : [ "+str(pagecode)+" ]")
	  print("[>]:File	     : [ "+str(name))
	  print("[@]:Proxy status     : [ "+proxy+" ["+prostatus+"]")
	  print(cor[1]+"\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	  sleep(1.5)
	  print(cor[4] +"\n[$]"+cor[2]+" <<<<<<<<<"+cor[4]+" Finding Control Panel Start"+cor[2]+" >>>>>>>>>"+cor[4]+" [$]\n")
	  sleep(2)
	  rs = 1
	  rs2 = 1
	  a = 0
	  found = []
          while True:
	   link = links.readline()
	   if not link:
	    if a ==0:
		print(cor[2]+"[x]"+"="*6+cor[4]+" Result "+cor[2]+"="*6+"[x]\n")
		print(cor[3]+"[!]"+cor[5]+" I Was Scaning All Links From[ "+cor[1]+name+cor[5]+" ] File.")
		print(cor[3]+"[!]"+cor[5]+" Sorry I Can't Find Any Cp :(")
		print(cor[4]+"[@]"+cor[2]+"Shutdown At: "+cor[1]+str(timenow))
	    elif a > 0:
		print(cor[4]+"\n[*]"+"="*6+cor[2]+" Result "+cor[4]+"="*6+"[*]")
		print(cor[1]+"[*] CP Found= "+cor[2]+str(a))
		print("============ CP Table Found  =============\n")
		loop = 1
		for i in found:
		     print(cor[2]+"[CP"+cor[4]+"{}".format(loop)+cor[2]+">] "+cor[1]+i)
		     loop +=1
		print(cor[4]+"[@]"+cor[2]+"Shutdown At: "+cor[1]+str(timenow))
            break

	   if target[:7] == "http://":
	     request_link = target+"/"+link
	   elif target[:8] == "https://":
	     request_link ="http://"+target[8:]+"/"+link
	   else:
	     request_link = "http://"+target+"/"+link

	   print(cor[3] + '[!]:Trying Link[%s] : '%(rs2) +cor[0]+ str(request_link) +cor[5]+ "\n ==> "+cor[4]+"No")
	   rs2 += 1
	   REQUEST = Request(request_link)
	   try:
              if webproxy == True:
				 proxy = ProxyHandler({'http':proxyy})
				 opener = build_opener(proxy)
				 install_opener(opener)
				 url = "https://"+request_link[7:]
				 withproxy = Request(url)
				 response = urlopen(withproxy)
	      else:
		 response = urlopen(REQUEST)

	   except HTTPError as e:
				continue
	   except URLError as w:
			       continue
	   else:
	       print(cor[3] + '[!]:Trying Link[%s] : '%(rs2) +cor[0]+ str(request_link) +cor[5]+ "\n ==> "+cor[2]+"Yes")
	       print(cor[1]+"\n[+]"+cor[4]+":"+cor[2]+"CP"+cor[5]+"["+cor[0]+str(rs)+cor[5]+"]"+cor[4]+" Found!"+cor[1]+" ==> "+cor[2]+str(request_link))
	       rs +=1
	       a +=1
	       found.append(request_link)
	       ask = raw_input(cor[5]+"\n[?]:Do You Want Continue To Find Other Control Panel ? [Y:n]: "+cor[4])
	       if ask =="n" or ask =="N":
	         print(cor[4] + "\n[!]:"+cor[3]+"Stoping Scan.......")
		 sleep(2)
		 print("See You Later")
		 break
	       else:
		   pass
	       print("")
         except KeyboardInterrupt:
		print(" ")
		print(cor[4] + "\n[!]:"+cor[3]+"Stoping Scan.......")
		sleep(2)
		print("Bye")
		exit(1)
   elif check() == False:
	print(cor[3]+"\n[!]Ops:"+cor[5]+" Your Not Connected To The "+cor[4]+"[ Internet ]"+cor[2]+"\n[*]:"+cor[3]+"Please Connect To The Internet and try again :)")
	exit(1)

  elif options.examples:
	examples()

  elif options.ver:
	print("\n[+] Tool Version: 1.0")

  else:
	print(parse.usage)
	exit(1)
if __name__=="__main__":
	Main()

##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
