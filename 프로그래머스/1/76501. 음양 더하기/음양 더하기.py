def solution(absolutes, signs):
    answer = 123456789
    result = 0 
    for i in range(len(absolutes)) :
        if signs[i] == 1 :
            result += absolutes[i]
        else : 
            result -= absolutes[i]
            
    return result