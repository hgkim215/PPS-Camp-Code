'''
백준 1439 실버
- 그리디
'''

import sys
input = sys.stdin.readline

num = input().rstrip()


prev = num[0]
result = [prev]
if len(num) != 1 :
  for i in range(1, len(num)) :
    if (num[i] != prev) :
      result.append(num[i])
    prev = num[i]

count0 = 0
count1 = 0
for i in result :
  if (i == '0') :
    count0 += 1
  else :
    count1 += 1

if (len(num) == 1) :
  print(0)
elif count0 >= count1 :
  print(count1)
else :
  print(count0)
