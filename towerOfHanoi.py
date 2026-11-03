def toh(n, source, auxiliary, destination):

    # Base case
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary
    toh(n-1, source, destination, auxiliary)

    # Move largest disk to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination
    toh(n-1, auxiliary, source, destination)


toh(3, 'A', 'B', 'C')

































#state space search 
from collections import deque

n = int(input("Enter number of disks: "))

start = (tuple(range(n, 0, -1)), (), ())
goal = ((), (), tuple(range(n, 0, -1)))

queue = deque([start])
visited = {start}
parent = {start: None}
move = {}

while queue:
    state = queue.popleft()

    if state == goal:
        break

    for i in range(3):
        for j in range(3):

            if i == j or not state[i]:
                continue

            pegs = [list(p) for p in state]
            disk = pegs[i][-1]

            if not pegs[j] or disk < pegs[j][-1]:

                pegs[i].pop()
                pegs[j].append(disk)

                new_state = tuple(tuple(p) for p in pegs)

                if new_state not in visited:
                    visited.add(new_state)
                    parent[new_state] = state
                    move[new_state] = (disk, i, j)
                    queue.append(new_state)

# Print solution
path = []
current = goal

while current != start:
    path.append(move[current])
    current = parent[current]

path.reverse()

names = ['A', 'B', 'C']

print("\nInitial State:", start)

for disk, i, j in path:
    print("Move disk", disk, "from", names[i], "to", names[j])

print("\nGoal State:", goal)
print("Total Moves:", len(path))