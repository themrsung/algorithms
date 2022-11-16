from collections import Counter

def solution(n):
    numbers = []
    
    i = 0
    while len(numbers) < 100:
        num = i + 1
        
        if not num % 3 == 0 and not Counter(str(num))["3"] > 0:
            numbers.append(num)
            
        i += 1
    
    return numbers[n - 1]