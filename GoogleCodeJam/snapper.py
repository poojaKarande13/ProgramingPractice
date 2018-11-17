# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
# if i == 0 then toggle
# if s[i] == 0 and s[i-1] == 0 then s[i] = 0
# if s[i] == 0 and s[i-1] == 1 then s[i] = 0
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    res = 1
    for _ in range(n):
        res =  res * 2

    if (m+1) % res == 0:
        print("Case #{}: {}".format(i, "ON"))
    else:
        print("Case #{}: {}".format(i, "OFF"))
  # check out .format's specification for more formatting options
