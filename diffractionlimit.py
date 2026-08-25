import numpy as np 
import matplotlib.pyplot as plt 

#Bessel function using trapezium rule
def J(m, x):
    N = 10000
    theta = np.linspace(0, np.pi, N)
    h = np.pi/(N - 1)
    
    y = np.cos(m*theta - x*np.sin(theta))
    
    #Using the trapezium rule
    s = 0.5*y[0] + 0.5*y[-1]
    for i in range(1, N-1):
        s += y[i]
        
    return (h * s) / np.pi

#Defining values 
lamda = 5.5e-7
f_ratio = 10 

a = 1e-3 
R = 2*a*f_ratio 

#r range = +- 25 micrometers 
r_values = np.linspace(-25e-6, 25e-6, 200) 

I = [] 

#Calculating intensity 
for r in r_values: 
    x = (2*np.pi/lamda) * a * (r/R) 

    if abs(x) < 1e-12: 
        I.append(1)
    else: 
        J1_value = J(1, x) 
        I.append((2*J1_value/x)**2) 
 

#Plotting the graph 
plt.plot(r_values*1e6, I) 
plt.xlabel("r (micrometres)") 
plt.ylabel("Diffraction pattern") 
plt.grid() 
plt.show() 
