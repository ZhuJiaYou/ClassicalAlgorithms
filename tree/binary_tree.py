class BinaryNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preTraverse(root):
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def postTraverse(root):
    if root == None:
        return
    postTraverse(root.left)
    postTraverse(root.right)
    print(root.value)


if __name__ == '__main__':
    root = BinaryNode('a', BinaryNode('b', BinaryNode('c'), BinaryNode('d')), 
            BinaryNode('e', BinaryNode('f')))

    postTraverse(root)
