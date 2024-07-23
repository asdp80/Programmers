def solution(my_string):
    answer = list(my_string)
    ans = []
    for i in answer : 
        if i.isdigit() :
            ans.append(int(i))
        
    return sorted(ans)