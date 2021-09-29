#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None        

#Linked list class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None

    def PrintList(self):
        count = self.head
        while count:
            print(count.data)
            count = count.next

    # Function to insert a new node at the beginning
    def Push(self, new_data):

        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)

        # 3. Make next of new node
        new_node.next = self.head

        #4. Move the head to point to new node
        self.head = new_node

    # Inserts a new node after the given prev_node. This method is
    # defined inside LinkedList class shown above 
    def InsertAfter(self, prev_node, new_data):
        
        #1. check if the given previos node exists
        if prev_node is None:
            print("The given previous node must in LinkedList")
            return
        
        # 2 & 3: Create new node & Put in the data
        new_node = Node(new_data)

        # 4. Make next of new node
        new_node.next = prev_node.next

        # 5. Make next of prev_node 
        prev_node.next = new_node

    # Append a new node at the end. This method is
    # defined inside LinkedList
    def Append(self, new_data):

        # 1. Create new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked list is empty, 
        # then make a new node is head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the end last node
        last = self.head
        while last.next:
            last = last.next
        
        # 6. Change the next of last node
        last.next = new_node



# Code execution starts here
if __name__=='__main__':
    llist = LinkedList()

    llist.head = Node("Thứ nhất")
    second =Node("Thứ hai")
    third = Node("Thứ ba")

    llist.head.next = second
    second.next = third

    llist.Push("Add heading")
    llist.InsertAfter(second, "Sáng thứ hai")
    llist.Append("Cuối cùng")

    llist.PrintList()


