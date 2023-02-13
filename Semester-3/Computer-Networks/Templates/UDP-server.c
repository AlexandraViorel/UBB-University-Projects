#include <netinet/in.h>
#include <stdio.h>
#include <strings.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
    int server_socket;
    struct sockaddr_in server, from;
    int cod;
    char buffer[1024];

    server_socket = socket(AF_INET, SOCK_DGRAM, 0);
    if (server_socket < 0) {
        printf("Error on creating socket!\n");
        return 1;
    }

    bzero(&server, sizeof(server));
    server.sin_family = AF_INET;
    server.sin_port = htons(atoi(argv[1]));
    server.sin_addr.s_addr = INADDR_ANY;

    cod = bind(server_socket, (struct sockaddr*)&server, sizeof(server));
    if (cod < 0) {
        printf("Bind error!\n");
        return 1;
    }

    // receive/send a string

    while (1) {
        cod = recvfrom(server_socket, buffer, 1024, 0, (struct sockaddr*)&from, sizeof(from));
        if (cod < 0) {
            printf("Receive error!\n");
            continue;
        }

        cod = sendto(server_socket, buffer, sizeof(buffer), 0, (struct sockaddr*)&from, sizeof(from));
        if (cod < 0) {
            printf("Send error!\n");
            continue;
        }
    }

    close(server_socket);



    return 0;
}