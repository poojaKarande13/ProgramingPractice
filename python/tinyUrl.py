'''
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''
import string
import random

class Codec:

    def __init__(self):
        self.map = {}

    def generateCode(self):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))

    def encode(self, longUrl):
        code = self.generateCode()
        while code in self.map.keys():
            code = self.generateCode()
        self.map[code] = longUrl
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl):
        code = shortUrl.split("/")[-1]
        url = self.map[code]
        return url

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
