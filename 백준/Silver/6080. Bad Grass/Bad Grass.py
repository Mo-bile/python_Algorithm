def find_is_islands(grid, R, C):
    def iterative_dfs(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if grid[cx][cy] == 0:
                continue
            grid[cx][cy] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] > 0:
                    stack.append((nx, ny))

    island_count = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                iterative_dfs(i, j)
                island_count += 1

    return island_count

if __name__ == "__main__":
    R, C = map(int, input().split())

    grid = []

    for _ in range(R):
        grid.append(list(map(int, input().split())))

    result = find_is_islands(grid, R, C)

    print(result)
