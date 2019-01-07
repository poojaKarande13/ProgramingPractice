# https://techdevguide.withgoogle.com/resources/compress-decompression/#!
# my implementation of google interview question compress and decompress
# using stack in python
q = list()

def emptyQueue():
    result = ''
    for x in q:
        result = result + x
    return result

def decompress(str):
    i = 0
    for c in str:
        if c == ']':
            # pop from queue and
            # form body
            body = ''
            c = q.pop()
            while c != '[':
                body = c + body
                c = q.pop()

            #form number
            num = ''
            c = q.pop()
            while c.isdigit() == True:
                num = c + num
                c = q.pop()

            q.append(c)
            num = int(num)
            result = ''
            for i in range(num):
                result = result + body
            q.append(result)
        else:
            q.append(c)

    return emptyQueue()

print(decompress('p2[o3[s]]ja3[b5[son]]'))
