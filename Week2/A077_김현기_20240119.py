'''
BaekJoon Silver 2822

- 정렬
'''

import sys
input = sys.stdin.readline

scoreList = []
for i in range(8) :
  scoreList.append(int(input()))

index = []
total = 0
for i in range(5) :
  total += max(scoreList)
  index.append(scoreList.index(max(scoreList))+1)
  scoreList[scoreList.index(max(scoreList))] = -1

index.sort()
print(total)
print(*index)