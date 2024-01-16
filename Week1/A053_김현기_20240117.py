'''
사용 알고리즘
- 스택 (파이썬에서는 Stack이 따로 없다)
'''
import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = []
for _ in range(N):
  cmd = input().split()
  
  if (cmd[0] == 'push') :
    stack.append(int(cmd[1]))
  elif (cmd[0] == 'pop') :
    if (len(stack) == 0) :
      answer.append(-1)
    else :
      answer.append(stack.pop(-1))
  elif (cmd[0] == 'size') :
    answer.append(len(stack))
  elif (cmd[0] == 'empty') :
    if (len(stack) == 0) :
      answer.append(1)
    else :
      answer.append(0)
  elif (cmd[0] == 'top') :
    if (len(stack) == 0) :
      answer.append(-1)
    else :
      answer.append(stack[-1])

for i in answer :
  print(i)

