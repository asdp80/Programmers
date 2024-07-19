def solution(rny_string):
    convert = list(rny_string)
    answer = []
    for i in range(len(convert)):
        if convert[i] == 'm':
            answer.append('rn')
        else :
            answer.append(convert[i])
            
    sol = ''.join(answer)
    return sol