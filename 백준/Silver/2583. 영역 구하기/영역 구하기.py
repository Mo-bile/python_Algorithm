def adj_list(M, N, square_areas):
    adj = [[0 for col in range(N)] for row in range(M)]
    while square_areas :
        square_area = square_areas.pop()
        x1 = square_area[0]
        y1 = square_area[1]
        x2 = square_area[2]
        y2 = square_area[3]

        for row in range(M):
            for col in range(N):
                # 조건에서 착각함
                if y1 <= row < y2 and x1 <= col < x2:
                    adj[row][col] = 1
    return adj

def find_area(grid, M, N):
    area_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(grid, row, col):
        stack = [(row, col)]
        area_size = 0

        while stack:
            cy, cx = stack.pop()
            if grid[cy][cx] == 1:
                continue

            grid[cy][cx] = 1
            area_size += 1
            for dy, dx in directions:
                ny, nx = cy + dy, cx + dx
                if (0 <= ny < M) and (0 <= nx < N) and (grid[ny][nx] == 0):
                    stack.append((ny,nx))
        return area_size

    # print(grid)
    area_sizes = []
    for row in range(M):
        for col in range(N):
            if grid[row][col] == 0:
                area_count += 1
                # print(grid)
                area_size = dfs(grid, row, col)
                area_sizes.append(area_size)
    return area_count, area_sizes

if __name__ == "__main__":

    M, N, K = map(int, input().split())
    square_area = []
    for _ in range(K):
        square_area.append(list(map(int, input().split())))

    adj = adj_list(M,N,square_area)
    result, sizes = find_area(adj,M,N)
    sizes.sort()
    sizes = list(map(str, sizes))
    text = ' '.join(sizes)

    print(result)
    print(text)