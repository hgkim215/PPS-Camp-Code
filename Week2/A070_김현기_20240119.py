'''
일반적인 사고로 문제를 풀면 시간초과가 걸린다. 그 이유는?

컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우, 
일반적인 list가 이러한 연산에 O(n)이 소요되는 데 반해, deque는 O(1)로 접근 가능하다.
'''

import sys
from collections import deque
input = sys.stdin.readline

nums = deque(range(1, int(input())+1))

while(True) :
  if (len(nums) == 1) :
    break
  nums.popleft()
  if (len(nums) == 1) :
    break
  nums.rotate(-1)

print(nums[0])