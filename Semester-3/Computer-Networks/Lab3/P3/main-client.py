import socket
import struct
import threading
import sys

peers = []
my_lock = threading.Lock()
finished = False
peer_socket = 0


def read_messages_from_client(cs):
    global my_lock, finished
    if finished:
        my_lock.acquire()
        finished = False
        exit(0)
        my_lock.release()
    else:
        while True:
            message, addr = cs.recvfrom(256)
            print("Message from peer with address ", addr, ": ", message.decode('ascii'), '\n')


def read_user_message_and_send(ps, ss):
    global peers, my_lock, finished, peer_socket
    while True:
        message = input()
        my_lock.acquire()
        if message.lower() != 'quit':
            for peer in peers:
                print("sending to peer: ", peer)
                ps.sendto(message.encode('ascii'), peer)
        else:
            for peer in peers:
                if peer != peer_socket:
                    print("sending to peer: ", peer)
                    ps.sendto(message.encode('ascii'), peer)
        my_lock.release()
        my_lock.acquire()
        if message.lower() == 'quit':
            print("Goodbye!\n")
            ss.send(message.encode('ascii'))
            ps.close()
            ss.close()
            finished = True
            exit(0)
        my_lock.release()


if __name__ == '__main__':

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect(('172.30.113.175', 5555))
    except socket.error as e:
        print("Error: ", e.strerror)
        exit(-1)

    try:
        client_port = int(sys.argv[1])
        peer_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        peer_socket.bind(('172.30.113.175', client_port))
    except socket.error as e:
        print("Error: ", e.strerror)
        exit(-1)

    peer_thread = threading.Thread(target=read_messages_from_client, args=(peer_socket,))
    user_thread = threading.Thread(target=read_user_message_and_send, args=(peer_socket, server_socket))
    peer_thread.start()
    user_thread.start()

    server_socket.send(struct.pack("!I", client_port))

    while True:
        peers_list = server_socket.recv(512).decode('ascii')
        # ip,port;ip,port...
        if peers_list == '':
            exit(0)
        print("received new peer list: ", peers_list, '\n')
        my_lock.acquire()
        peers.clear()
        clients = peers_list.split(';')
        for client in clients:
            client_info = client.split(',')
            ip = client_info[0].rstrip()
            port = int(client_info[1])
            print('peer: ', ip, port)
            peers.append((ip, port))
        my_lock.release()
