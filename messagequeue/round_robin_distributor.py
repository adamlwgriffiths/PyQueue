
class RoundRobinDistributor( object ):

    def __init__( self, queue ):
        super( RoundRobinDistributor, self ).__init__()

        self.queue = queue
        self.connections = []
        self.next_connection = 0

    def distribute( self ):
        message = self.queue.pop()

        if self.next_connection > len( self.connections ):
            self.next_connection= 0

        connection = self.connections[ self.next_connection ]

        connection.send( message )

    def run( self ):
        self.distribute()


if __name__ == '__main__':
    pass

