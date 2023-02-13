import socket
import threading
import struct

def worker(cs):
    # receive number
    n = cs.recv(2)
    n = struct.unpack("!H", n)[0]

    # receive string
    my_string = cs.recv(1024).decode('ascii')

    # send number
    cs.send(struct.pack("!H", n))

    #send string
    cs.send(bytes(my_string, 'ascii'))

    #close socket
    cs.close()


if __name__ == "__main__":
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("192.254.160.0", 1234))
        server_socket.listen(5)
    except socket.error as err:
        print("Error: " + err.strerror)
        exit(-1)

    client_socket, addr = server_socket.accept()
    t = threading.Thread(target=worker, args=(client_socket,))
    t.start()
    #t.join()