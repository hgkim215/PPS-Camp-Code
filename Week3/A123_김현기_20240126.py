'''
백준 1463 실버
- 다이나믹 프로그래밍
'''

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 1000001

# bottom-up
for i in range(2, N+1) :
  # 1 빼는 경우
  dp[i] = dp[i-1] + 1
  
  # 2로 나누어 떨어지는 경우
  if i % 2 == 0 :
    dp[i] = min(dp[i], dp[i//2] + 1)
  
  # 3으로 나누어 떨어지는 경우
  if i % 3 == 0 :
    dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])
