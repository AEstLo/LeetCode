class HashMapLinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        # Our hash func will be a simple mod
        self.MAXVALUE = 10**4
        self.hashMap = [None] * self.MAXVALUE

    def getIndex(self, key):
        return key % self.MAXVALUE

    def put(self, key: int, value: int) -> None:
        index = self.getIndex(key)
        node = self.hashMap[index]
        if node is None:
            self.hashMap[index] = HashMapLinkedListNode(key, value)
            return
        while node.next:
            if node.key == key:
                node.val = value
                return
            node = node.next
        if node.key == key:
            node.val = value
        else:
            node.next = HashMapLinkedListNode(key, value)
        return

    def get(self, key: int) -> int:
        index = self.getIndex(key)
        node = self.hashMap[index]
        if node is None:
            return -1
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = self.getIndex(key)
        node = self.hashMap[index]
        if node is None:
            return
        prev = None
        while node:
            if node.key == key:
                if prev is None:
                    self.hashMap[index] = node.next
                else:
                    prev.next = node.next
                return
            prev = node
            node = node.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Runtime: 262 ms, faster than 87.21% of Python3 online submissions for Design HashMap.
# Memory Usage: 17.6 MB, less than 45.04% of Python3 online submissions for Design HashMap.
