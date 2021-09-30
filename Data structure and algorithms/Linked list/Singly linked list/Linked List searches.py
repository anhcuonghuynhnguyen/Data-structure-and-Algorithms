class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def Append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

        
    # This Function checks whether the value
    # x present in the linked list 
    def search(self, key):
        current = self.head
        # loop till current not equal to None
        while current:
            if current.data == key:
                return True # data found
            current = current.next
        
        return False # data not found

    # Checks whether the value key 
    # is present in linked list 
    def searchRecursive(self, lis, key):
          
        # Base case
        if(not lis):
            return False
          
        # If key is present in 
        # current node, return true
        if(lis.data == key):
            return True
          
        # Recur for remaining list
        return self.searchRecursive(lis.next, key)

# Code execution starts here
if __name__ == '__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    ''' Use push() to construct below list
        10->30->11->21->14'''
    llist.Append(10)
    llist.Append(30)
    llist.Append(11)
    llist.Append(21)
    llist.Append(14)
  
    print("Yes" if llist.search(21) else "No")
    print("Yes" if llist.search(100) else "No")

    print("Yes" if llist.searchRecursive(llist.head, 11) else "No")