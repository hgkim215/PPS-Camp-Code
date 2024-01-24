'''
Baekjoon Bronze 3062
- 수학
'''
import sys
input = sys.stdin.readline

def checkPalindrome(num) :
  if (num == num[::-1]) :
    return "YES"
  else :
    return "NO"
N = int(input())

answer = []
for _ in range(N):
  num = input()
  reverseNum = num[::-1]
  result = int(num) + int(reverseNum)
  answer.append(checkPalindrome(str(result)))

for i in answer :
  print(i)