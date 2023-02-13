import socket
import select
import struct

def send_clients(clients):
    data_to_send = ''
    for info in clients.values():
        data_to_send += info[0]+','+str(info[1])+';'
    data_to_send = data_to_send[:-1] #omits the last character
    for client in clients:
        client.send(data_to_send.encode('ascii'))

# client communicates with server through TCP and clients between them through UDP

if __name__ == '__main__':
    clients = dict()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('ip', port))
    server_socket.listen(5)

    read_socket = [server_socket]
    while True:
        ready_read, _, _ = select.select(read_socket, [], [])
        for s in ready_read:
            if s is server_socket:
                # we have a new client, so we accept and send the client list to all the clients
                client_socket, addr = s.accept()
                print('new client from addr: ', addr)
                client_udp_port = client_socket.recv(4)
                client_udp_port = struct.unpack('!I', client_udp_port)[0]
                clients[client_socket] = (addr[0], client_udp_port)
                send_clients(clients)
                read_socket.append(client_socket)
            else:
                data = s.recv(512)
                if not data or 'quit' in data.decode('ascii').lower():
                    s.close()
                    clients.pop(s)
                    read_socket.remove(s)
                    send_clients(clients)

