import socket
import struct

"""
! - from or to network
c - char
h - short
H - unsigned short
i - int
I - unsigned int
q - long long
Q - unsigned long long
f - float
d - double
"""

# create socket & connect
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.254.160.0", 1234))
except socket.error as err:
    print("Error: " + err.strerror)
    exit(-1)

# send number
a = int(input("a="))
res = client_socket.send(struct.pack("!H", a))

# receive number
c = client_socket.recv(2)
c = struct.unpack("!H", c)[0]

# send string
string = input("string=")
client_socket.send(bytes(string, 'ascii'))

# receive string
string = client_socket.recv(1024).decode('ascii')

# close socket

client_socket.close()
