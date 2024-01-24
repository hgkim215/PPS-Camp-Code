'''
Baekjoon 5585 Bronze
- 그리디 알고리즘
'''
import sys
input = sys.stdin.readline

change = [500, 100, 50, 10, 5, 1]

cost = 1000 - int(input())

answer = 0
for i in change:
  while (cost >= i) :
    cost -= i
    answer += 1

print(answer)