'''
Baekjoon Bronze 3059
- 문자열
'''
import sys
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N) :
  data = input()
  alphaAscii = list(range(65, 91))
  for i in data :
    asciiData = ord(i)
    if (alphaAscii.count(asciiData) != 0) :
      alphaAscii.remove(asciiData)
  answer.append(sum(alphaAscii))

for i in answer :
  print(i)

