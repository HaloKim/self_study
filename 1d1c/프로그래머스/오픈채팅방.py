def solution(record):
    dict = {}
    ans = []
    ids = []
    for i in record:
        if i.split(' ')[0] == 'Enter':
            dict[i.split(' ')[1]] = i.split(' ')[-1]
            ans.append('님이 들어왔습니다.')
            ids.append(i.split(' ')[1])
        if i.split(' ')[0] == "Leave":
            ans.append('님이 나갔습니다.')
            ids.append(i.split(' ')[1])
        if i.split(' ')[0] == "Change":
            dict[i.split(' ')[1]] = i.split(' ')[-1]
    result = []
    for i in range(len(ans)):
        result.append((dict[ids[i]]+ans[i]))
    return result