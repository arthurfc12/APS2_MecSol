import numpy as np
import matplotlib.pyplot as plt
import math

#matrizes
C = np.zeros((41,61))
C_ = np.zeros((41,61))

#deltas
delta_t = 0.05
tempo = np.arange(0, 30, delta_t)
delta_x = 0.5
delta_y = 0.5

#constantes
k = 1
alpha = 1
u = alpha
a = 9/1.4
b = 60/(9+5)



for l in tempo:
    for i in range(0,60):
        for j in range(0,40):
            if l<=3 and i == 9 and j == 13:
                qc = 100/(delta_x*delta_y)
            else:
                qc = 0

            v = alpha*math.sin((math.pi / 5) * j)
            
            termo1direita = C[j][i]
            termo2 = u*(C[j][i+1] - C[j][i-1]) / (2*delta_x)
            termo3 = v*(C[j+1][i] - C[j-1][i]) / (2*delta_y)
            termo4 = k*((C[j][i+1]-(2*C[j][i])+C[j][i-1])/delta_x**2)
            termo5 = k*((C[j+1][i]-(2*C[j][i])+C[j-1][i])/delta_y**2) 
            C_[j][i] = delta_t*( termo5 + termo4 - termo3 - termo2 + qc) + (termo1direita)
            
            if C_[j][i] < 0:
                C_[j][i] = 0

            #Condições de contorno
            if j == 0:
                C_[0][i] = C_[1][i]
            elif j == 40:
                C_[40][i] = C_[39][i]
            elif i == 0:
                C_[j][0] = C_[j][1]
            elif i == 60:
                C_[j][60] = C_[j][59]
            
    C = np.copy(C_)


plt.imshow(C, vmin = 0, vmax = 1, extent(0,,0,))
plt.colorbar()
plt.show()