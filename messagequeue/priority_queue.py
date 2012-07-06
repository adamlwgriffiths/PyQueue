from Queue import PriorityQueue as pqueue

class PriorityQueue( object ):

    def __init__( self ):
        super( PriorityQueue, self ).__init__()

        self.messages = pqueue()

    def push( self, priority, message ):
        self.messages.put( (priority, message) )

    def pop( self ):
        while self.messages.empty() == False:
            yield self.messages.get()[ 1 ]


if __name__ == '__main__':
    import gevent
    msgq = PriorityQueue()

    def readFunc( queue ):
        for msg in msgq.pop():
            print msg,
        print 'done'

    msgq.push( 1, 1 )
    msgq.push( 6, 2 )
    msgq.push( 2, 3 )
    msgq.push( 5, 4 )
    msgq.push( 3, 5 )
    msgq.push( 4, 6 )

    greenlet = gevent.spawn( readFunc, msgq )
    greenlet.join()
