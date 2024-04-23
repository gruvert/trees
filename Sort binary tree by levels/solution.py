class Nodel:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def add(self, item):
        if self.head is None:
            self.tail = Nodel(item)
            self.head = self.tail
        else:
            self.tail.next = Nodel(item)
            self.tail = self.tail.next
    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.head.item
def tree_by_levels(node):
    if not node:
        return []
    stk = Queue()
    res = [node.value]
    stk.add(node.left)
    stk.add(node.right)
    while not stk.is_empty():
        see = stk.pop()
        if see.data is None:
            continue
        if see.data:
            res.append(see.data.value)
        if see.data.left:
            stk.add(see.data.left)
        if see.data.right:
            stk.add(see.data.right)
    return res
