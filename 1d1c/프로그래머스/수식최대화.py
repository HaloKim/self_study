from itertools import permutations

def calc(op, seq, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if op[seq] == '*':
            spl = exp.split('*')
            temp = []
            for s in spl:
                temp.append(calc(op, seq+1, s))
            return str(eval("*".join(temp)))
            
        if op[seq] == '+':
            spl = exp.split('+')
            temp = []
            for s in spl:
                temp.append(calc(op, seq+1, s))
            return str(eval("+".join(temp)))
            
        if op[seq] == '-':
            spl = exp.split('-')
            temp = []
            for s in spl:
                temp.append(calc(op, seq+1, s))
            return str(eval("-".join(temp)))

def solution(expression):
    ans = 0
    operations = list(permutations(['+','*','-'],3))
    for op in operations:
        result = abs(int(calc(op, 0, expression)))
        if result > ans:
            ans = result
    return ans