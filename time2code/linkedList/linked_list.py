class Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.next = None
        
    def get_value(self):
        return self.value

class LinkedList:
    def __init__(self, node: Node):
        self.head = node
        self.tail = node
    
    # Return the string version of your linked list, for example, 1 -> 5 -> ...
    def __str__(self):
        cur = self.head
        linked_list = []
        
        while cur:
            linked_list.append(cur.get_value)
            cur = cur.next
        return ' -> '.join(linked_list)
        
    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail
        
    # Add a new node to tail with value
    def add(self, node: Node):
        self.tail.next = node
        self.tail = node
    
    def isEmpty(self):
        if not self.head:
            return True
        return False