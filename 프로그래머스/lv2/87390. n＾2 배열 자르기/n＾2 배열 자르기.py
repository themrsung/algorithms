import math
def get_nth_element(n, i):
     return max(i%n + 1, math.floor(i / n) + 1)
    

def solution(n, left, right):
    result = []
    for i in range(left, right + 1):
        result.append(get_nth_element(n, i))
    return result