
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        if hasattr(self, 'nickname'):
        	print self.nickname
        print "Got Message", data
        if data[0] == "\\":
			command = data.split(" ")
			print "Command entered", command[0]
			self.nickname = command[1]
        self.transport.write("You said " + data)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()