'''
Baekjoon Bronze 11653

- 수학
'''
import sys
input = sys.stdin.readline

N = int(input())

answer = []
while N != 1 :
  for i in range(2, N+1) :
    if (N % i == 0) :
      N = int(N / i)
      answer.append(i)
      break

for i in answer :
  print(i)
    