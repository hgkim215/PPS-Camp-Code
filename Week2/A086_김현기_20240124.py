'''
백준 1755 Silver

- 문자열, 정렬
'''
import sys
input = sys.stdin.readline

numDict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 0: 'zero'}

def numToEng(s) :
  engNum = ''
  for i in str(s) :
    engNum += numDict[int(i)]
  return engNum

M, N = map(int, input().split())

nums = list(range(M, N+1))
nums.sort(key=lambda x: numToEng(x))

for i in range(len(nums)) :
  if (i % 10 == 0 and i != 0) :
    print()
  print(nums[i], end=' ')
  
    