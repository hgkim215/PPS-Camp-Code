'''
Baekjoon Silver 1260

- 깊이 우선 탐색 (DFS: Depth-First-Search)
- 너비 우선 탐색 (BFS: Breadth-First-Search)
'''
'''
DFS는 재귀로 구현하는 게 일반적. BFS는 Queue로 구현하는 게 일반적.
1) 입력받은 노드의 개수 만큼 2차원 리스트를 구현해 False로 초기화 한 후 연결되었다면 True로 변경해주는 방법
2) 정점만 입력 받아서 정점만 찾아나가는 방식 (낮은 숫자부터라면 정렬 과정이 필요)
'''
'''
- DFS 개념
그림: https://developer-mac.tistory.com/64
Root Node나 다른 임의 Node에서 다음 Branch로 넘어가기 전, 해당하는 Branch의 모든 Node를 완벽하게 탐색하는 방법이다.
  - 시간 복잡도 (V: Vertex, E: Edge)
    인접리스트: O(V+E)
    인접 행렬: O(V^2)
  - 구현
    스택, 재귀 (주로 재귀로 구현)

- BFS 개념
참고: https://heytech.tistory.com/56 
그림: https://developer-mac.tistory.com/64
Root Node나 다른 임의 Node에서 Branch 상관없이 인접한 Node를 먼저 탐색하는 방법이다.
  - 시간 복잡도
    인접리스트: O(V+E)
    인접 행렬: O(V^2)
  - 구현
    Queue(Deque)
'''

import sys
input = sys.stdin.readline
from collections import deque

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
N, M ,V = map(int, input().split())

# Graph의 연결되어있는 정점들 정보
# N + 1인 이유는 index 0을 사용하지 않기 위함이다.
graph = [[False] * (N + 1) for _ in range(N + 1)]

# M개의 줄에는 간선이 연결하는 두 정점의 번호 (양방향)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 설정된 그래프에서 방문한 곳을 True로 설정
dfsVisited = [False] * (N + 1)
bfsVisited = [False] * (N + 1)

# 재귀
def dfs(V) :
  dfsVisited[V] = True
  print(V, end=" ")
  for i in range(1, N + 1) :
    if not dfsVisited[i] and graph[V][i] :
      dfs(i) # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)
  
# deque
def bfs(V) :
  q = deque([V]) # List 보다 pop 메서드의 시간복잡도가 더 낮은 deque 구조 사용
  bfsVisited[V] = True 
  while q : # q가 empty가 될 때까지 반복
    V = q.popleft() # queue의 첫 번째 값
    print(V, end=' ')
    for i in range(1, N+1) : # index 0은 패스
      if not bfsVisited[i] and graph[V][i] :
        q.append(i)
        bfsVisited[i] = True

dfs(V)
print()
bfs(V)