'''
Baekjoon Silver 1431

- 정렬

arr.sort(key = lambda x : (정렬기준1, 정렬기준2, 정렬기준3, …))
'''

import sys
input = sys.stdin.readline

def checkSum(s) :
  result = 0
  for i in s :
    if i.isdigit() :
      result += int(i)
  return result

N = int(input())

answer = []
for _ in range(N):
  serial = input().rstrip()
  answer.append(serial)

answer.sort(key=lambda x : (len(x), checkSum(x), x))

for i in answer :
  print(i)