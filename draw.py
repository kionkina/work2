from display import *


def draw_line( x0, y0, x1, y1, screen, color ):
    # OCTANT 1


    A = y1-y0
    B = -1*(x1-x0)
#swapping x and y coordinates if x is decreasing to use same formula for different octants
    if B >= 0:
        oldx1 = x1
        oldy1 = y1
        oldx0 = x0
        oldy0 = y0
        x1 = oldx0
        y1 = oldy0
        x0 = oldx1
        y0 = oldy1
    x = x0
    y = y0
    A = y1-y0
    B = -1*(x1-x0)
    print "x0: " + str(x0)
    print "y0: " + str(y0)
    print "x1: " + str(x1)
    print "y1: " + str(x1)
    print "plotting: " + str(x) + " , " + str(y)
    plot(screen, color, x0, y0)
    print "A: " + str(A)
    print "B: " + str(B)
    #OCTANT I and V ==> the slope is less than or equal to one and positive
    if (A>0 and B<=0 and A<=-B):
        d=2*A+B
        while (x < x1):
            plot(screen, color, x, y)
            print "x: "+str(x)
            print "y: "+str(y)
            if (d > 0):
                y+=1
                d+=(2*B)
  
            x+=1
            d+=(2*A)
    #OCTANT II and VI==> the slope is greater than one and positive
    elif (B<=0 and A>=0 and A>=-B):
        print "case 2 ------"
        d=2*B+A
        while (y < y1):
            plot(screen, color, x, y)
            print "x: "+str(x)
            print "y: "+str(y)
            if (d<0):
                x+=1
                d+=2*A
            y+=1
            d+=2*B
    #OCTANT III and VII ==> slope is between -1 and 0
    elif (A<=0 and B<=0 and -A>=-B): #realized this is not the same as A<=B
        print "case 3 -----"
        d=(-2*B)+A
        while (y > y1):
            plot(screen, color, x,y)
            print "x: "+str(x)
            print "y: "+str(y)
            if (d>0):
                x+=1
                d+=2*A
            y-=1
            d-=2*B
    #VIII and IV slope is less than -1
    else:
        d=2*A-B
        while(x<x1):
            plot(screen,color,x,y)
            if(d<0):
                y-=1
                d-=2*B
            x+=1
            d+=2*A
    plot(screen, color, x1, y1)
    print "x1: " + str(x1)
    print "y1: " + str(y1)



def superman(screen, color):
    for i in xrange(0,500, 3):
        draw_line(250,0, 500-i, 250, screen, color)
    for i in range(10):
        draw_line(250, 0+i, 500-i, 250, screen, [225,0,0])
        draw_line(250, 0+i, i, 250, screen, [225,0,0])
    for i in xrange(0,130,2):
        draw_line(0,250,100,250+i,screen,color)
    for i in xrange(0,130,2):
        draw_line(500,250,400,250+i,screen,color)
    for i in range(10):
        draw_line(0+i,250, 100, 380-i, screen, [255,0,0])
    for i in range(10):
        draw_line(500-i, 250, 400, 380-i, screen, [255,0,0])
    for i in xrange(0,130, 2):
        draw_line(100, 250+i, 400, 250+i, screen, color)
    for i in range(10):
        draw_line(100, 380-i, 400, 380-i, screen, [255,0,0])
