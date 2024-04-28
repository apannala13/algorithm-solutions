import heapq  #minheap

def dijkstra(graph, start):
    #priority_queue to hold nodes and current shortest distance
    priority_queue = []
    
    #keep track of min distance to each node
    min_distances = {node:float('inf') for node in graph}
    
    #keep track of visited nodes
    visited = set()
    
    #set initial nodes distance to 0 and push to queue
    min_distances[start] = 0
    heapq.heappush(priority_queue, (0, start))
    
    
    while priority_queue:
        #get node with smallest distance
        cur_distance, cur_node = heapq.heappop(priority_queue)
        
        #if node has been visited, skip it
        if cur_node in visited:
            continue 
        
        #mark node as visited
        visited.add(cur_node)
        
        #check all adjacent nodes
        for neighbor, weight in graph[cur_node].items():
            if neighbor in visited: #skip
                continue 
            
            #calculate new distance to neighboring node
            new_distance = cur_distance + weight 
            
            #if found shorter path to neighbor, update and push to queue
            if new_distance < min_distances[neighbor]:
                min_distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    return min_distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
distances = dijkstra(graph, 'A')
print(distances)
