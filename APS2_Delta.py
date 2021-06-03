# Grupo 9 - APS 2 - APS DELTA


##||Imports|##
import numpy as np
import matplotlib.pyplot as plt
from math import sin,pi

##|Set variables|##
k=1
n=9
alpha=1
T=3
Q_ponto=100
lx=30
ly=20
a=6
b=5
u=alpha
delta_x=0.5
delta_y=0.5
delta_t=0.05


##|Create an array filled with zeros|##
##|in this case is a Matrix with 602 ATs, 60 lines and 40 columns,
##|being the river in 30 seconds of time.
##|Ex:matrix[time, i(x/line), j (y/column)]
C = np.zeros((602, 61, 41))


for p in range(0,601):
    for i in range(1,60):
        for j in range(1,40):
            v = alpha*sin(pi/5*i)
            ##|Burgers equation in each point for a certain amount of time|##
            if i == a*2 and j == b*2 and p <= 60: 
                # print(i)
                C[p+1,i,j] = C[p,i,j] + delta_t * (Q_ponto/(delta_x*delta_y) - u*((C[p,i+1,j]-C[p,i-1,j])/(2*delta_x)) - \
                    v*((C[p,i,j+1]-C[p,i,j-1])/(2*delta_y)) + k*((C[p,i+1,j]-2*C[p,i,j] + C[p,i-1,j])/(delta_x**2)) + \
                    k*((C[p,i,j+1] -2*C[p,i,j] +C[p,i,j-1])/(delta_y**2)) )     
            
            else:
                C[p+1,i,j] = C[p,i,j] + delta_t * (- u*((C[p,i+1,j]-C[p,i-1,j])/(2*delta_x)) - \
                    v*((C[p,i,j+1]-C[p,i,j-1])/(2*delta_y)) + k*((C[p,i+1,j]-2*C[p,i,j] + C[p,i-1,j])/(delta_x**2)) + \
                    k*((C[p,i,j+1] -2*C[p,i,j] +C[p,i,j-1])/(delta_y**2)) )  
            
            if C[p+1,i,j] < 0:
                C[p+1,i,j] = 0
    
        

##|Few ajustments|##
C[:,0,:] = C[:,1,:]
C[:,60,:] = C[:,59,:]
C[:,:,0] = C[:,:,1]
C[:,:,40] = C[:,:,39]

#print(C[121,40,60])

#fig, ax = plt.subplots()

#print(C_transpose)


##|Print tools|##      
time = 4
##|Show the river with colour in a certain time, being between 0 and 601.
plt.imshow(C[time].T, cmap='viridis',vmax=1,extent=[0,30,0,20], origin='lower')
# ax.axis([0, 30, 0, 30])
plt.colorbar()
plt.show()




