

babbles = [
    "aya",
    "ye",
    "woo",
    "ma"
]

def solution(babbling):
    
    
    
    count = 0
    babble_list = []
    
    for babble in babbling:
        has_meaningful_babbles = False
        for bls in babbles:
            if bls in babble:
                babble_list.append((babble, bls))
                has_meaningful_babbles = True
        
        if has_meaningful_babbles:
            only_babbles = ""
            for blist in babble_list:
                if blist[0] == babble:
                    only_babbles += blist[1]
            
            if len(only_babbles) == len(babble):
                count += 1
    
    return count