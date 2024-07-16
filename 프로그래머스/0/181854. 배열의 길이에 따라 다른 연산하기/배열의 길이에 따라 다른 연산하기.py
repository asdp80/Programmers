def solution(arr, n):
    answer = []
    length = len(arr)
    
    if length % 2 == 0 :
        for i in range(length):
            if i % 2 == 0:
                answer.append(arr[i])
            else:
                answer.append(arr[i] + n)
    else:
        for i in range(length):
            if i % 2 != 0:
                answer.append(arr[i])
            else:
                answer.append(arr[i] + n)
        
                

            
    return answer