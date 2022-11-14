def solution(numbers):
    tally = 0
    for num in numbers:
        tally += num
    return tally / len(numbers)