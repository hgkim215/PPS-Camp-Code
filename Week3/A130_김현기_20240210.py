'''
알고리즘
- 구현
- 자료 구조
- 스택
'''
N = int(input())
nums = []

for _ in range(N) :
  num = int(input())
  if (num != 0) :
    nums.append(num)
  else :
    nums.pop()

print(sum(nums))