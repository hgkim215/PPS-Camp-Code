N = int(input())
members = []

for _ in range(N) :
  age, name = map(str, input().split())
  member = [int(age), name]
  members.append(member)

members.sort(key=lambda x: x[0])

for member in members:
  print(member[0], end=" ")
  print(member[1])