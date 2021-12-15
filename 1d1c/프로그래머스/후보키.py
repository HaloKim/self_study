from itertools import combinations

def solution(relation):
    total = len(relation)
    col = len(relation[0])
    combis = []
    
    for i in range(1, col+1):
        combis.extend(combinations(range(col), i))

    unique = []
    for combi in combis:
        tmp = [tuple([arr[key] for key in combi]) for arr in relation]
        if len(set(tmp)) == total:
            put = True
            for x in unique:
                if set(x).issubset(set(combi)):
                    put = False
                    break
            if put: 
                unique.append(combi)
    return len(unique)