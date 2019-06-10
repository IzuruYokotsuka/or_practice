from pulp import *
m = LpProblem(sense=LpMaximize)
x = LpVariable('x', lowBound=0)
y = LpVariable('y', lowBound=0)
m += 300 * x + 280 * y 
m += 12 * x + 18 * y <= 180 
m += 20 * x + 12 * y <= 200
m += 15 * x + 12 * y <= 200
m += 18 * x + 10 * y <= 200
m += 8 * x + 12 * y <= 100
m.solve()
print(value(x), value(y))
