# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
import collections
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def put(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if self.capacity <= len(self.cache):
                self.cache.popitem(last=False)
        self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Test Case
#["LRUCache","put","put","get","put","get","put","get","get","get"]
#[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
