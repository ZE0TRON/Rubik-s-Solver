from RubikCubeClass import Cube
def denemefonk(cube,a):
    if(a==1):
        cube.printcube("up")
        cube.printcube("front")
        cube.printcube("left")
        cube.printcube("right")
        cube.printcube("down")
        cube.printcube("back")
f=open('rubikfaces.txt','r')
linelist=f.readlines()
up=[]
front=[]
left=[]
right=[]
down=[]
back=[]
ups=linelist[0]
fronts=linelist[1]
lefts=linelist[2]
rights=linelist[3]
downs=linelist[4]
backs=linelist[5]
for i in xrange(9):
    up.append(ups[i])
for i in xrange(9):
    front.append(fronts[i])
for i in xrange(9):
    left.append(lefts[i])
for i in xrange(9):
    right.append(rights[i])
for i in xrange(9):
    down.append(downs[i])
for i in xrange(9):
    back.append(backs[i])
cube=Cube(up,down,front,back,left,right)
a=1
denemefonk(cube.rc(),a)
print "bitti"
#rc,uc,rac,fac,lc,bc,dac,lac,uac,bac,bc,dc,f
