import numpy as np
import matplotlib.pyplot as plt
import math

#matrizes
C = np.zeros((61,61))
C_ = np.zeros((61,61))

#deltas
delta_t = 0.05
tempo = np.arange(0, 5, delta_t)
delta_x = 0.5
delta_y = 0.5

#u = velocidade correnteza em x
#v = velocidade correnteza em y

#constantes
k = 1
alpha = 1
u = 1
a = 9/1.4
b = 60/(9+5)
#vreal = alpha*sen(pi/5 x)
v = 0
contador = 0
for l in tempo:
    for i in range(0,60):
        for j in range(0,60):
            if l<=2 and i == 30 and j == 30:
                
                contador += 1
                print(contador)
                

                qc = 80/(delta_x*delta_y)
            else:
                qc = 0
            
            termo1direita = C[j][i]
            termo2 = alpha*(C[j][i+1] - C[j][i-1]) / (2*delta_x)
            termo3 = v*(C[j+1][i] - C[j-1][i]) / (2*delta_y)
            termo4 = k*((C[j][i+1]-(2*C[j][i])+C[j][i-1])/delta_x**2)
            termo5 = k*((C[j+1][i]-(2*C[j][i])+C[j-1][i])/delta_y**2) 
            C_[j][i] = delta_t*( termo5 + termo4 - termo3 - termo2 + qc) + (termo1direita)
            
            if C_[j][i] < 0:
                C_[j][i] = 0

            
    C = np.copy(C_)

plt.imshow(C_, vmin = 0, vmax = 1, extent = (0,30,0,30))
plt.colorbar()
plt.show()



#Condições de contorno
C[0][1:40] = C[1][1:40]
C[60][1:40] = C[59][1:40]
C[1:60][0] = C[1:60][1]
C[1:60][40] = C[1:60][39]

print(C[40][40])