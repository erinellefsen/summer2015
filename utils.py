from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from scipy.optimize import brentq

def plot_implicit2d(fn, rangeX=(0,4),rangeY=(0,1),ax=None):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    xmin, xmax = rangeX
    ymin, ymax = rangeY

    A = np.linspace(xmin, xmax, 250) # resolution of the contour
    B = np.linspace(ymin, ymax, 250) # number of slices
    A1,A2 = np.meshgrid(A,B) # grid on which the contour is plotted

    
    X,Y = A1,A2
    #print(len(X)," ",len(Y))
    Z = fn(X,Y)
    #print(Z+z)
    cset = ax.contour(X, Y, Z, [0], zdir='z')
    # [z] defines the only level to plot for this contour for this value of z

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    #ax.set_zlim3d(zmin,zmax)
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    return fn.func_name
    
    
def continuousInfection(x=None,y=None,N=2000,nu=0): #CHECK THIS OUT AND DON'T FORGET THAT SOME ARE VACCINATED
    if y == None and x != None:
        
        g = lambda z: np.log((2000-1-nu)/(2000*(1-z)-nu))-x*z if z != 1 else 1
        return g
    elif x == None:
        g = lambda z: np.log((2000-1-nu)/(2000*(1-z)-nu))-z*y if z != 1 else 1
        return g
    else:
        return np.log((2000-1-nu)/(2000*(1-y)-nu))-x*y

def continuousInfection2(x,y=None,N=2000,nu=400): #CHECK THIS OUT AND DON'T FORGET THAT SOME ARE VACCINATED
    return (np.log((2000-1-nu)/(2000*(1-y)-nu))-x*y)

def continuousInfection4(x,y=None,N=2000,nu=800): #CHECK THIS OUT AND DON'T FORGET THAT SOME ARE VACCINATED
    return (np.log((2000-1-nu)/(2000*(1-y)-nu))-x*y)

def continuousInfection6(x,y=None,N=2000,nu=1200): #CHECK THIS OUT AND DON'T FORGET THAT SOME ARE VACCINATED
    return (np.log((2000-1-nu)/(2000*(1-y)-nu))-x*y)


def plot_implicit3d(fn, bbox=(0,5)):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    #xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    xmin, xmax = 0,15
    ymin,ymax = 0,1900
    zmin,zmax =0,1
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    M = np.linspace(xmin, xmax, 100) # resolution of the contour 
    N = np.linspace(ymin, ymax, 100)
    B = np.linspace(0, 150, 150) # number of slices
    A1,A2 = np.meshgrid(M,N) # grid on which the contour is plotted
    #What do we want the grid to be to get the whole graph?
    
    Bx= np.linspace(xmin, xmax, 150)
    By= np.linspace(ymin, ymax, 150)
    Bz = np.linspace(zmin, zmax, 150)  
    
    colorLst = ['lightgreen', 'green', 'blue', '#afeeee']
    acc =0
    for z in Bz: # plot contours in the XY plane
        #print(acc)
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z',colors=(colorLst[acc%4]))
        # [z] defines the only level to plot for this contour for this value of z
        acc +=1
                                                           
    for y in By: # plot contours in the XZ plane
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y',colors=('green', 'green', 'blue', (1,1,0), '#afeeee', ))

    for x in Bx: # plot contours in the YZ plane
        Y,Z = A1,A2
        X = fn(x,Y,Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x',colors=('blue', 'green', 'blue', (1,1,0), '#afeeee', '0.5'))

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    ax.set_zlim3d(zmin,zmax)    
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)

def eq( a, b, eps=0.000001 ):
    return abs(a - b) <= eps


def calcRSquared(f,popt,xLst,yLst): #input: function, xlist and y list 
    SSreg = calcSSreg(f,popt,xLst,yLst)
    SStot = calcSStot(yLst) #mean
    print(SSreg,SStot)
    return 1- (SSreg/SStot)

def calcSSreg(f,popt,xLst,yLst):
    res = 0
    for i in range(len(xLst)):
        x = xLst[i]
        yGuess = yLst[i]
        temp = yGuess - f(x,*popt) 
        res += temp**2
    return res
def calcSStot(yLst):
    res = 0
    mean = np.mean(yLst)
    for i in yLst:
        res += (mean-i)**2
    return res


def calcRSquaredImplicit(f,xLst,yLst):
    
    SSreg = calcSSregImplicit(f,xLst,yLst) #8.6
    SStot = calcSStot(yLst) #3.5
    print(SSreg,SStot)
    return 1- (SSreg/SStot)
        
def calcSSregImplicit(f,xLst,yLst):
    res = 0
    for i in range(len(xLst)):
        x = xLst[i]
        yGuess = yLst[i]
        g = f(x=x) #return a single variable function
        yReal = brentq(g,0,1)
        temp = yReal-yGuess
        res += temp**2
    return res