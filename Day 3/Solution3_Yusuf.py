a = [3, 4, -1, 1]
a = [1, 2, 0]
#Solution 1
for i in range(1,len(a)+1):
    if i not in a:
        print(i)
        break

b=(n**2 for n in range(12))

#Solution 2
next(i for i in range(1,len(a)+1) if i not in a)
