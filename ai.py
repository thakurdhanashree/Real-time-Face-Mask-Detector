def iddfs(graph, start, goal, max_depth, heuristic):
    for depth in range(max_depth + 1):
        visited = set()
        path = dfs(graph, start, goal, depth, visited, heuristic)
        if path:
            return path
    return None

def dfs(graph, current, goal, depth, visited, heuristic):
    if depth == 0:
        return None

    visited.add(current)

    if current == goal:
        return [current]

    min_next_h = float('inf')
    best_next_node = None

    for neighbor, cost in graph[current].items():
        if neighbor not in visited:
            h_value = heuristic[neighbor]
            if h_value < min_next_h:
                min_next_h = h_value
                best_next_node = neighbor

    if best_next_node:
        path = dfs(graph, best_next_node, goal, depth - 1, visited, heuristic)
        if path:
            return [current] + path

    return None

dict_hn = {
    'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

dict_gn = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Bucharest': {'Urziceni': 85, 'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu': 146},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Rimnicu': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Oradea': 71, 'Arad': 75}
}

start_city = 'Arad'
goal_city = 'Bucharest'
max_depth = 10

path = iddfs(dict_gn, start_city, goal_city, max_depth, dict_hn)

if path:
    print("Path found:", ' -> '.join(path))
else:
    print("Path not found within the specified depth.")