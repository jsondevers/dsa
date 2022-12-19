from typing import List
from collections import deque


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adjacency_list = {}

        for start, end in edges:
            if start not in adjacency_list:
                adjacency_list[start] = []
            if end not in adjacency_list:
                adjacency_list[end] = []

            adjacency_list[start].append(end)
            adjacency_list[end].append(start)

        visited = [False] * n
        visited[source] = True
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for next_node in adjacency_list[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)

        return False
