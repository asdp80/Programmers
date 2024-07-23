def solution(dot):
    answer = 0
    if dot[0] > 0 and dot[1] > 0 :
        answer = 1
    elif dot[0] < 0 and dot[1] > 0 :
        answer = 2
    elif dot[0] < 0 and dot[1] < 0 :
        answer = 3
    elif dot[0] > 0 and dot[1] < 0 :
        answer = 4
    return answer

"""
def solution(dot):
    x,y = dot
    if x*y>0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2
"""