def pre_order(node):
    if node is None:
        return []
    if node.right is None and node.left is None:
        return [node.data]
    elif node.right is None:
        return [node.data]+pre_order(node.left)
    elif node.left is None:
        return [node.data]+pre_order(node.right)
    else:
        return [node.data]+pre_order(node.left)+pre_order(node.right)
def in_order(node):
    if node is None:
        return []
    if node.right is None and node.left is None:
        return [node.data]
    elif node.right is None:
        return in_order(node.left)+[node.data]
    elif node.left is None:
        return [node.data]+in_order(node.right)
    else:
        return in_order(node.left)+[node.data]+in_order(node.right)
def post_order(node):
    if node is None:
        return []
    if node.right is None and node.left is None:
        return [node.data]
    elif node.right is None:
        return post_order(node.left)+[node.data]
    elif node.left is None:
        return post_order(node.right)+[node.data]
    else:
        return post_order(node.left)+post_order(node.right)+[node.data]
