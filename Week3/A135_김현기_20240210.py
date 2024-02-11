'''
Baekjoon Silver 1302
-문자열
-해쉬맵
'''

import sys
input = sys.stdin.readline

N = int(input())

result = {}
for _ in range(N):
  book = input().rstrip()
  if (result.get(book) == None) :
    result[book] = 1
  else :
    result[book] += 1

sortedResult = sorted(result.items(), key=lambda x: x[1], reverse=True)
max = sortedResult[0][1]
answer = []
for result in sortedResult :
  if result[1] == max :
    answer.append(result[0])

answer.sort()
print(answer[0])