import random as r

#flowers, badgers, lions, buffer flowers, buffer badgers, buffer lions, cell version,last flowers, last badgers, last lions
def matrix(x,y):
  out = []
  #print(x,y)
  for i in range(x):
    out.append([(0,0,0,0,0,0,0,0,0,0)]*y)
    
  return(out)
def matrix2(x,y):
  out = []
  #print(x,y)
  for i in range(x):
    out.append([0])
    
  return(out)
w = 500 #width of matrix
h = 500 #height of matrix

pw = 1000 #width of display
ph = 1000 #height of display

rx = pw/w #width of a grid square
ry = ph/h #height of a grid square


foodChunkWidth = 100
foodChunkHeight = 100


cw = w/foodChunkWidth
ch = h/foodChunkHeight
foodC = matrix2(foodChunkWidth,foodChunkHeight)
scene = matrix(w,h)



def getFoodChunk(x,y):
    xpos = floor(x/cw)
    ypos = floor(y/ch)
    print(xpos,ypos)
    
    
    
    
    
    


def distributeBadgers(amount):
    global scene
    for i in range(amount):
        x = r.randint(0,w-1)
        y = r.randint(0,h-1)
        d,b,l,db,bb,lb,v,ld,lb,ll = scene[x][y]
        b += 1
        scene[x][y] = (d,b,l,db,bb,lb,v,ld,lb,ll)


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


def badgerAI(x,y):
    global scene
    d,b,l,db,bb,lb,v,ld,lb,ll= scene[x][y]
    x1 = x+ r.randint(-1,1)
    y1 = y + r.randint(-1,1)
    x1,y1 = inr(x1,y1)
    b -=1
    scene[x][y] = (d,b,l,db,bb,lb,v,ld,lb,ll)
    d1,b1,l1,db1,bb1,lb1,v1,ld1,lv1,ll1 = scene[x1][y1]
    
    if v1 < v:
        db1 += 1
    else:
        b1 += 1
        
   
    scene[x1][y1] = ((d1,b1,l1,db1,bb1,lb1,v1))
    

def distribute_food(amount):
    global scene
    for i in range(amount):
        x = r.randint(0,w-1)
        y = r.randint(0,h-1)
        d,b,l,db,bb,lb,v,ld,lb,ll = scene[x][y]
        
        d += 1
        
        
        scene[x][y] = (d,b,l,db,bb,lb,v,ld,lb,ll)
        
        
def render_matrix():
    for x in range(w):
        for y in range(h):
            d,b,l,db,bb,lb,v,ld,lb,ll = scene[x][y]
            scl = 0
            if (d+b+l) != 0:
                scl = 255/(d+b+l)
            fill(d*scl,b*scl,l*scl)
            rect(x*rx,y*ry,rx,ry)


def re_add_buffers(x,y):
    d,b,l,db,bb,lb,v,ld,lb,ll = scene[x][y]
    d += db
    b += bb
    l += lb
    scene[x][y] = (d,b,l,db,bb,lb,v,ld,lb,ll)
    
def run_ai():
    for x in range(w):
        for y in range(h):
            d,b,l,db,bb,lb,v,ld,lb,ll = scene[x][y]
            
            
            for i in range(b):
                badgerAI(x,y)
            re_add_buffers(x,y)
            d,b,l,db,bb,lb,v,ld,lb,ll = scene[x][y]
            v += 1
            scene[x][y] = (d,b,l,db,bb,lb,v,ld,lb,ll)

            
                        
                                                
def setup():
    size(500,500)
    distribute_food(100)
    render_matrix()


def draw():
    distribute_food(1)
    distributeBadgers(1)
    render_matrix()
    #print(getFoodChunk(10,10))
    run_ai()
    pass
    
