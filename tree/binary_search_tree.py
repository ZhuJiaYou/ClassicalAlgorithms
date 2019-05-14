import random


class BinarySearchNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, values=None):
        self.root = None
        random.shuffle(values)
        for value in values:
            self.insert(value)

    def insert(root, value):
        if root == None:
            return BinarySearchNode(value)
        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)
        return root

if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5]
    BinarySearchTree(nodes)
    
