import math
import numpy as np
import matplotlib.pyplot as plt

#Simulation of a mass spring system undergoing simple harmonic motion.
#Total energy of spring E = 1/2 k x^2 + 1/2 m v^2

def main():
    #Initial conditions
    x0 = 0 #Zero initial displacement
    v0 = 1
    k = 1
    m = 1
    dt = 0.1
    e0 = 0.5 * k * x0**2 + 0.5 * m * v0**2
    
    #Initialise discrete timesteps
    t = np.arange(1000)*dt 
    
    #Intialise empty np array which will contain the values of x, v and e
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    e = np.zeros(len(t))
    
    x[0] = x0
    v[0] = v0
    e[0] = e0
    
    for i in range(len(t)-1):
        x[i+1] = x[i] + dt * v[i]
        v[i+1] = v[i] - dt * k * x[i] / m
        e[i+1] = 0.5 * k * x[i+1]**2 + 0.5 * m * v[i+1]**2
        
    plt.plot(t, x, label="Position x(t)")
    plt.plot(t, v, label="Velocity v(t)")
    #plt.plot(t, e, label="Energy E(t)")
    plt.xlabel("Time/s")
    plt.legend() 
    plt.show()
    
    #x, v and e are noted to be increasing over time
    #This is expected as the euler method is unstable and does not conserve energy.
    
if __name__ == "__main__":
    main()