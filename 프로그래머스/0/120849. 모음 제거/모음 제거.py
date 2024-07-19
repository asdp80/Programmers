def solution(my_string):
    my_list = list(my_string)
    remove = ['a', 'e', 'i', 'o', 'u']
    
    new_list = [char for char in my_list if char not in remove]  

    answer = ''.join(new_list)
    return answer