from collections import Counter

def solution(s1, s2):
    cnt = Counter(s1 + s2)
    similar = 0
    for counter in cnt.keys():
        if cnt[counter] > 1:
            similar += 1
    return similar