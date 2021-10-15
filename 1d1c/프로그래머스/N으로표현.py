def solution(N, number):
    dp = [set([int(str(N)*i)]) for i in range(1, 9)] 
    for i in range(8):
        for j in range(i):
            for num1 in dp[j]:  #i 번 사용해서 나타낼 수 있는 수 
                for num2 in dp[i-j-1]: # N-i번 사용해서 나타낼 수 있는 수
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1//num2)
                        
        if number in dp[i]:
            return i+1 # 정답 출력
    return -1