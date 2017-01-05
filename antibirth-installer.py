#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  antibirth-installer.py
#  
#  Copyright 2017 kirbylife <kirbylife>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import commands
import os

REBIRTHSIZE="2718736"
REBIRTHURL="~/.PlayOnLinux/wineprefix/Steam/drive_c/Program\ Files/Steam/steamapps/common/The\ Binding\ of\ Isaac\ Rebirth"
ANTIBIRTHURL="~/.PlayOnLinux/wineprefix/Steam/drive_c/Program\ Files/Steam/steamapps/common/The\ Binding\ of\ Isaac\ Rebirth/Antibirth"

def download():
	output=commands.getstatusoutput("cd "+ANTIBIRTHURL)[0]
	if(output==0):
		while True:
			print "Antibirth is already installed, do you want to reinstall it? (Y/N)"
			input=raw_input()
			if(input == "Y" or input == "y"):
				os.system("rm -R "+ANTIBIRTHURL)
				download()
			elif(input == "N" or input == "n"):
				print "Enjoy antibirth!!!!!!!"
				exit()
			else:
				print "Incorrect option. Please, try again"
	os.system("mkdir "+ANTIBIRTHURL)
	print "Downloading Antibirth (Can take several minutes)"
	output=commands.getstatusoutput("wget -c https://www.dropbox.com/s/qntzgggtax3pvg6/antibirth.rar -O "+ANTIBIRTHURL+"/.antibirth.rar")[0]
	if(output==32512):
		while True:
			print "wget isn't installed. Do you want me to install it for you? (Y/N)"
			input=raw_input()
			if(input == "Y" or input == "y"):
				installWget()
			elif(input == "N" or input == "n"):
				print "Install wget manually and try again"
				exit()
			else:
				print "Incorrect option. Please, try again"
	elif(output==1024):
		print "Error downloading Antibirth. Verify you internet conection or contact me (@kirbylife on twitter)"
		exit()
	elif(output==0):
		print "Download complete"
		print "Installing Antibirth"
		output=commands.getstatusoutput("cd "+ANTIBIRTHURL+" && unrar x .antibirth.rar")[0]
		if(output==1792):
			print "Error installing Antibirth. Please, try again"
			os.system("rm -R "+ANTIBIRTHURL)
			exit()
		elif(output==32512):
			while True:
				print "unrar isn't installed. Do you want me to install it for you? (Y/N)"
				input=raw_input()
				if(input == "Y" or input == "y"):
					installRar()
				elif(input == "N" or input == "n"):
					print "Install unrar manually and try again"
					exit()
				else:
					print "Incorrect option. Please, try again"
		else:
			files=split(commands.getstatusoutput("ls "+REBIRTHURL)[1],"\n")
			for c in files:
				if(c not in "Antibirth"):
					os.system("cp -R "+REBIRTHURL+"/"+c+" "+ANTIBIRTHURL)
			print "Antibirth it's al ready installed. Enjoy the game :D"
			os.system("rm "+ANTIBIRTHURL+"/.antibirth.rar")
			
	
def installWget():
	distro=commands.getoutput("lsb_release -s -i")
	command=""
	if(distro=="Fedora"):
		command="sudo dnf -y install wget"
	elif(distro=="Debian"):
		command="sudo apt-get install wget"
	
	if(command==""):
		print "you linux distribution '"+distro+"' is not supported at the moment. Install wget manually and try again"
	else:
		while True:
			print "I'm going to use '"+command+"', do you want to continue? (Y/N)"
			input=raw_input()
			if(input == "Y" or input == "y"):
				os.system(command)
				if(commands.getstatusoutput("wget")[0]==32512):
					print "The installation failed. Please, install wget manually and try again"
					exit()
				else:
					download()
			elif(input == "N" or input == "n"):
				print "Install wget manually and try again"
				exit()
			else:
				print "Incorrect option. Please, try again"

def installRar():
	distro=commands.getoutput("lsb_release -s -i")
	command=""
	if(distro=="Fedora"):
		command="sudo dnf -y install unrar"
	elif(distro=="Debian"):
		command="sudo apt-get install unrar"
	
	if(command==""):
		print "you linux distribution '"+distro+"' is not supported at the moment. Install rar manually and try again"
	else:
		while True:
			print "I'm going to use '"+command+"', do you want to continue? (Y/N)"
			input=raw_input()
			if(input == "Y" or input == "y"):
				os.system(command)
				if(commands.getstatusoutput("rar")[0]==32512):
					print "The installation failed. Please, install rar manually and try again"
					exit()
				else:
					download()
			elif(input == "N" or input == "n"):
				print "Install rar manually and try again"
				exit()
			else:
				print "Incorrect option. Please, try again"

def split(text,value):
	array=[]
	string=""
	c=""
	for c in text:
		if(c==value):
			array.append(string)
			string=""
		else:
			string=string+c
	array.append(string)
	return array

print "Welcome to the antibirth installation wizard - By Kirbylife"
print ""

output=commands.getstatusoutput("cd "+REBIRTHURL)[0]
if(output==256):
	print "Install The Binding of Isaac: Rebirth and try again"
	exit()

output=commands.getoutput("cd "+REBIRTHURL+" && wc -c isaac-ng.exe")
if(output[:output.find(" ")] not in REBIRTHSIZE):
	print "Uninstall Afterbirth and try again"
	exit()
else:
	download()
