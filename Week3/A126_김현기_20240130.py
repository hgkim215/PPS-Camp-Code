'''
Baekjoon 1065 Silver

- 브루트포스
'''
import sys
input = sys.stdin.readline

N = int(input())

hansu = 0
for i in range(1, N+1) :
  if (i < 100) :
    hansu += 1
  elif (i > 100) :
    first = int(str(i)[1]) - int(str(i)[0])
    second = int(str(i)[2]) - int(str(i)[1])
    if (first - second == 0) :
      hansu += 1

print(hansu)
    