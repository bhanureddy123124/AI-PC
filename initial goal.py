import heapq

class Node:
    def _init_(self, state, g, h, parent=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
    
    def _lt_(self, other):
        return self.f < other.f

def A_star_search(graph, start, end):
    start_node = Node(start, 0, graph[start][end])
    end_node = Node(end, 0, 0)
    
    open_list = []
    heapq.heappush(open_list, start_node)
    
    closed_list = set()
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.state)
        
        for neighbor, cost in graph[current_node.state].items():
            if neighbor in closed_list:
                continue
            
            g = current_node.g + cost
            h = graph[neighbor][end]
            f = g + h
            
            neighbor_node = Node(neighbor, g, h, current_node)
            
            if any(neighbor_node.state == open_node.state for open_node in open_list):
                for open_node in open_list:
                    if neighbor_node.state == open_node.state and neighbor_node.f < open_node.f:
                        open_node.g = g
                        open_node.h = h
                        open_node.f = f
                        open_node.parent = current_node
            else:
                heapq.heappush(open_list, neighbor_node)
                
    return None

graph = {'A': {'B': 1, 'C': 4, 'D': 10},
         'B': {'E': 3},
         'C': {'D': 4, 'F': 2},
         'D': {'E': 1},
         'E': {},
         'F': {'E': 5}}

start = 'A'
end = 'E'

path = A_star_search(graph, start, end)

if path is None:
    print("No path found")
else:
    print("Path:", path)
