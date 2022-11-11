import math

def solution(price):
    discount_rate = 0
    if price >= 500000:
        discount_rate = 0.2
    elif price >= 300000:
        discount_rate = 0.1
    elif price >= 100000:
        discount_rate = 0.05
    
    return math.floor(price * (1 - discount_rate))