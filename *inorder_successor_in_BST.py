def inorderSucc(node):
    if not node:
        return None
    if node.right:
        return leftMostChild(node.right)
    else:
        tmp = node
        x = tmp.parent
        while x and x.left != tmp:
            tmp = x
            x = x.parent
        return x
def leftMostChilde(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node
