'''
Baekjoon Silver 10867

- 정렬
'''
import sys
input = sys.stdin.readline

N = int(input())

nums = input().split()
nums = list(map(int, nums))
nums = set(nums)
nums = list(nums)
nums.sort()

print(*nums)