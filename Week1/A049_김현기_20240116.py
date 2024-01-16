'''
Baekjoon Silver 4659

- 문자열
'''
import sys
input = sys.stdin.readline

answer = []

vowels = {'a', 'e', 'i', 'o', 'u'}
while True:
  pw = input().rstrip()
  if pw == 'end' :
    break
  
  standard1 = False # 모음이 하나도 없으면 False
  standard2 = True # 모음이 3개 혹은 자음이 3개 연속으로 오면 False
  standard3 = True # 같은 글자가 연속으로 2번 오면 False (ee, oo 제외)
  
  for i in range(0, len(pw)) :
    # Standard 3 확인
    if (i > 0) :
      if (pw[i] == pw[i-1] and pw[i] != 'e' and pw[i] != 'o') :
        standard3 = False
        break
    
    # Standard 1 확인
    if (pw[i] in vowels) :
      standard1 = True
      
    # Standard 2 확인
    if (i > 1) :
      if (pw[i] in vowels and pw[i-1] in vowels and pw[i-2] in vowels) :
        standard2 = False
      if (pw[i] not in vowels and pw[i-1] not in vowels and pw[i-2] not in vowels) :
        standard2 = False
    
  if (standard1 and standard2 and standard3) :
    answer.append("<"+pw+"> is acceptable.")
  else :
    answer.append("<"+pw+"> is not acceptable.")

for i in answer :
  print(i)