from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    for i in course:
        candidates = []
        for order in orders:
            for k in list(combinations(order, i)):
                candidates.append(''.join(sorted(k)))
        sorted_candidates = Counter(candidates).most_common()
        ans += [menu for menu, cnt in sorted_candidates if cnt >= 2 and cnt == sorted_candidates[0][1]]
    return sorted(ans)