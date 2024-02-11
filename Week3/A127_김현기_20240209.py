'''
Baekjoon Bronze 1934

- 최소공배수
- 최대공약수
'''

import sys
input = sys.stdin.readline

N = int(input())

def gcd(a, b) :
  while b > 0 :
    a, b = b, a % b
  return a

def lcm(a, b) :
  return int((a * b) / gcd(a,b))

answer = []
for _ in range(N):
  num1, num2 = map(int, input().split())
  if (num1 >= num2) :
    answer.append(lcm(num1, num2))
  else :
    answer.append(lcm(num2, num1))

for i in answer :
  print(i)