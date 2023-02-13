import socket
import threading
import struct
import time

my_lock = threading.Lock()
threads = []
client_count = 0

def worker(cs):
    global my_lock, client_count

    my_id = client_count
    print("client #", client_count, "from :", cs.getpeername(), cs)
    message = "Hello client #" + str(client_count)
    cs.sendall(bytes(message, 'ascii'))

    # receive number, example locking
    my_lock.acquire()
    n = cs.recv(2)
    n = struct.unpack("!H", n)[0]
    my_lock.release()

    # receive string
    my_stringR = cs.recv(1024)
    my_string = my_stringR.decode('ascii')

    # send number
    # Unlike send(), this method continues to send data from bytes until
    # either all data has been sent or an error occurs.
    cs.sendall(struct.pack("!H", n))

    #send string
    cs.send(bytes(my_string, 'ascii'))

    time.sleep(1)

    #close socket
    cs.close()
    print("Worker Thread ", my_id, " end!")
    exit(0)


if __name__ == '__main__':
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('ip', port))
        server_socket.listen(5)
    except socket.error as err:
        print("Error ", err.strerror)
        exit(-1)

    while True:
        client_socket, addr = server_socket.accept()
        t = threading.Thread(target=worker, args=(client_socket,))
        threads.append(t)
        client_count += 1
        t.start()

