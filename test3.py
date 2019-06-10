from pulp import *
c = [300,240,150,80]
w = [5,4,3,2]
n = len(c)
s = 7
m = LpProblem(sense=LpMaximize)
x = [LpVariable('x%d' % i, cat = LpBinary) for i in range (n)]
m += lpDot(c,x)
m += lpDot(w,x) <= s
m.solve()

for i in range(n): print(value(x[i])) 
