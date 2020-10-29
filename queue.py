"""
    TODOS:
        FUNCTIONS:
            enqueue
            dequeue
            is_empty
"""


class Queue:
    '''Queue data structure implementation'''

    def __init__(self, size=10):
        self.MAXSIZE = size
        # incremented/decremented when an item has been added/removed
        #
        self.curr_index = -1
        self.queue = [0 for _ in range(self.MAXSIZE)]

    def is_empty(self):
        return all(i == 0 for i in self.queue)

    def is_full(self):
        return self.curr_index == len(self.queue)-1

    def enqueue(self, val):
        ''' adds an item to the queue '''
        if type(val) != int:
            # integers only
            raise TypeError('integers only')
            return

        if self.is_full():
            print(f"the queue is full! {val} can't be added")
            return
        self.curr_index += 1
        self.queue[self.curr_index] = val

    def dequeue(self, num=1):
        ''' removes an item from the queue
            @params num: number of items to remove
        '''

        if num > 1:
            # removing multiple items
            del self.queue[:num]
            self.curr_index -= num

        self.curr_index -= 1
        del self.queue[0]

    def peekFront(self):
        ''' return the first item in the queue '''
        return self.queue[0]

    def peekBack(self):
        ''' return the last item in the queue '''
        if self.curr_index == -1:
            return "the queue is empty"

        return self.queue[self.curr_index]

    def __repr__(self):
        return repr(self.queue)


if __name__ == '__main__':
    q = Queue()

    for i in list(range(5)):
        q.enqueue(i)
    q.dequeue(num=3)
    print(q)
    print(q.curr_index)
    print(q.peekBack())
