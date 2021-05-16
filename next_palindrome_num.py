# https://www.codechef.com/problems/PALIN
from sys import stdin


def nxpalin(s):
    s = s.lstrip("0")
    L = len(s)
    if L < 2:
        # single digit case, & don't crash on accidental blank lines :)
        k = int('0'+s) + 1
        if k == 10:
            k = 11
        return(str(k))  # ----->

    m = L//2
    mdc = (s[m] if L % 2 == 1 else '')
    rst = list(reversed(s[0:m]))
    en = s[-m:L]
    inc_st = True
    for sc, ec in zip(rst, en):
        if ec < sc:
            inc_st = False
            break
        elif ec > sc:
            break

    if inc_st:
        if mdc == '9':
            mdc = '0'
        elif mdc != '':
            mdc = str(1+int(mdc))
            inc_st = False
    if inc_st:
        for p, c in enumerate(rst):
            if c != '9':
                rst[p] = str(1+int(c))
                inc_st = False
                break
            else:
                rst[p] = '0'
        if inc_st:
            # all nines, add a digit
            rst[-1] = '1'
            mdc = mdc+'0'

    return(''.join((*reversed(rst), mdc, *rst)))


for _ in range(int(input())):
    z = stdin.readline().strip()
    print(nxpalin(z))
