#Task 5:
import heapq
def dijkstra(graph, start):
    #Initialize distances with infinity
    distances = {node: float("inf") for node in graph}
    distances[start] = 0 #Distance to start is 0
    #Priority queue to pick the smallest distance node
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        #Skip if a better path already exists
        if current_distance > distances[current_node]:
            continue
        #Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            #If new shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
#Example graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}}
#Run Dijkstra starting from 'A'
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}:")
for node, dist in shortest_paths.items():
    print(f"{start_node} → {node}: {dist}")