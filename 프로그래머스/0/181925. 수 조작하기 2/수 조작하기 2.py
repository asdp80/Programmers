def solution(numLog):
    move_mapping = {1: "w", -1: "s", 10: "d", -10: "a"}
    result = ""
    
    for i in range(1, len(numLog)):
        difference = numLog[i] - numLog[i - 1]
        result += move_mapping[difference]
        
    return result