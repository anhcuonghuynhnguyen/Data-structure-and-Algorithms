
class Node:
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

        # Function to initialize head
        def __init__(self):
            self.head = None

            # This function is in LinkedList class. It inserts
            # a new node at the beginning of Linked List.

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



        # Returns data at given index in linked list
        def getNth(self, index):
            current = self.head # Initialise temp
            count = 0 # Index of current node

            # Loop while end of linked list is not reached
            while (current):
                if (count == index):
                    return print(count, " is ", current.data)
                count += 1
                current = current.next

            return print("The value of index isn't exist ")


        def getNthRecur(self, listt, position):
            # call recursive method
            llist.getNthNode(self.head, position, listt)

        # recursive method to find Nth Node
        def getNthNode(self, head, position, listt):
            count = 0  # initialize count
            if(head):
                if count == position:  # if count is equal to position,
                                    # it means we have found the position
                    print(head.data)
                else:
                    llist.getNthNode(head.next, position - 1, listt)
            else:  # if head doesn't exist we have
                # traversed the LinkedList
                print('Index Doesn\'t exist')
 
 


# Driver Code
if __name__ == '__main__':

    llist = LinkedList()
    llist.head = Node("Đầu tiên")

    # Use push() to construct below list
    # 1->12->1->4->1
    llist.Append("Thứ hai")
    llist.Append("Thứ ba")
    llist.Append("Thứ tư")
    llist.Append("Thứ năm")
    llist.Append("Thứ sáu")

    n = 4
    llist.getNth(n)
    print("Element at Index 3 is", end=" ")
    llist.getNthRecur(llist,3)
