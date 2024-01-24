'''
Baekjoon Silver 11656

- 정렬
'''

string = input()

answer = []

for i in range(len(string)) :
  answer.append(string[i:])
  
answer.sort()
for i in answer:
  print(i)
