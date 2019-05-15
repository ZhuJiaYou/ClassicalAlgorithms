import random


class BinarySearchNode():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree():
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

    def query(self, root, val):
        if root == None:
            return False
        if root.value == val:
            return True
        elif val < root.value:
            return self.query(root.left, val)
        else:
            return self.query(root.right, val)

    def find_min(self, root):
        if root.left == None:
            return root
        else:
            return self.find_min(root.left)
        
    def find_max(self, root):
        if root.right == None:
            return root
        else:
            return self.find_max(root.right)





if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    bst = BinarySearchTree(values)
    print(bst.find_max(bst.root).value)

    
