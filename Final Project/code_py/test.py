import numpy as np
from numpy import loadtxt
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math as mat

#parameters


# initial conditions (here, and final)
#x1 = 0
#y1 = 0
#x2 = 
#y2 = 

def abs(x):
    if x<0:
        return -1*x
    else:
        return x

def lorenz(s, r, b):
    def diffeqs(w, t, p):
        [x, y, z] = w # d matrix
        [s, r, b] = p # parameters
        #if y/((2*a)-y) >= 0:
        der = [s*(y - x),
               r*x - y - x*z,
               x*y - b*z]
        #else:
            #der = [np.sqrt(abs((y/((2*a)-y)))), 1]
        return der

        # time scale
    t = np.linspace(0, 100, 100000)

    #print(1/((4*C)**(1/2)))

    # containing parameters and initial conditions
    p = [s, r, b]
    w0 = [0, 1, 0]

    wsol = odeint(diffeqs, w0, t, args = (p, ))
    plt.plot(wsol[:, 0], wsol[:, 2])
    #print(wsol[:, 0])
# THIS FIXES THE HALF-GRAPHS, IGNORE FOR NOW.
'''
    y1 = []
    for i in range(0, len(wsol[:, 1])):
        if i>2 and wsol[i, 1] != 0:
            y1.append(-1*wsol[i, 1])

    y2 = []
    for i in range(0, len(y1)):
        y2.append(y1[-1*(i+1)])
    
    y1.pop()

    y3 = y1 + y2

    x1 = []
    for i in range(0, len(wsol[:, 0])):
        if i>2 and wsol[i, 0] != 0:
            x1.append(wsol[i, 0])

    x2 = []
    for i in range(0, len(x1)):
        x2.append(-1*x1[-1*(i+1)] + 2*np.pi*a)

    x1.pop()
    x2[0] = np.pi

    x3 = x1 + x2

    #print(x3)
    #print(len(x1), len(y3))
    #print(x1[1993])

    #plt.figure(figsize=(100, 100))
    #ax = plt.gca() #you first need to get the axis handle
    #ax.set_aspect() #sets the height to width ratio to 1.5. 
    
    plt.plot(x3, y3, 'k-')
    #plt.xlabel('x')
    #plt.ylabel('y')
'''
#for a in np.linspace(1, 10, 30): #np.linspace(0, 100, 50):
#for a in range(0, 20):
    #for b in range(0, 20):
lorenz(10, 28, 8/3)

plt.show()