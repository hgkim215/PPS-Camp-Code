'''
Baekjoon Silver 9095

- DP
'''
'''
1 --> 1
2 --> 2
3 --> 4
1 1 1
1 2
2 1
3
4 --> 7
1 1 1 1
1 1 2
1 2 1
2 1 1
1 3
3 1
2 2
5 --> 13
1 1 1 1 1
1 1 1 2 
1 1 2 1
1 2 1 1
2 1 1 1
1 1 3 
1 3 1
3 1 1
1 2 2
2 1 2
2 2 1
2 3 
3 2
'''
import sys
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N):
  num = int(input())
  dp = [0] * (num + 1)
  
  for i in range(1, num+1) :
    if i == 1 :
      dp[i] = 1
    elif i == 2:
      dp[i] = 2
    elif i == 3:
      dp[i] = 4
    else :
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  
  answer.append(dp[num])

for i in answer :
  print(i)