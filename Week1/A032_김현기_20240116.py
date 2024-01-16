'''
Baekjoon Bronze 2775

- Dynamic Programming (Bottom-Up)
'''

import sys
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N) :
  k = int(input()) # k층
  n = int(input()) # n호
  floor0 = [x for x in range(1,n+1)]
  for i in range(k) : # 층수
    for j in range(1, n) : # 호실
      floor0[j] += floor0[j-1]
  answer.append(floor0[-1])
  
    
for i in answer :
  print(i)
