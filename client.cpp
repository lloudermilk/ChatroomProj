#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <iostream>

using namespace std;

void error(const char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    
    //Message
    char msg[256];
    
    //Make sure user included the right command line args
    if (argc < 3) {
        cout << "usage: ./client [hostname] [port]\n";
        exit(0);
    }
    
    //Convert command line arg port number to int
    portno = atoi(argv[2]);
    
    //sockfd is the socket file descriptor that is returned from the socket()
    //call. The socket() args are socket(int domain, int type, int protocol)
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    //AF_INET is the address family, in this case IP
    //SOCK_STREAM is used for TCP connections (as opposed to UDP)
    //0 is used to declare what protocol to use with our address family
    //but there are no variations of protocol for our family
    
    if (sockfd < 0)
        error("ERROR opening socket");
    
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        cout << "ERROR, no such host\n";
        exit(0);
    }
    
    //bzero()sets the first n bytes of the area starting at s to zero
    bzero((char *) &serv_addr, sizeof(serv_addr));
    //sin_family is the same address family we used for socket()
    serv_addr.sin_family = AF_INET;
    //void bcopy(const void *src, void *dest, size_t n) copies n bytes from src to dest
    bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr, server->h_length);
    //sin_port is the port number
    //htons is host to network short. it converts a number into a 16-bit network representation.
    //This is commonly used to store a port number into a sockaddr structure.
    serv_addr.sin_port = htons(portno);
    
    if (connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0)
        error("ERROR connecting");
    
    cout << "Please enter the message: ";
    
    //make sure msg is empty
    bzero(msg,256);
    //char * fgets ( char * str, int num, FILE * stream );
    //reads chars from stream and stores as a C string into str until num-1 chars
    //have been read or a newline/end-of-file is reached, whichever happens first.
    fgets(msg,255,stdin);
    
    //Do the message writing
    n = write(sockfd,msg,strlen(msg));
    if (n < 0)
        error("ERROR writing to socket");
    bzero(msg,256);
    n = read(sockfd,msg,255);
    if (n < 0)
        error("ERROR reading from socket");
    cout << msg;
    
    close(sockfd);
    return 0;
}
