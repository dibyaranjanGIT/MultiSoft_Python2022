"""
Binary Tree
-----------
In computer science, a binary tree is a data structure 
composed of nodes that have at most two children, referred to as the left and right child

"""
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

tree = BinaryTree()
tree.add_node(5)
tree.add_node(3)
tree.add_node(7)
tree.add_node(1)
tree.add_node(4)
tree.add_node(6)
tree.add_node(9)

"""   

        5
       / \
      3   7
     / \ / \
    1  4 6  9
    
"""