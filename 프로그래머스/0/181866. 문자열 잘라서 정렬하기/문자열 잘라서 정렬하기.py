def solution(myString):
    answer = []
    result = []
    answer = myString.split("x")
    result = [s for s in answer if s != ""]
    
    return sorted(result)