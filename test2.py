from pulp import *
m = LpProblem(sense=LpMinimize)
a = LpVariable('a', lowBound=0)
b = LpVariable('b', lowBound=0)
c = LpVariable('c', lowBound=0)
d = LpVariable('d', lowBound=0)
e = LpVariable('e', lowBound=0)
m += 180 * a + 200 * b + 200 * c + 200 * d + 100 * e 
m += 12 * a + 20 * b + 15 * c + 18 * d + 8 * e >= 300 
m += 18 * a + 12 * b + 12 * c + 10 * d + 12 * e >= 280
m.solve()
print(value(a), value(b), value(c), value(d), value(e))
