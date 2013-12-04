#  CS450 - OPERATING SYSTEMS
#  CHAT PROJECT - PHASE 1
#  Monday, October 28, 2013
#  Team Members:  Eric Wooley, Lauryn Loudermilk, David Wells, Tandra Felly

from twisted.internet import reactor, protocol
# a client protocol
class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    
    def connectionMade(self):
        print "You are logged in as 'Anonymous'. To change your nickname use '\\nick [new nickname]'\n"
        self.transport.write("Connection established")
        
    def dataReceived(self, data):
        message = raw_input("Message: ")
        if message != "exit":
        	self.transport.write(message)
        else: 
        	print "exiting..."
        	self.transport.loseConnection()
    
    def connectionLost(self, reason):
        print "connection lost"

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()

# this connects the protocol to a server runing on port 8000
def main():
	
	f = EchoFactory()
	reactor.connectTCP("localhost", 8000, f)
	reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()