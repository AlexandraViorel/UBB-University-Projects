#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {

    int client_socket;
    struct sockaddr_in server;
    int cod;

    // create the socket

    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket < 0) {
        printf("Error on creating client socket!\n");
        return 1;
    }

    // set the server address

    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1500);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr("192.124.32.1"); // se pune ip ul luat cu ifconfig

    // connect

    cod = connect(client_socket, (struct sockaddr*)&server, sizeof(server));
    if (cod < 0) {
        printf("Error on connecting to server!\n");
        return 1;
    }

    // send/receive data example - integers

    uint16_t a, b;
    a = 5;
    a = htons(a); // encode - host to network short
    cod = send(client_socket, &a, sizeof(a), 0);
    if (cod != sizeof(a)) {
        printf("Error on sending data to server!\n");
        return 1;
    }

    cod = recv(client_socket, &b, sizeof(b), 0);
    if (cod != sizeof(b)) {
        printf("Error on receiving data from server!\n");
        return 1;
    }

    b = ntohs(b); // decode - network to host short

    // if we want to send strings, we send strlen(s)+1

    // close the socket

    close(client_socket);

    return 0;
}