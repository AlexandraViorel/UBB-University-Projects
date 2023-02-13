import socket
import struct

# create socket
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err:
    print("Error: " + err.strerror)
    exit(-1)

# NO CONNECT

# send number
a = int(input("a="))
res = client_socket.sendto(struct.pack("!H", a), ("ip addr", port))

#receive number
n, addr = client_socket.recvfrom(2)
n = struct.unpack("!H", n)[0]

# close socket
client_socket.close()