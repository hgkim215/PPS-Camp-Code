'''
Baekjoon Bronze 2953

- 사칙연산
'''

import sys
input = sys.stdin.readline

index = 0
max = 0
for i in range(5) :
  scores = input().split()
  total = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
  
  if (max < total) :
    max = total
    index = i+1
  elif (max == total) :
    index = -1
    

print(index, end=' ')
print(max)