import random as r

#flowers, badgers, lions, buffer flowers, buffer badgers, buffer lions, cell version,last flowers, last badgers, last lions
def matrix(x,y):
  out = []
  #print(x,y)
  for i in range(x):
    out.append([(0,0,0,0,0,0,0,0,0,None)]*y)
    
  return(out)
def matrix2(x,y):
  out = []
  #print(x,y)
  for i in range(x):
    out.append([0])
    
  return(out)
w = 100 #width of matrix
h = 100 #height of matrix

pw = 500 #width of display
ph = 500 #height of display

rx = pw/w #width of a grid square
ry = ph/h #height of a grid square


foodChunkWidth = 100
foodChunkHeight = 100


cw = w/foodChunkWidth
ch = h/foodChunkHeight
foodC = matrix2(foodChunkWidth,foodChunkHeight)
scene = matrix(w,h)
searchR = 5


rpf = 0






def getFoodChunk(x,y):
    xpos = floor(x/cw)
    ypos = floor(y/ch)
    print(xpos,ypos)
    
    
    
    
    
    


def distributeBadgers(amount):
    global scene
    for i in range(amount):
        x = r.randint(0,w-1)
        y = r.randint(0,h-1)
        d,b,l,db,bb,lb,v,ld,lab,ll = scene[x][y]
        b += 1
        scene[x][y] = (d,b,l,db,bb,lb,v,ld,lab,ll)
def distributeLions(amount):
    global scene
    for i in range(amount):
        x = r.randint(0,w-1)
        y = r.randint(0,h-1)
        d,b,l,db,bb,lb,v,ld,lab,ll = scene[x][y]
        l += 1
        scene[x][y] = (d,b,l,db,bb,lb,v,ld,lab,ll)


def inr(x,y):
    if x > w-1:
        x = w-1
    if x < 0:
        x = 0
    if y > h - 1:
        y = h-1
    if y < 0:
        y = 0
    return(x,y)



def badger_search(x,y): #highly inefficient test search
    global scene
    closest = (None,None)
    rp = (0,0)
    cdist = 0
    for rx in xrange(searchR*2):
        for ry in xrange(searchR*2):
            cx = searchR-rx
            cy = searchR-ry
            
            ax = x + cx
            ay = y + cy
            
            ax,ay = inr(ax,ay)
            
            d,b,l,db,bb,lb,v,ld,lab,ll = scene[ax][ay]
            #l += 1
            scene[ax][ay] = (d,b,l,db,bb,lb,v,ld,lab,ll)
            if d+db > 0:
                clx,cly = closest
                if clx == None:
                    closest = (ax,ay)
                    cdist = cx**2 + cy**2
                    rp = (cx,cy)
                    
                else:
                    cdist1 = cx**2 + cy**2
                    #print(searchR-rx,searchR-ry)
                    if cdist1 < cdist:
                        closest = (ax,ay)
                        cdist = cdist1
                        rp = (cx,cy)
                    if cdist1 == cdist and r.randint(0,2) == 1:
                        closest = (ax,ay)
                        cdist = ax**2 + ay**2
                        rp = (cx,cy)
        #
    
    rpx,rpy = rp
    mx= 0
    my = 0
    if rpx != 0:
        mx = rpx/abs(rpx)
    if rpy != 0:    
        my = rpy/abs(rpy)
    return(mx,my)
    
        





def lion_search(x,y): #highly inefficient test search
    global scene
    closest = (None,None)
    rp = (0,0)
    cdist = 0
    for rx in xrange(searchR*2):
        for ry in xrange(searchR*2):
            cx = searchR-rx
            cy = searchR-ry
            
            ax = x + cx
            ay = y + cy
            
            ax,ay = inr(ax,ay)
            
            d,b,l,db,bb,lb,v,ld,lab,ll = scene[ax][ay]
            #l += 1
            scene[ax][ay] = (d,b,l,db,bb,lb,v,ld,lab,ll)
            if b+bb > 0:
                clx,cly = closest
                if clx == None:
                    closest = (ax,ay)
                    cdist = cx**2 + cy**2
                    rp = (cx,cy)
                    
                else:
                    cdist1 = cx**2 + cy**2
                    #print(searchR-rx,searchR-ry)
                    if cdist1 < cdist:
                        closest = (ax,ay)
                        cdist = cdist1
                        rp = (cx,cy)
                    if cdist1 == cdist and r.randint(0,2) == 1:
                        closest = (ax,ay)
                        cdist = ax**2 + ay**2
                        rp = (cx,cy)
        #
    
    rpx,rpy = rp
    mx= 0
    my = 0
    if rpx != 0:
        mx = rpx/abs(rpx)
    if rpy != 0:    
        my = rpy/abs(rpy)
    return(mx,my)







def badgerAI(x,y):
    #print("ai ran",r.randint(0,5))
    
    global scene
    #fill(255)
    #rect(x*rx,y*ry, 5,5)
    #rpf += 1
    d,b,l,db,bb,lb,v,ld,lab,ll= scene[x][y]
    
    mx,my = badger_search(x,y)
    x1 = x + mx
    y1 = y + my
    
    x1,y1 = inr(x1,y1)
    #print(mx,my)
    
    
    b -=1
    if d > 0:
        
        
        rc = r.randint(0,10)
        if rc == 1:
            b += 1
        d-=1
    scene[x][y] = (d,b,l,db,bb,lb,v,ld,lab,ll)
    d1,b1,l1,db1,bb1,lb1,v1,ld1,lv1,ll1 = scene[x1][y1]
    
    if x1 > x or y1 > y:
        bb1 += 1
    else:
        b1 += 1
    #if v1 < v:
    #    bb1 += 1
    #else:
     #   b1 += 1
        
    #b1 += 1
    
    scene[x1][y1] = (d1,b1,l1,db1,bb1,lb1,v1,ld1,lv1,ll1)
    
    


def LionAI(x,y):
    #print("ai ran",r.randint(0,5))
    
    global scene
    #fill(255)
    #rect(x*rx,y*ry, 5,5)
    #rpf += 1
    d,b,l,db,bb,lb,v,ld,lab,ll= scene[x][y]
    
    mx,my = lion_search(x,y)
    x1 = x + mx
    y1 = y + my
    
    x1,y1 = inr(x1,y1)
    #print(mx,my)
    
    
    l -=1
    if b > 0:
        rc = r.randint(0,10)
        if rc == 1:
            l += 1
        b-=1
    scene[x][y] = (d,b,l,db,bb,lb,v,ld,lab,ll)
    d1,b1,l1,db1,bb1,lb1,v1,ld1,lv1,ll1 = scene[x1][y1]
    
    if x1 > x or y1 > y:
        lb1 += 1
    else:
        l1 += 1
    #if v1 < v:
    #    bb1 += 1
    #else:
     #   b1 += 1
        
    #b1 += 1
    
    scene[x1][y1] = (d1,b1,l1,db1,bb1,lb1,v1,ld1,lv1,ll1)

def distribute_food(amount):
    global scene
    for i in xrange(amount):
        x = r.randint(0,w-1)
        y = r.randint(0,h-1)
        d,b,l,db,bb,lb,v,ld,lab,ll = scene[x][y]
        
        d += 10
        
        
        scene[x][y] = (d,b,l,db,bb,lb,v,ld,lab,ll)
        
        
def render_matrix():
    for x in xrange(w):
        for y in xrange(h):
            d,b,l,db,bb,lb,v,ld,lab,ll = scene[x][y]
            #scl = 0
            #if (d+b+l) != 0:
            #    scl = 255/(d+(b+bb)+l)
            if (d != ld)  or (b != lab) or (l != ll):
                if l > 0:
                    fill(0,0,255)    
                elif b > 0:
                    fill(0,255,0)
                elif d > 0:
                    fill(255,0,0)
                else:
                    fill(0)
                
                rect(x*rx,y*ry,rx,ry)
            
            
def re_add_buffers(x,y):
    global scene
    d,b,l,db,bb,lb,v,ld,lab,ll = scene[x][y]
    d += db
    b += bb
    l += lb
    
    scene[x][y] = (d,b,l,0,0,0,v,ld,lab,ll)
    
def run_ai():
    global scene
    for x in xrange(w):
        for y in xrange(h):
            d,b,l,db,bb,lb,v,ld,lab,ll = scene[x][y]
            ld = d+db
            lab = b+bb
            ll = l+lb
            
            for i in xrange(b):
                    badgerAI(x,y)
            for i in xrange(l):
                    LionAI(x,y)
                        #print(x,y)
            d,b,l,db,bb,lb,v,ld,lab,ll = scene[x][y]
           # if b != 0:
            #    print(b)    
            #re_add_buffers(x,y)
            #d,b,l,db,bb,lb,v,lad,lb,ll = scene[x][y]
            v += 1
            scene[x][y] = (d+db,b+bb,l+lb,0,0,0,v,ld,lab,ll)
    #print("end")
            
    

            
def smc(sx,sy): #screen to matrix coordinate converter
    mx = int(round(sx/rx))
    my = int(round(sy/ry))
    mx,my = inr(mx,my)
    return(mx,my)
                                                
def mouseClicked():
    mx,my = smc(mouseX,mouseY)
    d,b,l,db,bb,lb,v,ld,lb,ll = scene[mx][my]
    b += 1
    print(mx,my)
    #scene[mx][my] = (d,b,l,db,bb,lb,v,ld,lb,ll)    
    print(frameRate)                                            
def setup():
    size(pw,ph)
    #frameRate(60)
    noStroke()
    distributeBadgers(500)
    distribute_food(50)
    distributeLions(10)
    render_matrix()


def draw():
    
    global rpf
    #print(rpf)
    #background(0)
    #rpf = 0
    distribute_food(5)
    #distributeBadgers(1)
    #print(frameRate)
    #stroke(255)
    #text(str(frameRate),20,20)
    #noStroke()
    
    #print(getFoodChunk(10,10))
    
    run_ai()
    render_matrix()
    #print(tx,ty)
    
    pass
    
