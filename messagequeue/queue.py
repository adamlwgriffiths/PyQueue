from collections import deque

class Queue( object ):

    def __init__( self ):
        super( Queue, self ).__init__()

        self.messages = deque()

    def push( self, message ):
        self.messages.append( message )

    def pop( self ):
        while len( self.messages ) > 0:
            yield self.messages.popleft()


if __name__ == '__main__':
    import gevent
    msgq = Queue()

    def readFunc( queue ):
        for msg in msgq.pop():
            print msg,
        print 'done'

    msgq.push( 1 )
    msgq.push( 2 )
    msgq.push( 3 )
    msgq.push( 4 )
    msgq.push( 5 )
    msgq.push( 6 )

    greenlet = gevent.spawn( readFunc, msgq )
    greenlet.join()
