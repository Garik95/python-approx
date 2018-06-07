def sum(x):
    S = 0
    for _x in range(len(x)):
        S = S + float(x[int(_x)])
    return S
def mulsum(x,y):
    S = 0
    for i in range(len(x)):
        S = S + float(x[int(i)]) * float(y[int(i)])
    return S
def sqsum(x):
    S = 0
    for i in range(len(x)):
        S = S + float(x[int(i)])*float(x[int(i)])
    return S
