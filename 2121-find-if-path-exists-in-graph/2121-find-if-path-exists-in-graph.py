class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination : return True
        # 2. DFS 사용
        def dfs(graph, start_node, end_node):

            stack = deque()
            visited = set()
            
            stack.append(start_node)
            visited.add(start_node)
            
            while stack:
                node = stack.pop()
                for val in graph[node]:
                    if val in visited:
                        continue

                    if val == end_node:
                        return True
                    stack.append(val)
                    visited.add(val)

            return False

        # 1. 인접리스트 만들기
        adj_list = {i : [] for i in range(n)}
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        print(adj_list)
        return dfs(adj_list, source, destination)

        # 3. 방문기록

        # 4. 종료조건