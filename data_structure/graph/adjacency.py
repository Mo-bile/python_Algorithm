# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

# 여기에 코드를 작성하세요

# 영훈 0
adjacency_matrix[0][1] = 1
adjacency_matrix[1][0] = 1
adjacency_matrix[0][2] = 1
adjacency_matrix[2][0] = 1

# 현승 1
adjacency_matrix[1][3] = 1
adjacency_matrix[3][1] = 1
adjacency_matrix[1][5] = 1
adjacency_matrix[5][1] = 1

# 동욱 2 
adjacency_matrix[2][5] = 1
adjacency_matrix[5][2] = 1

# 지웅 3
adjacency_matrix[3][4] = 1
adjacency_matrix[4][3] = 1
adjacency_matrix[3][5] = 1
adjacency_matrix[5][3] = 1

# 규리 4
adjacency_matrix[4][5] = 1
adjacency_matrix[5][4] = 1



print(adjacency_matrix)