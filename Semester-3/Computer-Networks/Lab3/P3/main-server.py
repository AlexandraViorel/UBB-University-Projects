import socket
import select
import struct


def send_clients(clients):
    # we send the clients list to each client encoding the message as follows:
    # ip0,port0;ip1,port1;ip2,port2;...
    data_to_send = ''
    for info in clients.values():
        data_to_send += info[0]+','+str(info[1])+';'
    # we omit the last character, because we don't need the last ';'
    data_to_send = data_to_send[:-1]
    for client in clients:
        client.send(data_to_send.encode('ascii'))


# client communicates with server through TCP and clients between them through UDP
if __name__ == '__main__':
    # clients dictionary with socket descriptor as key and tuple (ip, port)
    clients = dict()
    # create server socket, bind and listen for incoming connections
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('172.30.113.175', 5555))
        server_socket.listen(5)
    except socket.error as e:
        print("Error: ", e.strerror)
        exit(-1)
    print("Listening for incoming connections!\n")

    read_socket = [server_socket]
    while True:
        ready_read, _, _ = select.select(read_socket, [], [])
        for s in ready_read:
            if s is server_socket:
                # we have a new client, so we accept and send the clients list to all the clients
                try:
                    client_socket, addr = s.accept()
                    print('New client from addr: ', addr)
                    client_udp_port = client_socket.recv(4)
                    client_udp_port = struct.unpack('!I', client_udp_port)[0]
                    clients[client_socket] = (addr[0], client_udp_port)
                    # we send the new clients list to all the clients
                    send_clients(clients)
                    read_socket.append(client_socket)
                except socket.error as e:
                    print("Error: ", e.strerror)
                    exit(-1)
            else:
                data = s.recv(512)
                data = data.decode('ascii').lower()
                if data == 'quit':
                    print("Client with addr: ", clients[s], " out!\n")
                    s.close()
                    clients.pop(s)
                    read_socket.remove(s)
                    send_clients(clients)

