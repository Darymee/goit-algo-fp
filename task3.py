import heapq

class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj = [[] for _ in range(num_vertices)] 

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def dijkstra(self, start):
        distances = [float('inf')] * self.V
        distances[start] = 0

        # Кожен елемент у купі: (відстань, вершина)
        heap = [(0, start)]
        visited = [False] * self.V

        while heap:
            current_dist, u = heapq.heappop(heap)

            if visited[u]:
                continue
            visited[u] = True

            for neighbor, weight in self.adj[u]:
                if not visited[neighbor]:
                    new_dist = current_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))

        return distances

g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 1, 4)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 7)
g.add_edge(4, 3, 9)

start_vertex = 0
shortest_paths = g.dijkstra(start_vertex)

for i, dist in enumerate(shortest_paths):
    print(f"Відстань від вершини {start_vertex} до вершини {i} = {dist}")
