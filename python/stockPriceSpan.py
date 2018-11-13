class Stack:
    def __init__(self):
        self.stack = []

    def push(self,elem):
         self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peak(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

def stockPriceSpan(stockPrices):
    s = Stack()
    print(stockPrices[0])
    s.push(0)
    span = [0] * len(stockPrices)

    span[0] = 1
    for i in range(1, len(stockPrices)):
        count = 1
        while stockPrices[s.peak()] <= stockPrices[i] and s.isEmpty() == False:
            print("pop", s.pop())

        span[i] = i if s.isEmpty() else (i - s.peak())
        s.push(i)
    print(span)

stockPriceSpan([100, 80, 60, 70, 60, 75, 85])
