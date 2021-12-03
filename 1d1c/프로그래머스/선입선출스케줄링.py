def solution(n, cores):
    answer = -1
    time = 50000*10000
    minP = 0
    maxP = 50000*10000
    l = len(cores)
    rest = n-l

    while minP<=maxP:
        mid = (minP+maxP)//2
        completedWork = 0
        for c in cores:
            completedWork += mid//c

        if completedWork<(rest):
            minP = mid+1
        else:
            if time>mid:
                time = mid
            maxP = mid-1

    for i in cores:
        rest -= (time-1)//i

    while rest is not 0:
        answer+=1
        rest-= 1 if time%cores[answer]==0 else 0
