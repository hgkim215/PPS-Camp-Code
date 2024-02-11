'''
백준 실버 1543
- 문자열 리스트
'''

import sys
input = sys.stdin.readline

word = input().rstrip('\n')
search = input().rstrip('\n')

answer = 0
while True:
  temp = word
  word = word.replace(search, ' ', 1)
  if (word != temp) :
    answer += 1
  else :
    break

print(answer)
