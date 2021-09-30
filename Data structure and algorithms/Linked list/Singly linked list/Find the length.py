class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node
    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        count = 0 # intinialise count
        current = self.head # intialise current
        # Loop while end of linked list is not reached
        while current:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    llist = LinkedList()
    llist.Push(1)
    llist.Push(3)
    llist.Push(1)
    llist.Push(2)
    llist.Push(1)

    print("Count of nodes is :", llist.getCount())