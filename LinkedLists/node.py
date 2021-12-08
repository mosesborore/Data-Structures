
class Node:
    """ representation of the single node """
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self) -> str:
        return str(f'{self.data}')