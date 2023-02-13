import socket
import struct
import threading

def worker(s):
    # receive number
    n, addr = s.recvfrom(2)
    n = struct.unpack("!H", n1)[0]

    # send number
    res = s.sendto(struct.pack("!H", n), addr) # !!!! SEND TO ADDR, PORT IS DIFFERENT

    # close socket
    s.close()


if __name__ == "__main__":
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(("ip addr", port))
        print("Waiting for client!")
    except socket.error as err:
        print("Error: " + err.strerror)
        exit(-1)

    t = threading.Thread(target=worker, args=(server_socket,))
    t.start()
    t.join()