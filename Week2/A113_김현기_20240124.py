'''
Baekjoon Silver 11724
- DFS BFS
'''
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

vertex, edge = map(int, input().split())

graph = [[False] * (vertex + 1) for _ in range(vertex + 1)]

#* 연결되어 있는 부분 graph에서 True로 표시하기
for _ in range(edge) :
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True

#* Vertex를 기준으로 방문한 Vertex이면 True
dfsVisited = [False] * (vertex+1)
bfsVisited = [False] * (vertex+1)

#* dfs (Depth-First-Search)
def dfs(v) :
  # 자기 자신 방문했기 때문에 True로 변경
  dfsVisited[v] = True
  # 현재 그래프에서 현재 vertex와 연결되어 있는 Node이지만, 아직 방문하지 않은 Vertex라면 방문해주기
  for i in range(1, vertex+1) :
    if (not dfsVisited[i] and graph[v][i]) :
      dfs(i)

#* bfs (Breadth-First-Search)
def bfs(v) :
  # bfs는 deque를 사용해서 queue에 인접 노드를 삽입해서 하나씩 뺴서 사용하는 방식을 이용한다.
  queue = deque([v])
  # 자기 자신을 방문했기 때문에 True로 변경한다
  bfsVisited[v] = True
  
  # queue가 모두 비어서 더이상 꺼내서 갈 vertex가 없을 때까지 반복한다
  while queue :
    v = queue.popleft()
    for i in range(1, vertex+1) :
      if (not bfsVisited[v] and graph[v][i]) :
        queue.append(i)
        bfsVisited[i] = True

answer = 0
for i in range(1, vertex+1) :
  if (not dfsVisited[i]) :
    answer += 1
    dfs(i)
    

print(answer)