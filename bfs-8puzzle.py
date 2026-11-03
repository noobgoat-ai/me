
from collections import deque

# Initial and goal states
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# BFS
queue = deque([start])
visited = {start}
parent = {start: None}

while queue:

    state = queue.popleft()

    # Check goal
    if state == goal:
        break

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    # Possible movements
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with adjacent tile
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = state
                queue.append(new_state)

# Print solution path
if state == goal:

    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    print("Solution found!")
    print("Total steps:", len(path) - 1)

    for s in path:
        for i in range(0, 9, 3):
            print(s[i:i+3])
        print()

else:
    print("No solution found")
