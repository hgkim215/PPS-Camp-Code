'''
백준 1300 골드
- ??
'''
'''
        index1 index2 index3

index1    1       2      3

index2    2       4      6

index3    3       6      9

=> [0, 1, 2, 2, 3, 3, 4, 6, 6, 9]
'''

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 1, n**2
result = 0

if n**2 == k:
    print(k)
    # k가 n의 제곱이면 당연히 맨 끝자리 수이므로 k를 출력한다.
else:
    while(start < end):
        mid = (start+end)//2

        c = 0
        # mid보다 작거나 같은 숫자 계산
        for i in range(1,n+1):
            c += min(mid // i, n)
        
        if c >= k:
            end = mid
            result = mid
        elif c < k:
            start = mid+1
    print(result)