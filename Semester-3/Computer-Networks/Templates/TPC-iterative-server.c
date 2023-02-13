#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {

    int server_socket;
    struct sockaddr_in client, server;
    int cod;

    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        printf("Error on creating socket!\n");
        return 1;
    }

    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1500);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;

    cod = bind(server_socket, (struct sockaddr*)&server, sizeof(server));
    if (cod < 0) {
        printf("Bind error!\n");
        return 1;
    }

    listen(server_socket, 5);

    int l = sizeof(struct sockaddr_in);
    memset(&client, 0, sizeof(client));

    while (1) {
        int client_socket;

        client_socket = accept(server_socket, (struct sockaddr*)&client, &l);
        if (client_socket < 0) {
            printf("Accept error!\n");
            continue;
        }

        // receive/send data


        printf("Incomming connected client from: %s:%d\n", inet_ntoa(client.sin_addr), ntohs(client.sin_port));

        close(client_socket);
    }



    //
    close(server_socket);
    return 0;
}