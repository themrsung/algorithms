from collections import Counter

def solution(array):
    as_string = ""
    for element in array:
        as_string += str(element)
    
    return Counter(as_string)["7"]