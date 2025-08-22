import math
import numpy as np
import matplotlib.pyplot as plt

#Simulation of a mass spring system undergoing simple harmonic motion.
#Total energy of spring E = 1/2 k x^2 + 1/2 m v^2

def verlet(x_prev, x_curr, dt, m, k):
    x_next = 2*x_curr - x_prev - (k*x_curr*dt**2)/m
    return x_next

def simulate(dt, m, k, steps=1000, eps=100):
    x = np.zeros(1000)
    x[0] = 0
    x[1] = 1*dt
    
    for i in range(1, steps-1):
        x[i+1] = 2*x[i]-x[i-1]-(k*x[i]*dt**2)/m
        
        if x[i+1] > eps:
            return False
    return True

def main():
    #Initial conditions
    x0 = 0 #Zero initial displacement
    v0 = 1
    k = 1
    m = 1
    dt = 0.1
    e0 = 0.5 * k * x0**2 + 0.5 * m * v0**2
    
    #Initialise discrete timesteps
    t = np.arange(0, 20, dt)
    
    #Intialise empty np array which will contain the values of x, v and e
    x = np.zeros(len(t))
    v = np.zeros(len(t))
    e = np.zeros(len(t))
    
    #Verlet integrator requires two initial values
    x[0], x[1] = x0, x0+v0*dt
    v[0], v[1] = v0, v0
    e[0], e[1] = e0, e0
    
    for i in range(1, len(t)-1):
        x[i+1] = 2*x[i]-x[i-1]-(k*x[i]*dt**2)/m
        v[i] = (x[i+1]-x[i-1])/(2*dt) #more accurate, less fluctuation in energy
        #v[i+1] = (x[i+1]-x[i])/dt   
        e[i] = 0.5 * k * x[i]**2 + 0.5 * m * v[i]**2
    
    print(e)
    #plt.plot(t, x, label="Position x(t)")
    #plt.plot(t, v, label="Velocity v(t)")
    plt.plot(t, e, label="Energy E(t)")
    plt.xlabel("Time/s")
    plt.legend() 
    plt.show()
    
    #For the verlet integrator, energy is noticed to vary sinusoidally, 
    # but is stable below a certain value, to be determined.
    
def test(): #To find critical dt value beyond which verlet integrator is unstable
    start = 0.1
    end = 3.0
    step = 0.01
    dt = start
    m = 1
    k = 1
    while dt <= end:  
        stable = simulate(dt, m, k)
        if not stable:
            print(dt)
            break
        dt += step
        

if __name__ == "__main__":
    #main()
    test() #numerically testing the critical timestep value is 2.00 (for eps=100)