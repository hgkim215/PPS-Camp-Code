import sys
input=sys.stdin.readline

N = int(input())
coordinates = []

for _ in range(N) :
  coordinate = list(map(int, input().split()))
  coordinates.append(coordinate)

coordinates.sort()
for coordinate in coordinates :
  print(coordinate[0], end=' ')
  print(coordinate[1])