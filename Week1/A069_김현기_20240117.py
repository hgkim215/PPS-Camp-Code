'''
사용 알고리즘
- Queue

'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
result = []
nums = list(range(1,N+1))

currIndex = 0
while (len(nums) != 0) :
  currIndex += K-1
  length = len(nums)
  currIndex = currIndex % length  
  result.append(nums.pop(currIndex))
    
print("<", end="")
for i in result:
    print(i, end="")
    if i != result[-1]:
        print(", ", end="")
print(">") 