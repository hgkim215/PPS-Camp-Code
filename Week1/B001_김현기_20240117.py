'''
Baekjoon Silver 2606

- DFS, BFS
'''
from collections import deque
import sys
input = sys.stdin.readline

vertex = int(input()) # 컴퓨터 수
edge = int(input()) # 직접 연결되어있는 컴퓨터 쌍의 수

# index 0은 사용하지 않음 (vertex + 1 사용)
graph = [[False] * (vertex + 1) for _ in range(vertex + 1)]

for _ in range(edge) :
  N, M = map(int, input().split())
  graph[N][M] = True
  graph[M][N] = True

# 설정된 그래프에서 방문한 곳을 True로 설정
dfsVisited = [False] * (vertex + 1)
bfsVisited = [False] * (vertex + 1)

# Depth-First-Search (재귀)
def dfs(V) :
  dfsVisited[V] = True
  for i in range(1, vertex+1) :
    if not dfsVisited[i] and graph[V][i] :
      dfs(i)

# Breadth-First-Search (deque)
def bfs(V) :
  queue = deque([V])
  bfsVisited[V] = True # 시작 노드 방문 처리
  
  # queue 내부가 완전히 빌때까지 반복
  while queue :
    V = queue.popleft() # Queue에 삽입된 순서대로 노드 하나씩 꺼내기
    for i in range(1, vertex+1) : # 현재 처리 중인 노드 중에서 방문하지 않은 인접 노드들을 Queue에 삽입
      if not bfsVisited[i] and graph[V][i] :
        queue.append(i)
        bfsVisited[i] = True
  
dfs(1)
print(dfsVisited.count(True) - 1)
  