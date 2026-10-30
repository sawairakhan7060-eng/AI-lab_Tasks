
# Weighted Graph
graph = {
    'S': [('A', 2), ('B', 3), ('C', 6)],
    'A': [('D', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 2)],
    'D': [('G', 6)],
    'E': [('G', 3)],
    'G': []
}

# Heuristic values
h = {
    'S': 9,
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 3,
    'G': 0
}


def search(start, goal, use_heuristic):

    queue = [(start, 0, [start])]
    best_cost = {start: 0}

    processed = []
    stale = 0

    while queue:

        # Find node with minimum priority
        current = min(
            queue,
            key=lambda x: x[1] + (h[x[0]] if use_heuristic else 0)
        )

        queue.remove(current)

        node, cost, path = current

        # Check stale entry
        if cost > best_cost[node]:
            stale += 1
            continue

        processed.append(node)

        if node == goal:
            return path, cost, processed, stale

        for neighbor, weight in graph[node]:

            new_cost = cost + weight

            if new_cost < best_cost.get(neighbor, float('inf')):

                best_cost[neighbor] = new_cost

                queue.append(
                    (neighbor, new_cost, path + [neighbor])
                )

    return None, float('inf'), processed, stale


# A* Search
print("===== A* SEARCH =====")

path, cost, processed, stale = search('S', 'G', True)

print("Path:", path)
print("Cost:", cost)
print("Processed Nodes:", processed)
print("Expansion Count:", len(processed))
print("Stale Entries:", stale)


# UCS Search
print("\n===== UCS SEARCH =====")

path, cost, processed, stale = search('S', 'G', False)

print("Path:", path)
print("Cost:", cost)
print("Processed Nodes:", processed)
print("Expansion Count:", len(processed))
print("Stale Entries:", stale)
