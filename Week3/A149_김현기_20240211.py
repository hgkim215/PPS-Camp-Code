'''
백준 실버 7568
'''

import sys
input = sys.stdin.readline

N = int(input())

level = []
infoList = []
for _ in range(N):
  info = tuple(map(int, input().split()))
  order = 1
  for i in range(len(level)) :
    if (info[0] > infoList[i][0] and info[1] > infoList[i][1]) : # 다른 신체보다 더 덩치가 클때
      level[i] += 1
    elif (info[0] < infoList[i][0] and info[1] < infoList[i][1]) : # 다른 신체보다 더 덩치가 작을 때
      order += 1
    
  level.append(order)
  infoList.append(info)

print(*level)