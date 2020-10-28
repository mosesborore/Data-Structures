'''
    Stack data structure implementation
    TODOS:
        Functions:
            push
            popitem
            peak
            is_empty
'''


class Stack:
    def __init__(self, size=10):
        self.top = -1
        self.MAXSIZE = size
        self.stack = [0 for _ in range(self.MAXSIZE)]

    def is_empty(self):
        return self.top < 0

    def push(self, val):
        '''
            adds item to the stack
        '''
        if self.top >= len(self.stack)-1:
            print(f"Stack overflow! {val} can't be added")
            return
        self.top += 1
        self.stack[self.top] = val

    def popitem(self, start=None):
        """
            @param start: index where to reach while removing items
                          e.g. start=5 => pops item starting from the end upto index 5
                           index 4 becomes the new {self.top} value

        """
        if self.is_empty():
            print("Stack is empty! Add some data")
            return

        if start is not None:
            # if you want to remove multiple items at once
            indices = list(range(start, len(self.stack)))[::-1]
            for i in indices:
                index = self.top
                self.top -= 1
                del self.stack[index]
            return

        # normal popping of an item
        index = self.top
        self.top -= 1
        del self.stack[index]

    def peak(self):
        """
            return the top item of the stack
        """
        return self.stack[self.top]

    def __repr__(self):
        return repr(self.stack)


if __name__ == "__main__":
    #s = Stack(size=20)
    s = Stack()

    data = list(range(10))

    # push data into the stack
    for i in data:
        s.push(i)
    # print(s.is_empty())
    print(s)
    print("Peak values:", s.peak())
    # s.popitem(start=7)
    s.popitem(start=0)
    print(s.top)
    print(s)
