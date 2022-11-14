import math
def solution(money):
    coffees = math.floor(money / 5500)
    coffee_price = coffees * 5500
    
    leftover = money - coffee_price
    
    
    return [coffees, leftover]