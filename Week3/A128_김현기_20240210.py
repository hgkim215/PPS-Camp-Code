'''
Baekjoon Silver 4949

- 문자열
'''
import sys
input = sys.stdin.readline

answer = []
while True :
    str = input().rstrip()
    stack = []

    if str == "." :
        break

    for i in str :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
              
    if len(stack) == 0 :
        answer.append('yes')
    else :
        answer.append('no')
  
for i in answer :
  print(i)