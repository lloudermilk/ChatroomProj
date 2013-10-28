server: server.out 
	./server.out 4000 

client: client.out
	./client.out localhost 4000

all: server.out client.out

server.out: server.cpp
	g++ server.cpp -o server.out

client.out: client.cpp
	g++ client.cpp -o client.out
