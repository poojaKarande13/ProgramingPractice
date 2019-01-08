# https://techdevguide.withgoogle.com/resources/pairs-problem-classic-algorithm-hard/#!

# Given an array of non-empty strings, create and return a Map<String, String> as follows: for each string add its first character as a key with its last character as the value.

# pairs(["code", "bug"])  {"b": "g", "c": "e"}
# pairs(["man", "moon", "main"])  {"m": "n"}
# pairs(["man", "moon", "good", "night"])  {"g": "d", "m": "n", "n": "t"}

def pairs(pair):
    map = {}
    for elem in pair:
        map[elem[0]] = elem[-1]
    return map

print(pairs(["code", "bug"]))
print(pairs(["man", "moon", "main"]))
print(pairs(["man", "moon", "good", "night"]))
