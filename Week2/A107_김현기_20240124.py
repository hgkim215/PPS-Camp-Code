'''
Baekjoon Bronze 1292
- 수학
'''
import sys
input = sys.stdin.readline

numList = []

A, B = map(int, input().split())
for i in range(1, B+1) :
  for j in range(1, i+1) :
    numList.append(i)

answer = 0
for i in range(A, B+1) :
  answer += numList[i-1]

print(answer)