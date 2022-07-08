class LinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def toString(self):
        node = self.head
        ret = []
        while node:
            ret.append(f'({node.key}, {node.val})')
            node = node.next
        return '->'.join(ret) + (f'(head -> {self.head.val}, tail -> {self.tail.val})')

    def addFirst(self, key, val):
        new_node = LinkedListNode(key, val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def moveToBeginning(self, node):
        if not node.prev:
            # The node is already the head
            return
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        if next_node:
            next_node.prev = prev
        else:
            # I was the tail so the tail needs to be updated
            self.tail = prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def removeLast(self):
        if not self.tail:
            return None
        removed_val = self.tail.key
        if self.tail == self.head:
            self.head = self.tail = None
            return removed_val
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail.prev = None
        self.tail = new_tail
        return removed_val


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = LinkedList()
        self.keys = {}

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        self.cache.moveToBeginning(self.keys[key])
        return self.keys[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.cache.addFirst(key, value)
            self.keys[key] = self.cache.head
            while self.capacity < len(self.keys):
                removed_val = self.cache.removeLast()
                del self.keys[removed_val]
        else:
            node = self.keys[key]
            if node.val != value:
                node.val = value
            self.cache.moveToBeginning(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
