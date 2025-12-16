import curses as cs
import random as rd
import time
U = cs.KEY_UP
D = cs.KEY_DOWN
L = cs.KEY_LEFT
R = cs.KEY_RIGHT
def g(s):
    cs.curs_set(0)
    s.nodelay(1)
    s.timeout(100)
    h, w = s.getmaxyx()
    if h < 10 or w < 20:
        s.clear()
        s.addstr(h // 2, w // 2 - 10, "ZBYT MAŁE OKNO!")
        s.addstr(h // 2 + 1, w // 2 - 12, "POWIĘKSZ I SPRÓBUJ PONOWNIE.")
        s.refresh()
        time.sleep(3)
        return
    s.clear()
    s.addstr(h // 2, w // 2 - 2, "SNAKE")
    s.refresh()
    time.sleep(1)
    sn = [[h // 2, w // 2]]
    dr = R
    fds = [[rd.randint(1, h - 2), rd.randint(1, w - 2)]]
    sc = 0
    def np():
        while True:
            p = [rd.randint(1, h - 2), rd.randint(1, w - 2)]
            if p not in sn and p not in fds:
                return p
    while True:
        h, w = s.getmaxyx()
        if h < 10 or w < 20:
            break
        k = s.getch()
        if k == R and dr != L:
            dr = R
        elif k == L and dr != R:
            dr = L
        elif k == U and dr != D:
            dr = U
        elif k == D and dr != U:
            dr = D
        hd = sn[0]
        nhd = [hd[0], hd[1]]
        if dr == R:
            nhd[1] += 1
        elif dr == L:
            nhd[1] -= 1
        elif dr == U:
            nhd[0] -= 1
        elif dr == D:
            nhd[0] += 1
        sn.insert(0, nhd)
        if (nhd[0] <= 0 or nhd[0] >= h - 1 or
            nhd[1] <= 0 or nhd[1] >= w - 1):
            break
        if nhd in sn[1:]:
            break
        e = False
        for f in fds:
            if nhd == f:
                sc += 1
                fds.remove(f)
                e = True
                break
        if not e:
            tl = sn.pop()
            s.addch(tl[0], tl[1], ' ')
        if e:
            fds.append(np())
            if sc % 5 == 0 and sc > 0:
                fds.append(np())
        s.clear()
        for seg in sn:
            s.addch(seg[0], seg[1], 'o')
        for f in fds:
            s.addch(f[0], f[1], '*')
        ss = f"WYNIK: {sc}"
        s.addstr(0, w - len(ss) - 2, ss)
        s.refresh()
    s.clear()
    s.addstr(h // 2, w // 2 - 5, "KONIEC GRY")
    ss = f"WYNIK: {sc}"
    s.addstr(h // 2 + 1, w // 2 - len(ss) // 2, ss)
    s.refresh()
    time.sleep(3)
def main():
    cs.wrapper(g)
if __name__ == '__main__':
    main()
