#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int client_socket;

int tratare() {

    if (client_socket < 0) {
        printf("Error on accepting client!\n");
        exit(1);
    }

    // send/receive data

    close(client_socket);
    exit(0);

}

int main() {

    int server_socket;
    struct sockaddr_in server, client;
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

    while (1) {

        int l = sizeof(client);
        memset(&client, 0, sizeof(client));

        client_socket = accept(server_socket, (struct sockaddr*)&client, &l);
        if (client_socket < 0) {
            printf("Accept error!\n");
            continue;
        }

        if (fork() == 0) {
            tratare();
        }


    }

    return 0;
}