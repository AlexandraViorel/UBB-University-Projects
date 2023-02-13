import socket
import struct
import threading
import sys

peers = []
lock = threading.Lock()

def read_message_from_client(cs):
    while True:
        message, addr = cs.recvfrom(256)
        print("message from ", addr, ": ", message.decode('ascii'))

def read_user_message_and_send(ps):
    global peers, lock
    while True:
        message = input("give message: ")
        lock.acquire()
        for peer in peers:
            print(peer)
            ps.sendto(message.encode('ascii'), peer)
        lock.release()

if __name__ == '__main__':

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('ip', port))

    client_port = int(sys.argv[1])
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    peer_socket.bind(('ip', client_port))

    peer_thread = threading.Thread(target=read_message_from_client, args=(peer_socket,))
    user_thread = threading.Thread(target=read_user_message_and_send, args=(peer_socket,))
    peer_thread.start()
    user_thread.start()

    server_socket.send(struct.pack("!I", client_port))

    while True:
        peers_list = server_socket.recv(512).decode('ascii')
        # ip,port;ip,port...
        print("received new peer list: ", peers_list)
        lock.acquire()
        peers.clear()
        clients = peers_list.split(';')
        for client in clients:
            client_info = client.split(',')
            ip = client_info[0].rstrip()
            port = int(client_info[1])
            print('peer: ', ip, port)
            peers.append((ip, port))
        lock.release()