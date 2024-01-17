'''
Baekjoon Silver 1427

- 정렬
'''
import sys
input = sys.stdin.readline

num = input()
num = sorted(num, reverse=True)

for i in range(0, len(num)-1) :
  print(num[i], end='')