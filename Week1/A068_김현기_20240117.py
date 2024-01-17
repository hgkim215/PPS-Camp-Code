'''
Baekjoon Silver 18258

- Queue
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

queue = deque([])
answer = []
for _ in range(N):
  cmd = input().split()
  if (cmd[0] == 'push') :
    queue.append(int(cmd[1]))
  elif (cmd[0] == 'pop') :
    if (len(queue) == 0) :
      answer.append(-1)
    else :
      answer.append(queue.popleft())
  elif (cmd[0] == 'size') :
    answer.append(len(queue))
  elif (cmd[0] == 'empty') :
    if (len(queue) == 0) :
      answer.append(1)
    else :
      answer.append(0)
  elif (cmd[0] == 'front') :
    if (len(queue) == 0) :
      answer.append(-1)
    else :
      answer.append(queue[0])
  elif (cmd[0] == 'back') :
    if (len(queue) == 0) :
      answer.append(-1)
    else :
      answer.append(queue[-1])

for i in answer :
  print(i)