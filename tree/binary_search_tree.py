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
            self.root = self.insert(self.root, value)

    def insert(self, root, value):
        if root == None:
            return BinarySearchNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        return root

    def mid_traverse(self, root):
        if root == None:
            return
        self.mid_traverse(root.left)
        print(root.value)
        self.mid_traverse(root.right)


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    root = BinarySearchTree(values)
    root.mid_traverse(root.root)

    
