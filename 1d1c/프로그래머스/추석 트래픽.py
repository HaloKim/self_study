def get_time(time):
    h = int(time[:2])*3600
    m = int(time[3:5])*60
    s = int(time[6:8])
    ms = int(time[9:])
    return (h + m + s)*1000 + ms

def get_start(time, run):
    n_time = run[:-1]
    int_run = int(float(n_time) * 1000)
    return get_time(time) - int_run + 1

def solution(lines):
    start = []
    end = []
    ans = 0
    for i in lines:
        _, time, run = i.split()
        start.append(get_start(time,run))
        end.append(get_time(time))
    for i in range(len(lines)):
        cnt = 0
        for j in range(i,len(lines)):
            if end[i] > start[j] - 1000:
                cnt += 1
        ans = max(ans,cnt)
    return ans