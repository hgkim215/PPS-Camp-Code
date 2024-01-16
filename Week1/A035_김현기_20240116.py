'''
Baekjoon Bronze 5355

- 수학
'''
import sys
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N) :
  nums = input().split()
  n = float(nums[0])
  for i in range(1, len(nums)) :
    if (nums[i] == '@') :
      n = n * 3
    elif (nums[i] == '%') :
      n = n + 5
    elif (nums[i] == '#') :
      n = n - 7
  answer.append(n)

for i in answer :
  print(format(i, ".2f"))