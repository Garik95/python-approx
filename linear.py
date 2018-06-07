import math
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

def a(x,y,l):
    return ( sum(x) * sum(y) - l * mulsum(x,y) ) / ( ( sum(x) ) * (sum(x) ) - l * sqsum(x) )

def b(x,y,l):
    return ( sum(x) * mulsum(x,y) - sqsum(x) * sum(y) ) / ( ( sum(x) ) * (sum(x) ) - l * sqsum(x) )

def r(x,y,l):
    return ( l * mulsum(x,y) - sum(x) * sum(y) ) / math.sqrt( ( l * sqsum(x) - ( sum(x) ) * (sum(x) ) ) * (l * sqsum(y) - ( sum(y) ) * (sum(y) ) ) )

def A(x,y,l):
    _y = []
    __y = []
    for i in range(l):
        _y.append(float(a(x,y,l))*float(x[i])+b(x,y,l))
        __y.append( ( float(y[i]) - float(_y[i]) ) / float(y[i]) )

    A = 1/l * math.fabs(sum(__y)) * 100
    return A

def lineReg(x,y,l):
    print(" y = %5.4f*x + %5.4f \n r = %5.4f \n R = %5.4f \n A = %5.4f" % (a(x,y,l),b(x,y,l),r(x,y,l),r(x,y,l)*r(x,y,l),A(x,y,l)))