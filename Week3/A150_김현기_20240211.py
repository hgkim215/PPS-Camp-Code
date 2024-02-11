'''
Baekjoon 1912 Silver
- 수학
'''

import sys
input = sys.stdin.readline

n = int(input())
m = list( map(int, input().split(' ')))
 
for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i-1])

print(max(m))

# N = int(input())

# dp = [0] * N
# nums = list(map(int, input().split()))

# max = -1001
# sum = 0
# prev = -1001
# for i in range(N) :
#   for j in range(i+1) :
#     dp[i] += nums[j]

# if min(dp) < 0 :
#   idx = dp.index(min(dp))
#   newDp = dp[idx:]

# newDp.sort()

# if (max(dp) < 0) :
#   print(max(dp))
# elif (newDp[-1] < newDp[-1]-newDp[0]) :
#   print(newDp[-1]-newDp[0])
# else :
#   print(newDp[-1])

  