import collections

def bfs(r, c):
    q = collections.deque()
    visited.add((r,c))
    q.append((r, c))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while q:
        row, col = q.popleft()

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if(r in range(rows) and
            c in range(cols) and
            grid[r][c] == 1 and
            (r, c) not in visited):
                q.append((r, c))
                visited.add((r, c))


grid = [[1, 1, 1, 0, 1],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0]]

if not grid:
    print("no islands")

rows, cols = len(grid), len(grid[0])
visited = set()
islands = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1 and (r, c) not in visited:
            bfs(r, c)
            islands += 1
print(islands)