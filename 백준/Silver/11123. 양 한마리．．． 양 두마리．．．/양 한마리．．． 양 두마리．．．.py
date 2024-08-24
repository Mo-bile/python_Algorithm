def find_is_lamb_by_dfs(grid, row, column):

    directins = [(0,-1),(0,1),(1,0),(-1,0)]

    def dfs(x, y):
        stack = [(x, y)]

        while stack:
            cx,cy = stack.pop()

            if grid[cx][cy] == ".":
                continue

            grid[cx][cy] = "."

            for dx,dy in directins:
                nx, ny = cx + dx, cy + dy

                #for loop 밖에 있었음
                if (0 <= nx < row) and (0 <= ny < column) and (grid[nx][ny] == "#"):
                    stack.append((nx,ny))

    lamb_count = 0
    for i in range(row):
        for j in range(column):
            if grid[i][j] == "#":
                dfs(i, j)
                lamb_count += 1

    return lamb_count


if __name__ == "__main__":

    test_case = int(input())

    for _ in range(test_case):
        # row, colum 갯수 입력 받음
        R, C = map(int, input().split())

        grid = []

        # row 수만큼 반복문으로 입력을 받음
        # 각 row 마다 리스트 입력을 받음
        for __ in range(R):
            grid.append(list(input()))

        result = find_is_lamb_by_dfs(grid, R, C)
        print(result)