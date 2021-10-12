def dfs(tickets,start,check):
    for i in range(len(tickets)):
        if tickets[i][0] == start and i not in check:
            check.append(i)
            dfs(tickets,tickets[i][1],check)
            if len(check) == len(tickets):
                return
            else:
                check.pop()
    return

def solution(tickets):
    answer = ['ICN']
    tickets.sort(key = lambda x:x[-1])
    check = []
    dfs(tickets,'ICN',check)
    for i in check:
        answer.append(tickets[i][1])
    return answer