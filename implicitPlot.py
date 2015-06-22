from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def plot_implicit2d(fn, rangeX=(0,4),rangeY=(0,1),ax=None):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    xmin, xmax = rangeX
    ymin, ymax = rangeY

    A = np.linspace(xmin, xmax, 1000) # resolution of the contour
    B = np.linspace(xmin, xmax, 15) # number of slices
    A1,A2 = np.meshgrid(A,A) # grid on which the contour is plotted

    for z in B: # plot contours in the XY plane
        X,Y = A1,A2
        Z = fn(X,Y)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z')
        # [z] defines the only level to plot for this contour for this value of z

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    #ax.set_zlim3d(zmin,zmax)
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    
    
def continuousInfection(x,y,N=2000):
    return (np.log((N-1)/(N*(1-y)))-x*y)