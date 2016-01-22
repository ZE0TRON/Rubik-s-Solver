class Cube:
    def __init__(self,up,down,front,back,left,right):
        self.up=[]
        for i in xrange(len(up)):
            self.up.append(up[i])
        self.down=[]
        for i in xrange(len(down)):
            self.down.append(down[i])
        self.front=[]
        for i in xrange(len(front)):
            self.front.append(front[i])
        self.back=[]
        for i in xrange(len(back)):
            self.back.append(back[i])
        self.left=[]
        for i in xrange(len(left)):
            self.left.append(left[i])
        self.right=[]
        for i in xrange(len(right)):
            self.right.append(right[i])
        self.minstep=100
        self.solution=""
        self.u=0
        self.f=0
        self.l=0
        self.r=0
        self.d=0
        self.b=0
    def uc(self):
        #Up clockwise
        self.front[0:3],self.right[0:3],self.back[0:3],self.left[0:3]=self.right[0:3],self.back[0:3],self.left[0:3],self.front[0:3]
        self.up[0],self.up[1],self.up[2],self.up[3],self.up[4],self.up[5],self.up[6],self.up[7],self.up[8]=self.up[6],self.up[3],self.up[0],self.up[7],self.up[4],self.up[1],self.up[8],self.up[5],self.up[2]
        return self
    def uac(self):
        #Up anticlockwise
        self.front[0:3],self.right[0:3],self.back[0:3],self.left[0:3]=self.left[0:3],self.front[0:3],self.right[0:3],self.back[0:3]
        self.up[0],self.up[1],self.up[2],self.up[3],self.up[4],self.up[5],self.up[6],self.up[7],self.up[8]=self.up[2],self.up[5],self.up[8],self.up[1],self.up[4],self.up[7],self.up[0],self.up[3],self.up[6]
        return self
    def dc(self):
        #Down clockwise
        self.front[6:9],self.right[6:9],self.back[6:9],self.left[6:9]=self.left[6:9],self.front[6:9],self.right[6:9],self.back[6:9]
        self.down[0],self.down[1],self.down[2],self.down[3],self.down[4],self.down[5],self.down[6],self.down[7],self.down[8]=self.down[6],self.down[3],self.down[0],self.down[7],self.down[4],self.down[1],self.down[8],self.down[5],self.down[2]
        return self
    def dac(self):
        #Down anticlockwise
        self.front[6:9],self.right[6:9],self.back[6:9],self.left[6:9]=self.right[6:9],self.back[6:9],self.left[6:9],self.front[6:9]
        self.down[0],self.down[1],self.down[2],self.down[3],self.down[4],self.down[5],self.down[6],self.down[7],self.down[8]=self.down[2],self.down[5],self.down[8],self.down[1],self.down[4],self.down[7],self.down[0],self.down[3],self.down[6]
        return self
    def fc(self):
        #Front clockwise
        self.up[6:9],(self.right[0],self.right[3],self.right[6]),self.down[0:3],(self.left[2],self.left[5],self.left[8])=(self.left[8],self.left[5],self.left[2]),self.up[6:9],(self.right[6],self.right[3],self.right[0]),self.down[0:3]
        self.front[0],self.front[1],self.front[2],self.front[3],self.front[4],self.front[5],self.front[6],self.front[7],self.front[8]=self.front[6],self.front[3],self.front[0],self.front[7],self.front[4],self.front[1],self.front[8],self.front[5],self.front[2]
        return self
    def fac(self):
        #Front anticlockwise
        self.up[6:9],(self.right[0],self.right[3],self.right[6]),self.down[0:3],(self.left[2],self.left[5],self.left[8])=(self.right[0],self.right[3],self.right[6]),(self.down[2],self.down[1],self.down[0]),(self.left[2],self.left[5],self.left[8]),(self.up[8],self.up[7],self.up[6])
        self.front[0],self.front[1],self.front[2],self.front[3],self.front[4],self.front[5],self.front[6],self.front[7],self.front[8]=self.front[2],self.front[5],self.front[8],self.front[1],self.front[4],self.front[7],self.front[0],self.front[3],self.front[6]
        return self
    def bc(self):
        #Back clockwise
        self.up[0:3],(self.right[2],self.right[5],self.right[8]),self.down[6:9],(self.left[6],self.left[3],self.left[0])=(self.right[2],self.right[5],self.right[8]),(self.down[8],self.down[7],self.down[6]),(self.left[0],self.left[3],self.left[6]),self.up[0:3]
        self.back[0],self.back[1],self.back[2],self.back[3],self.back[4],self.back[5],self.back[6],self.back[7],self.back[8]=self.back[6],self.back[3],self.back[0],self.back[7],self.back[4],self.back[1],self.back[8],self.back[5],self.back[2]
        return self
    def bac(self):
        #Back anticlockwise
        self.up[0:3],(self.right[2],self.right[5],self.right[8]),self.down[6:9],(self.left[0],self.left[3],self.left[6])=(self.left[6],self.left[3],self.left[0]),self.up[0:3],(self.right[8],self.right[5],self.right[2]),self.down[6:9]
        self.back[0],self.back[1],self.back[2],self.back[3],self.back[4],self.back[5],self.back[6],self.back[7],self.back[8]=self.back[2],self.back[5],self.back[8],self.back[1],self.back[4],self.back[7],self.back[0],self.back[3],self.back[6]
        return self
    def lc(self):
        #Left clockwise
        (self.up[0],self.up[3],self.up[6]),(self.front[0],self.front[3],self.front[6]),(self.down[0],self.down[3],self.down[6]),(self.back[2],self.back[5],self.back[8])=(self.back[8],self.back[5],self.back[2]),(self.up[0],self.up[3],self.up[6]),(self.front[0],self.front[3],self.front[6]),(self.down[6],self.down[3],self.down[0])
        self.left[0],self.left[1],self.left[2],self.left[3],self.left[4],self.left[5],self.left[6],self.left[7],self.left[8]=self.left[6],self.left[3],self.left[0],self.left[7],self.left[4],self.left[1],self.left[8],self.left[5],self.left[2]
        return self
    def lac(self):
        #left anticlockwise
        (self.up[0],self.up[3],self.up[6]),(self.front[0],self.front[3],self.front[6]),(self.down[0],self.down[3],self.down[6]),(self.back[2],self.back[5],self.back[8])=(self.front[0],self.front[3],self.front[6]),(self.down[0],self.down[3],self.down[6]),(self.back[8],self.back[5],self.back[2]),(self.up[6],self.up[3],self.up[0])
        self.left[0],self.left[1],self.left[2],self.left[3],self.left[4],self.left[5],self.left[6],self.left[7],self.left[8]=self.left[2],self.left[5],self.left[8],self.left[1],self.left[4],self.left[7],self.left[0],self.left[3],self.left[6]
        return self
    def rc(self):
        #Right clockwise
        (self.up[2],self.up[5],self.up[8]),(self.front[2],self.front[5],self.front[8]),(self.down[2],self.down[5],self.down[8]),(self.back[6],self.back[3],self.back[0])=(self.front[2],self.front[5],self.front[8]),(self.down[2],self.down[5],self.down[8]),(self.back[6],self.back[3],self.back[0]),(self.up[2],self.up[5],self.up[8])
        self.right[0],self.right[1],self.right[2],self.right[3],self.right[4],self.right[5],self.right[6],self.right[7],self.right[8]=self.right[6],self.right[3],self.right[0],self.right[7],self.right[4],self.right[1],self.right[8],self.right[5],self.right[2]
        return self
    def rac(self):
        #Right anticlockwise
        (self.up[2],self.up[5],self.up[8]),(self.front[2],self.front[5],self.front[8]),(self.down[2],self.down[5],self.down[8]),(self.back[0],self.back[3],self.back[6])=(self.back[6],self.back[3],self.back[0]),(self.up[2],self.up[5],self.up[8]),(self.front[2],self.front[5],self.front[8]),(self.down[8],self.down[5],self.down[2])
        self.right[0],self.right[1],self.right[2],self.right[3],self.right[4],self.right[5],self.right[6],self.right[7],self.right[8]=self.right[2],self.right[5],self.right[8],self.right[1],self.right[4],self.right[7],self.right[0],self.right[3],self.right[6]
        return self
    def isSolved(self):
        #Check if two cubes are the same
        equal=1
        for i in xrange(9):
            if(self.up[i]!=self.up[4]):
                equal=0
        if(equal==1):
            for i in xrange(9):
                if(self.down[i]!=self.down[4]):
                    equal=0
        if(equal==1):
            for i in xrange(9):
                if(self.front[i]!=self.front[4]):
                    equal=0
        if(equal==1):
            for i in xrange(9):
                if(self.back[i]!=self.back[4]):
                    equal=0
        if(equal==1):
            for i in xrange(9):
                if(self.left[i]!=self.left[4]):
                    equal=0
        if(equal==1):
            for i in xrange(9):
                if(self.right[i]!=self.right[4]):
                    equal=0
        return equal
    def printcube(self,face):
        if(face=="up"):
            print self.up
        elif(face=="front"):
            print self.front
        elif(face=="down"):
            print self.down
        elif(face=="right"):
            print self.right
        elif(face=="left"):
            print self.left
        elif(face=="back"):
            print self.back
    def get_minStep(self):
        return self.minstep
    def minStep(self,number):
        self.minstep=number
    def get_solution(self):
        return self.solution
    def setSolution(self,solution):
        self.solution=solution
    '''
    def setU(self,u):
        self.u=u
    def setF(self,f):
        self.f=f
    def setL(self,l):
        self.l=l
    def setR(self,r):
        self.r=r
    def setD(self,d):
        self.d=d
    def setB(self,b):
        self.b=b
    def getU(self):
        return self.u
    def getF(self):
        return self.f
    def getL(self):
        return self.l
    def getR(self):
        return self.r
    def getD(self):
        return self.d
    def getB(self):
        return self.b
    '''
