from node import Node


class SinglyLinkedList:
    """ implementation of singly linkedlist """
    def __init__(self):
        self.head = None # start of the list
        self.tail = None # end of the list
    
    def is_empty(self) -> bool:
        """ checks if the linkedlist is empty"""
        return self.head is None
    
    def add(self, value):
        """ adds new value at the end of the linkedlist """
        new_node  = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def contains(self, value) -> Node:
        """ checks if @param value is in the list 
			returns: node whose data == value, else None
        """
        if self.is_empty():
            return None
        temp = self.head

        while temp is not None and temp.data != value:
            temp = temp.next
        
        if temp:
            return temp
        
        return temp
        
    
    def remove_with_value(self, value) -> bool:
        """ remove the @param value from the list \nreturns: True if @param value has been removed else False
        [cases from DSA book by Barnett, G. & Tongo, L., 2008 ]
        \ncases to account for:\n
        1. the list is empty; or
        2. the node to remove is the only node in the linked list; or
        3. we are removing the head node; or
        4. we are removing the tail node; or
        5. the node to remove is somewhere in between the head and tail; or
        6. the item to remove does not exist in the linked list
        """
        
        if self.is_empty():
            # case 1
            return False
        
        temp = self.head
        
        if temp.data == value:
            if self.head == self.tail:
                # case 2
                self.head = None
                self.tail = None
            else:
                # case 3
                self.head = self.head.next
            return True
        
        while temp.next is not None and temp.next.data != value:
            temp = temp.next
        
        if temp:
            if temp.next == self.tail:
                # case 4
                self.tail = temp
            
            # case 5 ; if case 4 was false
            temp.next = temp.next.next
            return True
        # case 6
        return False
    
    
    def reverse_traversal(self, head, tail):
        """ prints the list in reverse form @param head and tail belongs to the same list"""
        
        if tail is not None:
            current  = tail
            
            while current != head:
                previous = head
                
                while previous.next != current:
                    previous = previous.next
                
                print(current.data)
                current = previous
            print(current.data)
    
    
    def traverse(self):
        """ prints the each node value in the linkedlist"""
        if self.is_empty():
            print("List is empty")
            return
        
        temp = self.head
        
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
            
if __name__ == "__main__":
    s = SinglyLinkedList()
    
    data  = [1, 4, 3, 5, 20, 12, 80, 87]
    
    for i in data:
        s.add(i)
        
    s.traverse()
    s.remove_with_value(5)
    print("\nremoving...")
    s.traverse()
    print("\nreversing...")
    
    s.reverse_traversal(s.head, s.tail)
    
    print('\npresent:', s.contains(3))
