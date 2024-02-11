'''
백준 실버 1002

- 수학
- 원의 방정식 사용하기
'''

'''
좌표 계산
(x,y) -> (a,b) = 루트((a-x)^2 + (b-y)^2) = r
r^2 = (a-x)^2 + (b-y)^2
'''

import sys, math
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  
  dist = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 두 원의 중점 사이의 거리 (좌표 간 거리)
  
  if dist == 0 and r1 == r2 : # 두 원이 동심원, 그리고 반지름이 같은 경우 (두 원이 동일함)
    answer.append(-1)
  elif abs(r1-r2) == dist or abs(r1+r2) == dist : # 두 원이 내접하거나 외접할 때 (한 점에서 만남)
    answer.append(1)
  elif abs(r1-r2) < dist < abs(r1+r2) : # 두 원이 서로 다른 두 점에서 만날 떄
    answer.append(2)
  else : 
    answer.append(0)

for i in range(N) :
  print(i)
    
  