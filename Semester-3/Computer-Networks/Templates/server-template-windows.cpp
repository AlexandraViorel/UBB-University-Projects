#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#ifndef _WIN32
	#include <sys/types.h>
	#include <sys/socket.h>
	#include <netinet/in.h>
	#include <netinet/ip.h>
	#include <unistd.h>
	#include <errno.h>
	#include <arpa/inet.h>
	#include <unistd.h> 
	#define closesocket close
	typedef int SOCKET;
#else
	#define _WINSOCK_DEPRECATED_NO_WARNINGS
	#include<WinSock2.h>
	#include<stdint.h>
	#include<wsipv6ok.h>
	typedef int socklen_t;
#endif

int main() {

	int server_socket;
	struct sockaddr_in client, server;
	int cod;

	// create socket

	server_socket = socket(AF_INET, SOCK_STREAM, 0);
	if (server_socket < 0) {
		printf("Error on creating socket!\n");
		return 1;
	}

	// server address

	memset(&server, 0, sizeof(server));
	server.sin_port = htons(1500);
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;

	// bind

	cod = bind(server_socket, (struct sockaddr*)&server, sizeof(server));
	if (cod < 0) {
		printf("Bind error!\n");
		return 1;
	}

	// listen

	listen(server_socket, 5);

	// client addr

	int l = sizeof(struct sockaddr_in);
	memset(&client, 0, sizeof(client));

	while (1) {
		int client_socket = accept(server_socket, (struct sockaddr*)&client, (socklen_t*)&l);
		int err = errno;
#ifdef WIN32
		err = WSAGetLastError();
#endif
		if (client_socket < 0) {
			printf("Accept error: %d", err);
			continue;
		}

		printf("Incomming connected client from: %s:%d\n", inet_ntoa(client.sin_addr), ntohs(client.sin_port));

		closesocket(client_socket);

	}
#ifdef WIN32
	WSACleanup();
#endif

	return 0;
}