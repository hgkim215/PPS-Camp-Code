'''
Baekjoon Gold 5639

- 이진 검색 트리 (Binary Search Tree)
시간 복잡도: O(logN)
'''
'''
전위 순회: 루트 -> 왼쪽 -> 오른쪽
후위 순회: 왼쪽 -> 오른쪽 -> 루트

구현 방법
- 재귀 (더 선호되는 방법)
- 단순 구현

전위 순회한 결과가 입력으로 들어오므로, 
문제에서는 후위 순회한 결과를 출력하길 원하므로 재귀를 통해서 왼쪽 -> 오른쪽 -> 루트 순으로 찾아주면 된다.
'''

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

preorderList = []

while True:
  try :
    preorderList.append(int(input().rstrip()))
  except :
    break
  
def postorder(start, end) :
  if start > end :
    return
  
  # 리스트 내에 루트보다 큰 값이 없으면 전부 왼쪽 서브트리 취급
  right_start = end + 1
  
  for i in range(start + 1, end + 1) : # root 아래꺼부터
    if preorderList[start] < preorderList[i] : # 루트보다 더 큰 인덱스 (오른쪽 서브트리)
      right_start = i
      break
  
  # 루트 다음 인덱스부터 왼쪽 서브트리 탐색
  postorder(start+1, right_start-1)
  
  # 왼쪽 서브트리 탐색 끝나면 오른쪽 서브트리 탐색
  postorder(right_start, end)
  
  # 왼쪽, 오른쪽 서브트리 모두 탐색 끝났으므로 루트 출력
  print(preorderList[start])
  
postorder(0, len(preorderList)-1)
  
  
  
    