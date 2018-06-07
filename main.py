import linear as l

# check args count
lines = [line.rstrip('\n') for line in open("input.txt", "r")]

x=lines[0].split(' ')
y=lines[1].split(' ')
l = len(x)
print(l)
# a = l.sum(x)*l.sum(y) - 

print(l.sqsum(x))