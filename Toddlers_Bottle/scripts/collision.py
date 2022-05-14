from pwn import *

REMOTE_ADDRESS = "pwnable.kr"
REMOTE_PORT = 2222
REMOTE_USERNAME = "col"
REMOTE_PASSWORD = "guest"

shell = ssh(host = REMOTE_ADDRESS, port = REMOTE_PORT, user = REMOTE_USERNAME, password = REMOTE_PASSWORD)

shellcode = p32(0x1DD905E8) + p32(0x01010101) * 4
process = shell.process(["./col", shellcode])

flag = (process.recvline()).decode().strip()

shell.close()

print(f"Flag is: {flag}")