"""
알고리즘
- 구현
- 자료 구조
- 시뮬레이션
- 큐
새로 배운 내용
enumerate() 내장함수
max() 함수의 key parameter의 사용법
"""

testcaseNum = int(input())
totalOrder = []

for _ in range(testcaseNum) :
  N, M = map(int, input().split())
  queue = list(map(int, input().split()))
  queue = list(enumerate(queue))
  # max(queue, key=lambda x:x[1])
  '''
  queue의 각 원소가 순서대로 lambda함수의 입력 x로 들어가고 x[0]은 각 원소 tuple의 
  첫번째 값을 의미하는 것이고 x[1]은 각원소 tuple의 2번째 값을 의미한다.
  결국, x[1]이 제일 큰 원소를 찾겠다' 라는 의미이다.
  '''
  # 1. 만약, 우선순위가 가장 높은 수가 아니라면 맨 뒤로 보내기.
  # 2. 우선순위가 가장 높은 수라면 pop해서 빼고 order + 1
  # 3. 만약, pop하는 수가 순서를 찾고자 하는 수와 동일하다면 order를 totalOrder에 넣고, break
  order = 0
  while True :
    if (queue[0][1] != max(queue, key=lambda x:x[1])[1]) : # 우선순위 가장 높은 수가 아니라면
      queue.append(queue.pop(0))
    else : # 우선순위가 가장 높은 수라면
      order += 1
      if (queue[0][0] == M) : # 찾고자 하는 수와 동일
        totalOrder.append(order)
        break
      queue.pop(0)
  
for order in totalOrder :
  print(order)
      
    
    
  

