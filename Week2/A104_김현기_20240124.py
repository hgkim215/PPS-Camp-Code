'''
Baekjoon Bronze 14487
- Greedy
'''

import sys
input = sys.stdin.readline

N = int(input())
cost = input().split()
cost = list(map(int, cost))

print(sum(cost) - max(cost))