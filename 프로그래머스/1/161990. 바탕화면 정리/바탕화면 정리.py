def solution(wallpaper):
    answer = []
    
    top, down,left, right = -2, 0, 50, 0
    
    for i in range(len(wallpaper)):
        row = wallpaper[i]        

        loc = row.find('#')
        rloc = row.rfind('#')
        print(loc, rloc)
        if loc != -1 or rloc != -1:
            if top == -2 : 
                top = i
            if top != -2 :
                down = i

            left = min(left, loc)
            right = max(right, rloc)

    answer.append(top)
    answer.append(left)
    answer.append(down + 1)
    answer.append(right + 1)
    return answer