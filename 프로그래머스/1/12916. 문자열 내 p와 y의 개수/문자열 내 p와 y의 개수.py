def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y') :
        return True
    else :
        return False
    
    """
    def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
    """