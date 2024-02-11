# Binary Search (이분 탐색)

# K: 현재 가지고 있는 랜선 수
# N: 최대길이로 만들고 싶은 랜선 수
K, N = map(int, input().split())

# lans: 현재 가지고 있는 랜선들의 길이에 대한 리스트
lans = []

for i in range(K):
    lan = int(input())
    lans.append(lan)

# Binary Search
# start: 제일 짧은 길이, end: 가지고 있는 랜선 중 가장 긴 길이
start, end = 1, max(lans)

while start <= end:
    # mid: 만들고 싶은 랜선의 길이
    mid = (start+end) // 2
    lines = 0

    # 가지고 있는 랜선들 돌면서 mid로 나눴을 때 총 몇 개로 나눠지는지 계산
    for i in lans:
        lines += i // mid

    # 만약 만들고 싶은 수 이상으로 만들어진다면 랜선 길이를 더 길게하기
    # Binary Search 방식으로
    if lines >= N:
        start = mid + 1
    # 만약 N만큼 만들어지지 않았다면, 랜선 길이를 더 짧게하기
    else:
        end = mid - 1

# start보다 end가 더 짧아졌음
print(end)
