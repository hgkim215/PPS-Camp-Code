word = input().upper()

alpha = {}

for i in word:
    if (alpha.get(i) == None):
        alpha[i] = 1
    else:
        alpha[i] += 1

most = list(alpha.values())
maxNum = max(most)

if (most.count(maxNum) >= 2):
    print("?")
else:
    for i in word:
        if (alpha[i] == maxNum):
            print(i)
            break
