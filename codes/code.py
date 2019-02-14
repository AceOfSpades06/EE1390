import numpy as np 
import matplotlib.pyplot as plt
len = 1000
r = np.sqrt(37)              #radius of the given circle
A = np.array([0,-6])         #centre of the circle
R= np.array([2,-4])          #nearest point to the centre of given circle
Z = np.zeros((2,len))
Y = np.zeros((2,len))
X = np.zeros((2,len))
N = np.zeros((2,len))
p = np.linspace(-20,20,len)
t = np.linspace(0,2*np.pi,len)
coeff = [4,0,2,6]          #normal equation is y+tx=4t+2t^3 and passes through centre of circle
H = np.roots(coeff)
S = np.real(H[np.isreal(H)])        #slope of the normal
r1= np.sqrt(((A[0]-R[0])**2)+((A[1]-R[1])**2))                #radius of required circle
for i in range(len):
	Z[:,i] = [(p[i]**2)/8,p[i]]                               #parabola in matrix form
	Y[:,i] = [A[0]+r*np.cos(t[i]),A[1]+(r*np.sin(t[i]))]      #given circle
	X[:,i] = [R[0]+r1*np.cos(t[i]),R[1]+(r1*np.sin(t[i]))]    #required circle
	N[:,i] = A + p[i]*(S)               #normal line at point R
plt.title('circle with centre on parabola passing through centre')
plt.plot(Z[0,:],Z[1,:],label = '$y^2=8x$')
plt.plot(Y[0,:],Y[1,:],label = '$x^2+y^2+12Y=1$')
plt.plot(X[0,:],X[1,:],label = '$(x-2)^2+(y+4)^2=8$')
plt.plot(N[0,:],N[1,:],label = '$y-x+6=0$')
plt.plot(A[0],A[1],'ro')
plt.plot(R[0],R[1],'ro')
print('r1 is distance from centre of circle to (2,-4) on parabola =',r1)       #shortest distance from the centre of the circle
plt.grid()
plt.legend(loc='best')
plt.show()
