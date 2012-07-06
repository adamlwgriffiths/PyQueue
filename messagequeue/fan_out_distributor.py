
class FanOutDistributor( object ):

    def __init__( self, queue ):
        super( FanOutDistributor, self ).__init__()

        self.queue = queue
        self.connections = []

    def distribute( self ):
        message = self.queue.pop()
        for connection in self.connections:
            connection.send( message )

    def run( self ):
        self.distribute()


if __name__ == '__main__':
    pass

