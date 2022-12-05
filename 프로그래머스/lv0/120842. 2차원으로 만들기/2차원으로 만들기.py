import math

def solution(num_list, n):
    num_list_answer = []
    
    index_start = 0
    index_end = n
    
    for i in range(math.ceil(len(num_list) / n)):
        num_list_answer.append(num_list[index_start:index_end])
        index_start += n
        index_end += n
    
    return num_list_answer