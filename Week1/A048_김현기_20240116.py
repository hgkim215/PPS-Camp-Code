'''
Baekjoon Silver 1316

- 문자열
'''

import sys
input = sys.stdin.readline

N = int(input())

answer = 0
for _ in range(N):
  word = input()
  isGroup = True
  prev = ''
  wordsDic = {}
  for w in word :
    if (wordsDic.get(w) == None) :
      wordsDic[w] = True
    else :
      if (w != prev) :
        isGroup = False
        break
    prev = w
  
  if(isGroup) :
    answer += 1

print(answer)