import linear as li

# check args count
lines = [line.rstrip('\n') for line in open("input.txt", "r")]

x=lines[0].split(' ')
y=lines[1].split(' ')
l = len(x)

print(li.lineReg(x,y,l))