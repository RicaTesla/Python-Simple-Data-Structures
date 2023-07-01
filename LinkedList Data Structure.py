# Node class definition
class Node:
    def __init__(self, data=None):
        self.data= data
        self.next= None

# define linked list
class LinkedList:
    def __init__(self):
        self.head= None

    # insert node at the beginning of the linked list
    def insert_at_beginning(self,data):
        new_node= Node(data)
        new_node.next= self.head
        self.head= new_node
    # insert node at the beginning of Linked list
    def insert_at_end(self, data):
        new_node= Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current= current.next
            current.next= new_node

    # Deleting a node
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return


        current= self.head
        prev= None
        while current:
            if current.data == data:
                prev.next= current.next
                break
            prev= current
            current= current.next
        

    # searching a node
    def search(self, data):
        current= self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # Updating a node
    def update(self, data, new_data):
        current = self.head
        while current:
            if current.data == data:
                current.data = new_data
                break
            current = current.next

    # Traversing the linked list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Reversing the linked list
    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


linked_list = LinkedList()

# Initializing the linked list
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)
linked_list.insert_at_end(50)


print("Elements of the linked list:")
linked_list.traverse()


linked_list.insert_at_beginning(5)

linked_list.insert_at_end(60)


linked_list.delete(30)


search_value = 40
if linked_list.search(search_value):
    print(f"{search_value} found in the linked list.")
else:
    print(f"{search_value} not found in the linked list.")


linked_list.update(20, 25)


print("Elements of the linked list after modifications:")
linked_list.traverse()


linked_list.reverse()


print("Elements of the reversed linked list:")
linked_list.traverse()