'''
Baekjoon Bronze 5622

- 구현
'''
import sys
input = sys.stdin.readline

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()

answer = 0
for i in word :
  for j in range(0, len(dial)) :
    if (i in dial[j]) :
      answer += (j + 3)

print(answer)