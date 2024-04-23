# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    d = [node.data]
    l = node.left
    r = node.right
    return d + pre_order(l) + pre_order(r)
# In-order traversal
def in_order(node):
    if not node:
        return []
    d = [node.data]
    l = node.left
    r = node.right
    return in_order(l) + d + in_order(r)

# Post-order traversal
def post_order(node):
    if not node:
        return []
    d = [node.data]
    l = node.left
    r = node.right
    return post_order(l) + post_order(r) + d
