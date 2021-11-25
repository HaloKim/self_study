def solution(numbers, hand):
    left = [1,4,7]
    right = [3,6,9]
    ans = ''
    l = 10
    r = 12
    for i in numbers:
        if i == 0:
            i = 11
        if i in left:
            ans += "L"
            l = i
        elif i in right:
            ans += 'R'
            r = i
        else:
            ll = abs(i - l)
            rr = abs(i - r)
            if sum(divmod(ll,3)) == sum(divmod(rr,3)):
                if hand == "left":
                    l = i
                    ans += 'L'
                else:
                    r = i
                    ans += 'R'
            elif sum(divmod(ll,3)) < sum(divmod(rr,3)):
                l = i
                ans += 'L'
            elif sum(divmod(ll,3)) > sum(divmod(rr,3)):
                r = i
                ans += 'R'
    return ans