'''
Baekjoon Bronze 5598

- 문자열
'''

import sys
input = sys.stdin.readline

word = input()

answer = ''
for w in word :
  temp = ord(w) - 3
  if (temp < 65) :
    temp = 90 - (65 - temp) + 1
  if (chr(temp) != '!') :
    answer += chr(temp)

print(answer)
