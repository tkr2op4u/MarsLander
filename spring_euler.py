import math
import numpy as np
import matplotlib.pyplot as plt

#Simulation of a mass spring system undergoing simple harmonic motion.
#Total energy of spring E = 1/2 k x^2 + 1/2 m v^2

def main():
    #Initial conditions
    x0 = 0 #Zero initial displacement
    v0 = 1
    k = 10
    m = 0.1
    dt = 0.005
    
    #Initialise discrete timesteps
    t = np.arange(1000)*dt 
    
    #Intialise empty np array which will contain the values of x and v
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    
    x[0] = x0
    v[0] = v0
    
    for i in range(len(t)-1):
        x[i+1] = x[i] + dt * v[i]
        v[i+1] = v[i] - dt * k * x[i] / m
        
    plt.plot(t, x)
    plt.plot(t, v)
    plt.show()
    
if __name__ == "__main__":
    main()