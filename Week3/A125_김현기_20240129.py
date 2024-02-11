'''
백준 2217 실버
- 수학
'''
import sys
input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N) :
  nums.append(int(input()))

nums.sort()

answer = []
for num in nums :
  answer.append(num * N)
  N -= 1

print(max(answer))