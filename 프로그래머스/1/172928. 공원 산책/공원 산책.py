# def solution(park, routes):
#     init = []
#     # command = {}
#     # 1. 초기 위치 설정
#     for i in range(len(park)):
#         for j in range(len(park[i])):
#             if park[i][j] == 'S':
#                 init.append(i)
#                 init.append(j)
#     print(init)
    
#     move = []
#     for i in range(len(routes)):
#         # 2. 명령어 파싱
#         move = [routes[i][0], routes[i][2]]
#         how = int(move[1])
        
#         # 3. 이동 가능 여부 체크
#         if move[0] == 'E' :
#             row = park[init[0]]
#             # slicing = row[init[0] : how + 1]
#             slicing = row[init[1] + 1 : init[1] + how + 1]
#             if slicing in 'X' or len(slicing) < how:
#                 continue
#             init[1] += how
            
#         elif move[0] == 'W':
#             row = park[init[0]]
#             # slicing = row[how : init[0] + 1 ]
#             slicing = row[init[1] - how : init[1]]
#             if slicing in 'X' or len(slicing) < how:
#                 continue
#             init[1] -= how
            
                        
#         elif move[0] == 'S':
#             print(init[0] + how)
#             # if len(park) - init[0] < init[0] + how :
#             if init[0] + how >= len(park):
#                 print("넘음")
#                 continue
            
#             col = [park[i][init[1]] for i in range(init[0] , init[0] + how)]
#             if 'X' in col or len(col) < how:
#                 continue
#             init[0] += how
        
        
#         elif move[0] == 'N':
#             if init[0] - how < 0:  # 북쪽으로 이동할 때 공원의 경계를 넘는지 확인
#                 continue
            
#             col = [park[i][init[1]] for i in range(init[0] - how, init[0])]
#             if 'X' in col or len(col) < how:
#                 continue
#             init[0] -= how

        




#     # 4. 이동
    
#     # 5. 최종 위치 반환
#     answer = []
#     return init

def solution(park, routes):
    # 1. 초기 위치 찾기
    h, w = len(park), len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j
    
    # 2. 명령어 처리
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        
        # 임시 위치 설정
        nx, ny = x, y
        
        # 이동 방향에 따른 좌표 변화 계산
        for _ in range(distance):
            if direction == 'E':
                ny += 1
            elif direction == 'W':
                ny -= 1
            elif direction == 'S':
                nx += 1
            elif direction == 'N':
                nx -= 1

            # 경계 초과 시 이동 중지
            if nx < 0 or ny < 0 or nx >= h or ny >= w or park[nx][ny] == 'X':
                nx, ny = x, y
                break

        # 이동이 가능한 경우 위치 업데이트
        if (nx, ny) != (x, y):
            x, y = nx, ny
    
    # 최종 위치 반환
    return [x, y]