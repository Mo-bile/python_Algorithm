# 복습용 버전 2
# 입력
# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다.
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이
# 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다.
# 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.
#
# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2
#
# 출력
# 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다.
# 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
def fill_square(M, N, square):

    area = [[0 for x in range(N)] for y in range(M)]

    for x1,y1,x2,y2 in square:
        for y in range(y1, y2):
            for x in range(x1, x2):
                area[y][x] = 1

    return area

def find_area(M, N, adj_list):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    def dfs(y,x,grid):
        size = 0
        stack = [(y,x)]

        while stack:
            cy, cx = stack.pop()

            if grid[cy][cx] == 1:
                continue
            grid[cy][cx] = 1
            size += 1

            for dy, dx in directions:
                ny, nx = cy + dy, cx + dx
                # 아래 조건문 부분 빠트림
                if (0 <= ny < M) and (0 <= nx < N) and (grid[ny][nx] == 0): 
                    stack.append((ny,nx))

        return size

    result = []
    for y in range(M):
        for x in range(N):
            if adj_list[y][x] == 0:
                size = dfs(y, x, adj_list)
                result.append(size)
    result.sort()
    return len(result), result


if __name__ == "__main__":
    # M 은 y / N 은 x
    M, N, K = map(int, input().split())

    square = []
    for _ in range(K):
        square.append(list(map(int, input().split())))

    adj_list = fill_square(M,N,square)

    count, sizes = find_area(M,N,adj_list)
    print(count)
    result = map(str, sizes)
    a = ' '.join(result)
    print(a)
