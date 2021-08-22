class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def remove_node(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    def insert_node_to_mru_side(self, node):
        previous_node, next_node = self.right.prev, self.right
        previous_node.next = next_node.prev = node
        node.next, node.prev = next_node, previous_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache.get(key))
            self.insert_node_to_mru_side(self.cache.get(key))
            return self.cache.get(key).val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache.get(key))

        self.cache[key] = Node(key, value)
        self.insert_node_to_mru_side(self.cache.get(key))

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]



