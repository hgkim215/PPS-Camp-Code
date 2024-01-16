import sys
input = sys.stdin.readline

N = int(input())
answer = []
totalScore = 0
currentScore = 0

for _ in range(N) :
  result = input()
  for i in result :
    if (i == 'O') :
      currentScore += 1
      totalScore += currentScore
    else :
      currentScore = 0
  answer.append(totalScore)
  currentScore = 0
  totalScore = 0

for i in answer :
  print(i)