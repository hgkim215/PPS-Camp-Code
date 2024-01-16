'''
Baekjoon Bronze 3052

- 사칙연산
'''

import sys
input = sys.stdin.readline

answer = []
for _ in range(10) :
  num = int(input())
  result = num % 42
  answer.append(result)

answer = set(answer)
print(len(answer))