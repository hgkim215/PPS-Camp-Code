'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''
# import statistics
import sys
input=sys.stdin.readline
# 앞에 얘네들을 붙여주는 이유는 뭘까? https://www.acmicpc.net/problem/15552

N = int(input())
numbers = []
for _ in range(N) :
  numbers.append(int(input()))
  
# 산술평균
print(round(sum(numbers)/N))
# print(round(statistics.mean(numbers)))

# 중앙값
numbers.sort()
length = len(numbers)
if (length % 2 == 0) : # 짝수개
  print(round((numbers[N/2-1]+numbers[N])/2))
else : # 홀수개
  print(numbers[N//2])
# print(round(statistics.median(numbers)))

# 최빈값
numDic = {}
modeNums = []
for number in numbers :
  if (numDic.get(number) == None) : 
    numDic[number] = 1
  else :
    numDic[number] += 1
maxModeNum = max(numDic.values())
for number in numbers :
  if (numDic[number] == maxModeNum) :
    modeNums.append(number)
modeNums = set(modeNums)
modeNums = list(modeNums)
if (len(modeNums) == 1) :
  print(modeNums[0])
else :
  modeNums.sort()
  print(modeNums[1]) 
# print(statistics.mode(numbers))

# 범위
print(max(numbers) - min(numbers))
  