class BinaryNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_traverse(root):
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def pre_traverse_no_recur(root):
    if root == None:
        return
    rights = []

    pos = root
    while((pos != None) or (len(rights) > 0)):
        if pos == None:
            pos = rights.pop()
        else:
            print(pos.value)
            rights.append(pos.right)
            pos = pos.left



def post_traverse(root):
    if root == None:
        return
    postTraverse(root.left)
    postTraverse(root.right)
    print(root.value)


def mid_traverse(root):
    if root == None:
        return
    postTraverse(root.left)
    print(root.value)
    postTraverse(root.right)
    


if __name__ == '__main__':
    root = BinaryNode('a', BinaryNode('b', BinaryNode('c'), BinaryNode('d')), 
            BinaryNode('e', BinaryNode('f', None, BinaryNode('g'))))

    pre_traverse_no_recur(root)
