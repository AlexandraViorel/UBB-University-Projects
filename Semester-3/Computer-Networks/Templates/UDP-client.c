#include <sys/socket.h>
#include <sys/types.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[]) {

    int client_socket;
    struct sockaddr_in server, from;
    struct hostent *h;
    char buffer[256];
    int cod;

    client_socket = socket(AF_INET, SOCK_DGRAM, 0);
    if (client_socket < 0) {
        printf("Error on creating socket!\n");
        return 1;
    }

    server.sin_port = htons(1234);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr("192.254.160.3");

    // OR
    h = gethostbyname(argv[1]);
    if (h == 0) {
        printf("Unknown host!\n");
        return 1;
    }

    server.sin_port = htons(atoi(argv[2]));
    server.sin_family = AF_INET;
    bcopy((char*) h->h_addr, (char*)&server.sin_addr, h->h_length);

    bzero(buffer, 256);
    printf("Give message:");
    fgets(buffer, 255, stdin);
    cod = sendto(client_socket, buffer, strlen(buffer), 0, (struct sockaddr*)&server, sizeof(server));
    if (cod < 0) {
        printf("Send error!\n");
        return 1;
    }

    cod = recvfrom(client_socket, buffer, 256, 0, (struct sockaddr*)&from, sizeof(from));
    if (cod < 0) {
        printf("Receive error!\n");
        return 1;
    }

    close(client_socket);

    return 0;

}