numlist = []
for i in range(1001):
    if i%3 == 0 or i%5 == 0:
        numlist.append(i)

print(sum(numlist))
