'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the minimum starting gas stations index if you can travel around the circuit once, otherwise return -1.
You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2..
Completing the circuit means starting at i and ending up at i again.
Example:
Input :
      Gas :   [1, 2]
      Cost :  [2, 1]

Output : 1

If you start from index 0, you can fill in gas[0] = 1 amount of gas. Now your tank has 1 unit of gas. But you need cost[0] = 2 gas to travel to station 1.
If you start from index 1, you can fill in gas[1] = 2 amount of gas. Now your tank has 2 units of gas. You need cost[1] = 1 gas to get to station 0. So, you travel to station 0 and still have 1 unit of gas left over. You fill in gas[0] = 1 unit of additional gas, making your current gas = 2. It costs you cost[0] = 2 to get to station 1, which you do and complete the circuit.

'''

def getNextIndex(i, N):
    if i+1 == N:
        return 0
    else:
        return i+1

def findMinGasStation(Gas, Cost):
    N = len(Gas)
    start = 0
    curr = 0
    next = getNextIndex(curr, N) # 1
    gasAvailable = Gas[curr] # 1
    count = 0
    while start != next and count <= N:
        if gasAvailable >= Cost[curr]: # 1 2
            gasAvailable = gasAvailable - Cost[curr] + Gas[next]
            curr = next
            next = getNextIndex(curr, N)
        else:
            gasAvailable = gasAvailable - Gas[start] # 0
            if start != curr:
                gasAvailable += Cost[start]
            else:
                curr = getNextIndex(start, N)
                next = getNextIndex(curr, N)
                gasAvailable += Gas[curr]
            count += 1
            start = getNextIndex(start, N)

    if next == start and gasAvailable >= Cost[curr]:
        return start

'''

def findMinGasStation(Gas, Cost):
    N = len(Gas)
    for i in range(N):
        gasAvailable = 0
        curr = i
        next = getNextIndex(curr, N)
        gasAvailable += Gas[curr]

        while next != i:
            if gasAvailable < Cost[curr]:
                break
            else:
                gasAvailable -= Cost[curr]
                curr = next
                next = getNextIndex(curr, N)
                gasAvailable += Gas[curr]

        if next == i and gasAvailable >= Cost[curr]:
            return i
''' # [0,1,2,3]
Gas = [1,3] #- fill
Cost= [2,2] #- need

print(findMinGasStation(Gas,Cost))
