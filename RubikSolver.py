from RubikCubeClass import Cube
import thread
import threading
class myThread (threading.Thread):
    def __init__(self, threadID,name,cube,step,lastmove,solution,solved,counter,counters,threads,cubelist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.cubelist=cubelist
        self.name = name
        self.counter = counter
        self.cube=cube
        self.threads=threads
        self.step=step
        self.lastmove=lastmove
        self.solution=solution
        self.solved=solved
        self.counters=counters
    def run(self):
        solve(self.cube,self.step,self.lastmove,self.solution,self.solved,self.counter,self.name,self.counters,self.threads,self.cubelist)


def killthreads():
    global tc
    for i in xrange(1,tc+1):
        "th"+str(i).exit()
def solve(cube,step,lastmove,solution,solved,counter,cubelist,tc):
    print len(cubelist)
    print tc
    print counter
    if(solved==0):
        if(step>26):
            del cubelist[int(thname[2:])]
            thname.exit()
            return 0
        lme=0
        '''
        u
        f
        l
        r
        d
        b
        '''
        if(cube.isSolved()==1):
            print "cozdum lan"
            if(step<27):
                #cube.setSolution(solution)
                print solution
                solved=1
                #th1.exit()
                killthreads()
                return 0
        if(tn==1 or tn==5 ):
            if(lastmove!="uac" and counter[0]!=3):
                tc+=1
                cubelist.append(cube.uc())
                solve(cubelist[tc],step+1,"uc",solution+"uc",solved,[counter[0]+1,0,0,0,counter[4],0],cubelist,tc)
                #solve(cube.uc(),step+1,"uc",solution+"uc",solved,5,thname,[counter[0]+1,0,0,0,counter[4],0])
                cube=cube.uac()
        if(tn==2 or tn==5 ):
            if(lastmove!="uc" and counter[0]!=3):
                tc+=1
                cubelist.append(cube.uac())
                solve(cubelist[tc],step+1,"uac",solution+"uac",solved,[counter[0]+1,0,0,0,counter[4],0],cubelist,tc)
                #solve(cube.uac(),step+1,"uac",solution+"uac",solved,5,thname,[counter[0]+1,0,0,0,counter[4],0])
                cube=cube.uc()
        if(tn==3 or tn==5):
            if(lastmove!="dac" and counter[4]!=3):
                tc+=1
                cubelist.append(cube.dc())
                solve(cubelist[tc],step+1,"dc",solution+"dc",solved,[counter[0],0,0,0,counter[4]+1,0],cubelist,tc)
                #solve(cube.dc(),step+1,"dc",solution+"dc",solved,5,thname,[counter[0],0,0,0,counter[4]+1,0])
                cube=cube.dac()
        if(tn==4 or tn==5 ):
            if(lastmove!="dc" and counter[4]!=3):
                tc+=1
                cubelist.append(cube.dac())
                solve(cubelist[tc],step+1,"dac",solution+"dac",solved,[counter[0],0,0,0,counter[4]+1,0],cubelist,tc)
                #solve(cube.dac(),step+1,"dac",solution+"dac",solved,5,thname,[counter[0],0,0,0,counter[4]+1,0])
                cube=cube.dc()
        if(tn==5 or tn==5 ):
            if(lastmove!="fac" and counter[1]!=3):
                tc+=1
                cubelist.append(cube.fc())
                solve(cubelist[tc],step+1,"fc",solution+"fc",solved,[0,counter[1]+1,0,0,0,counter[5]],cubelist,tc)
                #solve(cube.fc(),step+1,"fc",solution+"fc",solved,5,thname,[0,counter[1]+1,0,0,0,counter[5]])
                cube=cube.fac()
        if(tn==6 or tn==5 ):
            if(lastmove!="fc" and counter[1]!=3):
                tc+=1
                cubelist.append(cube.fac())
                solve(cubelist[tc],step+1,"fac",solution+"fac",solved,[0,counter[1]+1,0,0,0,counter[5]],cubelist,tc)
                #solve(cube.fac(),step+1,"fac",solution+"fac",solved,5,thname,[0,counter[1]+1,0,0,0,counter[5]])
                cube=cube.fc()
        if(tn==7 or tn==5 ):
            if(lastmove!="bac" and counter[5]!=3):
                tc+=1
                cubelist.append(cube.bc())
                solve(cubelist[tc],step+1,"bc",solution+"bc",solved,[0,counter[1],0,0,0,counter[5]+1],cubelist,tc)
                #solve(cube.bc(),step+1,"bc",solution+"bc",solved,5,thname,[0,counter[1],0,0,0,counter[5]+1])
                cube=cube.bac()
        if(tn==8 or tn==5 ):
            if(lastmove!="bc" and counter[5]!=3):
                tc+=1
                cubelist.append(cube.bac())
                solve(cubelist[tc],step+1,"bac",solution+"bac",solved,[0,counter[1],0,0,0,counter[5]+1],cubelist,tc)
                #solve(cube.bac(),step+1,"bac",solution+"bac",solved,5,thname,[0,counter[1],0,0,0,counter[5]+1])
                cube=cube.bc()
        if(tn==9 or tn==5 ):
            if(lastmove!="lac" and counter[2]!=3):
                tc+=1
                cubelist.append(cube.lc())
                solve(cubelist[tc],step+1,"lc",solution+"lc",solved,[0,0,counter[2]+1,counter[3],0,0],cubelist,tc)
                #solve(cube.lc(),step+1,"lc",solution+"lc",solved,5,thname,[0,0,counter[2]+1,counter[3],0,0])
                cube=cube.lac()
        if(tn==10 or tn==5 ):
            if(lastmove!="lc" and counter[2]!=3):
                tc+=1
                cubelist.append(cube.lc())
                solve(cubelist[tc],step+1,"lac",solution+"lac",solved,[0,0,counter[2]+1,counter[3],0,0],cubelist,tc)
                #solve(cube.lac(),step+1,"lac",solution+"lac",solved,5,thname,[0,0,counter[2]+1,counter[3],0,0])
                cube=cube.lc()
        if(tn==11 or tn==5 ):
            if(lastmove!="rac" and counter[3]!=3):
                tc+=1
                cubelist.append(cube.rc())
                solve(cubelist[tc],step+1,"rc",solution+"rc",solved,[0,0,counter[2],counter[3]+1,0,0],cubelist,tc)
                                #solve(cube.rc(),step+1,"rc",solution+"rc",solved,5,thname,[0,0,counter[2],counter[3]+1,0,0])
                cube=cube.rac()
        if(tn==12 or tn==5 ):
            if(lastmove!="rc" and counter[3]!=3):
                tc+=1
                cubelist.append(cube.rc())
                solve(cubelist[tc],step+1,"rac",solution+"rac",solved,[0,0,counter[2],counter[3]+1,0,0],cubelist,tc)
                                #solve(cube.rac(),step+1,"rac",solution+"rac",solved,5,thname,[0,0,counter[2],counter[3]+1,0,0])
                cube=cube.rc()

up=[]
front=[]
left=[]
right=[]
down=[]
back=[]
f=open('rubikfaces.txt','r')
linelist=f.readlines()
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
cube1=Cube(up,down,front,back,left,right)
cubelist=[]
threadlist=[]
tc=0
for i in xrange(11):
    cubelist.append(cube1)

'''
cube.printcube("up")
cube.printcube("front")
cube.printcube("left")
cube.printcube("right")
cube.printcube("down")
cube.printcube("back")
'''
#thread.start_new_thread(solve,(cube,0,"","",0,1,"th1"))
counters=[0,0,0,0,0,0]
for i in xrange(11):
    threadlist.append(myThread(i,"th"+str(i),cubelist[i],0,"","",0,i,counters,threadlist,cubelist))
    tc+=1
tc=11
for i in xrange(11):
    threadlist[i].start()
#print cube.get_solution()
