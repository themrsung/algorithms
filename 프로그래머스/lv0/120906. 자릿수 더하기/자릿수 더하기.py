def solution(n):
    answer = 0
    for l in str(n):
        answer += int(l)
    return answer