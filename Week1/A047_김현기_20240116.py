'''
Baekjoon Bronze 11721 
'''

import sys
input = sys.stdin.readline

word = input()

answer = []
count = 0
temp = ''
for w in word :
  count += 1
  temp += w
  if (count == 10) :
    answer.append(temp)
    temp = ''
    count = 0

if (temp != '') :
  answer.append(temp)

for i in answer :
  print(i)