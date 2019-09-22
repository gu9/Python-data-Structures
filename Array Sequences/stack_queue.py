from collections import deque

class Queue():

    '''
    Thread-safe, memory-efficient, maximally-sized queue supporting queueing and
    dequeueing in worst-case O(1) time.
    '''

    def __init__(self, max_size = 10):
        '''
        Initialize this queue to the empty queue.

        Parameters
        ----------
        max_size : int
            Maximum number of items contained in this queue. Defaults to 10.
        '''

        self._queue = deque(maxlen=max_size)

    def enqueue(self, item):

        '''
        Queues the passed item (i.e., pushes this item onto the tail of this
        queue).

        If this queue is already full, the item at the head of this queue
        is silently removed from this queue *before* the passed item is
        queued.
        '''

        self._queue.append(item)

    def enqueue_left(self, item):

        '''
        Queues the passed item (i.e., pushes this item onto the tail of this
        queue).

        If this queue is already full, the item at the head of this queue
        is silently removed from this queue *before* the passed item is
        queued.
        '''

        self._queue.appendleft(item)

    def dequeue(self):

        '''
        Dequeues (i.e., removes) the item at the head of this queue *and*
        returns this item.

        Raises
        ----------
        IndexError
            If this queue is empty.
        '''
        if not len(self._queue):
            print("List is empty")
        else:

            return self._queue.pop()

    def dequeue_left(self):

        '''
        Dequeues (i.e., removes) the item at the head of this queue *and*
        returns this item.

        Raises
        ----------
        IndexError
            If this queue is empty.
        '''
        if not len(self._queue):
            print("List is empty")
        else:

            return self._queue.popleft()

    def print_log(self):
        return list(self._queue)


if __name__ == "__main__":
    queue = Queue()
    # Adding elements
    queue.enqueue('First')
    queue.enqueue('Second')
    queue.enqueue('Third')
    print("All the elements:", queue.print_log())

    queue.dequeue() # Stack LIFO
    print("All the elements:", queue.print_log())
    queue.dequeue() # Stack LIFO

    # Now add elements in the front of the array
    # Implementation of Queue
    queue.enqueue_left("left_first")
    print("All the elements:", queue.print_log())
    # Removing
    queue.dequeue_left()
    print("All the elements:", queue.print_log())






