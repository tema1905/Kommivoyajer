a = [[0, 380,140, 160, 200],
 [380, 0, 600, 540, 250],
 [140, 600, 0, 360, 350],
 [160, 540, 360, 0, 330],
 [200, 250, 350, 330, 0]]
n = 5
ans = []
b = []
def way2(x, y, s, t, st):
    if x == y and all(t):
        ans.append(s)
        b.append(st)
    else:
        t[x] = True
        for i in range(n):
            if a[x][i] != 0 and t[i] == False:
                way2(i, y, s + a[x][i], t.copy(), st + str(i))
        if all(t):
            way2(y, y, s + a[x][y], t.copy(), st+ str(y))
import time
start = time.time()

t = [False]*n

way2(0, 0, 0, t.copy(), '0')

print('время:',min(ans),
'маршрут:',b[ans.index(min(ans))]) 
