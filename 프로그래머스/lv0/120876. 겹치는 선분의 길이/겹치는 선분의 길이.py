from collections import Counter
def solution(lines):
    points = []
    for line in lines:
        for i in range(line[0], line[1]):
            points.append(i)
    
    cnt = Counter(points)
    intersection_count = 0
    for cnt_key in cnt.keys():
        if cnt[cnt_key] > 1:
            intersection_count += 1
    
    print(cnt)
    return intersection_count