import math
def solution(n):
    answer = math.floor(math.sqrt(n)) == math.sqrt(n)
    if answer:
        return 1
    else:
        return 2