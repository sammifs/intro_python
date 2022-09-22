def double(n):
    return n*2

def triple(n):
    return n*3

def quadruple(n):
    return double(n)*2

def funky(n, m):
    return triple(n) + quadruple(m)

a = 6
b = 16

d1 = double(a)    # 12
d2 = double(b)    # 32

t1 = triple(a)    # 18
t2 = triple(b)    # 48

q1 = quadruple(a) # 24
q2 = quadruple(b) # 64

f1 = funky(a, b)  # 82
f2 = funky(b, a)  # 72
