#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#ifndef _WIN32
	#include <sys/types.h>
	#include <sys/socket.h>
	#include <netinet/in.h>
	#include <netinet/ip.h>
	#include <arpa/inet.h>
	#include <unistd.h> 
	#define closesocket close
typedef int SOCKET;
#else
	#define _WINSOCK_DEPRECATED_NO_WARNINGS
	#include<WinSock2.h>
	#include<cstdint>
	#include<wsipv6ok.h>
#endif




int main() {

	// create socket
#ifdef WIN32
	WSADATA wsaData;
	if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0) {
		perror("Error initializing the Windows Sockets Library");
		return -1;
	}
#endif

	int client_socket;
	struct sockaddr_in server;

	client_socket = socket(AF_INET, SOCK_STREAM, 0);
	if (client_socket < 0) {
		printf("Error on creating socket!\n");
		return 1;
	}

	// server addr

	memset(&server, 0, sizeof(server));
	server.sin_port = htons(1234);
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = inet_addr("ip");

	// connect

	if (connect(client_socket, (struct sockaddr*)&server, sizeof(server)) < 0) {
		printf("Error on connecting!\n");
		return 1;
	}

	// send/recv ex

	uint16_t a, b;
	int cod;
	a = 5;
	a = htons(a); // encode - host to network short
	cod = send(client_socket, (char*)& a, sizeof(a), 0);
	if (cod != sizeof(a)) {
		printf("Error on sending data to server!\n");
		return 1;
	}

	cod = recv(client_socket, (char*)& b, sizeof(b), 0);
	if (cod != sizeof(b)) {
		printf("Error on receiving data from server!\n");
		return 1;
	}

	b = ntohs(b); // decode - network to host short

	// if we want to send strings, we send strlen(s)+1

	// close socket

#ifdef WIN32
	WSACleanup();
	closesocket(client_socket);
#else
	close(client_socket);
#endif

	return 0;
}