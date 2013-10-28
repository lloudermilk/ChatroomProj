#  CS450 - OPERATING SYSTEMS
#  CHAT PROJECT - PHASE 1
#  Monday, October 28, 2013

#  Team Members:  Eric Wooley, Lauryn Loudermilk, David Wells, Tandra Felly


from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print "Got Message", data
        self.transport.write("You said" + data)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()