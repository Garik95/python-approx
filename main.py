import math
import linear as li

# check args count
lines = [line.rstrip('\n') for line in open("input.txt", "r")]

x=lines[0].split(' ')
y=lines[1].split(' ')
l = len(x)
a = ( li.sum(x) * li.sum(y) - l * li.mulsum(x,y) ) / ( ( li.sum(x) ) * (li.sum(x) ) - l * li.sqsum(x) )
b = ( li.sum(x) * li.mulsum(x,y) - li.sqsum(x) * li.sum(y) ) / ( ( li.sum(x) ) * (li.sum(x) ) - l * li.sqsum(x) )
r = ( l * li.mulsum(x,y) - li.sum(x) * li.sum(y) ) / math.sqrt( ( l * li.sqsum(x) - ( li.sum(x) ) * (li.sum(x) ) ) * (l * li.sqsum(y) - ( li.sum(y) ) * (li.sum(y) )) )
R = r*r

_y = []
__y = []
for i in range(l):
    _y.append(float(a)*float(x[i])+b)
    __y.append( ( float(y[i]) - float(_y[i]) ) / float(y[i]) )

A = 1/l * math.fabs(li.sum(__y)) * 100

print(" y = %5.4f*x + %5.4f \n r = %5.4f \n R = %5.4f \n A = %5.4f" % (a,b,r,R,A))