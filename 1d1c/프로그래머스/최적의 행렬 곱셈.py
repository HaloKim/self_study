import math

def solution(matrix_sizes):
    mat = matrix_sizes
    dp = [[math.inf]*len(mat) for _ in range(len(mat))]
    for idx in range(len(mat)):
        dp[idx][idx] = 0
    
    for gap in range(1, len(mat)):
        for start in range(len(mat)):
            end = start + gap
            if end >= len(mat):
                break
            for sep in range(start, end):
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][sep] + dp[sep+1][end] + (mat[start][0] * mat[sep][1] * mat[end][1])
                )
    return dp[0][-1]
        