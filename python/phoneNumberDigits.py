def addWordAndLoop(pos, mappedDigits, word, result):
    if len(mappedDigits) <= pos:
        result.append(word)
        return

    for letter in mappedDigits[pos]:
        addWordAndLoop(pos+1, mappedDigits, word + letter, result)


def letterCombinations(digits):
    digitWordMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    mappedDigits = []
    for d in digits:
        mappedDigits.append(digitWordMap[d])

    result = []
    addWordAndLoop(0, mappedDigits, "", result)

    print(result)

letterCombinations("99")
