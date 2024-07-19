def solution(hp):
    j, b, g = 5, 3, 1
    
    result = 0
    
    result += hp // j
    hp %= j
    result += hp // b
    hp %= b
    result += hp // g
    
    
    
    return result