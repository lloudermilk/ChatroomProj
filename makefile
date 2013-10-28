server: server.out 
	./server.out 4000 

client: client.out
	./client.out localhost 4000

all: server.out client.out

server.out:
	g++ server.cpp -o server.out

client.out:
	g++ client.cpp -o client.out
