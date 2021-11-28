def solution(n, results):
    rank = [[0]*(n+1) for _ in range(n+1)]
    ans = 0
    for w,l in results:
        rank[w][l], rank[l][w] = 1,-1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if rank[i][k] == 0:
                    continue
                if rank[i][k] == rank[k][j]:
                    rank[i][j] = rank[i][k]
                    rank[j][i] = -rank[i][k]
    for i in range(1,n+1):
        if rank[i].count(0) == 2:
            ans+=1
    return ans