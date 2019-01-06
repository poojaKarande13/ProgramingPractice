class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        ptr = self.root
        length = len(word)
        for index in range(length):
            loc = ord(word[index]) - ord('a')
            if ptr.children[loc] == None:
                ptr.children[loc] = TrieNode()
            ptr = ptr.children[loc]
        ptr.isEndOfWord = True

    def search(self, word):
        ptr = self.root
        length = len(word)
        for index in range(length):
            loc = ord(word[index]) - ord('a')
            if ptr.children[loc] == None:
                return False
            ptr = ptr.children[loc]
        if ptr.isEndOfWord == True:
             return True
        return False

    def startsWith(self, prefix):
        ptr = self.root
        length = len(prefix)
        for index in range(length):
            loc = ord(prefix[index]) - ord('a')
            if ptr.children[loc] == None:
                return False
            ptr = ptr.children[loc]
        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
print(obj.search("wor"))
print(obj.startsWith("wkr"))
