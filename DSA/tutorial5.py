# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    print(n1.data)
    linked_list = LinkedList()
    linked_list.head = n1
    n1.nextval = n2
    n2.nextval = n3
    n3.nextval = None

