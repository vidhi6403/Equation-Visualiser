import json
from random import randint
import math
from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector import curl
import mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import axes3d
from sympy.vector import CoordSys3D
from sympy import symbols
import matplotlib.pyplot as plt
import numpy as np
R = ReferenceFrame('R')

with open('quotes.json') as f:
 data = json.load(f)

random_no = randint(0,10)
print('"',data[random_no]['text'],'"')
print("\t - ",data[random_no]['author'])

def plot_field(u,v,w,i,j,k,l):
 fig = plt.figure()
 ax = fig.gca(projection='3d')

 i, j, k = np.meshgrid(np.arange(-x, x, 1),
    np.arange(-y, y, 1),
    np.arange(-z, z, 1))

 ax.quiver(i, j, k, u, v, w, length=l)


 plt.show()

operations = ["Intensity(H)","Density(B)","Current Density(J)"]
Mu = 4*math.pi*10**-7
print("Enter Any of the follwing paramater to be calculated:")
for i in range(len(operations)):
 print(i+1,"-",operations[i])
to_cal = int(input("Enter here:")) - 1

print(f"\n\nEnter Any of the follwing paramater from {operations[to_cal]} to be calculated:")
for i in range(0,2):
 if operations[i] != operations[to_cal]:
    print(i,"-",operations[i])
from_cal = int(input("Enter here:"))

print("This solver works with 2-D or 3-D, therfore enter equation in terms of x,y,z.")
print("R_x - R[0], R_y - R[1], R_z - R[2]")
Sx = eval(input("Enter Sx:"))
Sy = eval(input("Enter Sy:"))
Sz = eval(input("Enter Sz:"))

 # print("input field")
 # plot_field(str(Sx),str(Sy),str(Sz))

if to_cal == 1 or to_cal == 2 or to_cal == 3:
 x = float(input("\n\nEnter evaluate at x = "))
 y = float(input("Enter evaluate at y = "))
 z = float(input("Enter evaluate at z = "))

if to_cal == 0:
 # Magnetic Flux Intensity
 print(Sx,"+",Sy,"+",Sz)

 try:
    Sx = str(eval(str(Sx).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z)))/Mu)
 except:
    pass
 try:
    Sy = str(eval(str(Sy).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z)))/Mu)
 except:
    pass
 try:
    Sz = str(eval(str(Sz).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z)))/Mu)
 except:
    pass
 print("H = ",(Sx+ "*R.x+"+Sy+ "*R.y+"+Sz+ "*R.z"),"A/m")
 plot_field(Sx,Sy,Sz,x,y,z,0.1)

elif to_cal == 1:
 # Magnetic Flux Density
 print(Sx,"+",Sy,"+",Sz)
 try:
    Sx = str(eval(str(Sx).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z)))*Mu)
 except:
    pass
 try:
    Sy = str(eval(str(Sy).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z)))*Mu)
 except:

    pass
 try:
    Sz = str(eval(str(Sz).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z)))*Mu)
 except:
    pass

 print("B = ",(Sx+ "*R.x+"+Sy+ "*R.y+"+Sz+ "*R.z"),"Wb/m^2 or Tesla")
 plot_field(Sx,Sy,Sz,x,y,z,0.0001)

elif to_cal == 2:
 # Current Density
 if from_cal == 2:
    Sx = str(Sx)+str((1/Mu))
    Sy = str(Sy)+str((1/Mu))
    Sz = str(Sz)+str((1/Mu))
 J = curl(Sx*R.x+Sy*R.y+Sz*R.z, R)
 print("J = ",J,"A/m^2")
 #J =str(J)
 try:
    Sx = J.split("*R.x")[0]
 except:
    pass
 try:
    Sy = (J.split("*R.y")[0]).split("R.x")[1]
 except:
    pass
 try:
    Sz = (J.split("*R.z")[0]).split
 except:
    pass

 try:
    Sx = str(eval(str(Sx).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z))))
 except:
    pass
 try:
    Sy = str(eval(str(Sy).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z))))
 except:
    pass
 try:
    Sz = str(eval(str(Sz).replace('R_x',str(x)).replace('R_y',str(y)).replace('R_z',str(z))))
 except:
    pass

 print(f'J = {str(Sx)}*R.x+{str(Sy)}*R.y+{str(Sz)}*R.z A/m^2 at x ={x},y={y},z={z}')
 plot_field(Sx,Sy,Sz,x,y,z,0.1)
