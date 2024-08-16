def solution(wallpaper):    
    top, down,left, right = None, None, float('inf'), -float('inf')
    
    for i in range(len(wallpaper)):
        row = wallpaper[i]        

        loc = row.find('#')
        rloc = row.rfind('#')

        if loc != -1: # find 성공했을 때 
            if top == None : # top 을 아직 찾은적이 없을 때
                top = i
            down = i

            left = min(left, loc)
            right = max(right, rloc)

    # answer.append(top)
    # answer.append(left)
    # answer.append(down + 1)
    # answer.append(right + 1)
    return [top, left, down + 1, right + 1]