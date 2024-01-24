'''
Baekjoon Bronze 9546
- 수학
'''
import sys
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N):
  station = int(input())
  
  result = 0
  for i in range(1, station+1) :
    result = (result + 0.5) * 2
  
  answer.append(result)

for i in answer :
  print(int(i))