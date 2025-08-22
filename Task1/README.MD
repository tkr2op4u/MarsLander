# Assignment 1: Numerical Dynamics in One Dimension

This and the next assignment are best done in Python. The first step is to learn to simulate something simple.

Consider a mass \( m \) at the end of a simple harmonic (massless) spring of strength \( k \) in one dimension. The energy of the system is given by the sum of the kinetic and potential energies:

\[
E = \frac{1}{2} k x^2 + \frac{1}{2} m v^2
\]

where \( x \) is the displacement and \( v \) is the velocity of the mass, which are functions of time. The force on the mass is the negative of the derivative of the potential energy with respect to position, so the equations of motion are:

\[
\dot{v} = \frac{F}{m} = - \frac{1}{m} \frac{\partial E}{\partial x} = - \frac{kx}{m}
\]

\[
\dot{x} = v
\]

In this first assignment, you have to write a program that integrates these equations from an initial condition (e.g., \( x(0) = 0, v(0) = v_0 \)). The integration will have to be done approximately, using a discrete time step \(\Delta t\). You will have to adjust the value of \(\Delta t\) empirically. If it is too small the program takes too long to run, and if it is too large the integration becomes numerically unstable due to accumulating inaccuracies, and the dynamical variables will take on unfeasible values (e.g., the amplitude of the oscillations will grow in time, even though no energy is supplied to the system).

You should investigate two different ways of discretizing the trajectory. To obtain the first one, let us expand the dynamical variables in Taylor series around a particular point \( t \) in time, e.g. for \( x \):

\[
x(t + \Delta t) = x(t) + \Delta t \frac{\partial x}{\partial t} + O(\Delta t^2) = x(t) + \Delta t v(t) + O(\Delta t^2)
\]

and similarly for \( v \):

\[
v(t + \Delta t) = v(t) + \Delta t \frac{\partial v}{\partial t} + O(\Delta t^2) = v(t) + \Delta t \frac{F(t)}{m} + O(\Delta t^2) = v(t) - \Delta t \frac{k x(t)}{m} + O(\Delta t^2)
\]

Using these equations, you can obtain the values of the dynamical variables at time \( t + \Delta t \) from their values at time \( t \), and this algorithm is called the **Euler method**. At each step, the error in your integration will be of the order \(\Delta t^2\), or alternatively, the trajectory will be accurate to order \(\Delta t\): this is a “first order” integrator and is rather inaccurate.

If we truncate the Taylor expansion beyond the second order term, we get a better Euler method, which is accurate to second order. However, with a little trick, we can do even better without increasing the complexity.

Let us again expand the dynamical variables in Taylor series, but now both forwards and backwards in time:

\[
x(t - \Delta t) = x(t) - \Delta t \frac{\partial x}{\partial t} + \frac{\Delta t^2}{2!} \frac{\partial^2 x}{\partial t^2} - \frac{\Delta t^3}{3!} \frac{\partial^3 x}{\partial t^3} + O(\Delta t^4)
\]

\[
x(t + \Delta t) = x(t) + \Delta t \frac{\partial x}{\partial t} + \frac{\Delta t^2}{2!} \frac{\partial^2 x}{\partial t^2} + \frac{\Delta t^3}{3!} \frac{\partial^3 x}{\partial t^3} + O(\Delta t^4)
\]

Adding the two expansions, we get

\[
x(t - \Delta t) + x(t + \Delta t) = 2 x(t) + \Delta t^2 \frac{\partial^2 x}{\partial t^2} + O(\Delta t^4)
\]

from which an update rule can be extracted:

\[
x(t + \Delta t) \approx 2 x(t) - x(t - \Delta t) + \Delta t^2 \frac{F(t)}{m}
\]

This is the **Verlet integrator**, which uses two previous values of the position to estimate the next one. Notice that it does not make use of the velocity directly. For analysis purposes, an estimate of the velocity can be obtained from the trajectory:

\[
v(t) = \frac{1}{2 \Delta t} \left[ x(t + \Delta t) - x(t - \Delta t) \right] + O(\Delta t^2)
\]

This velocity estimate is one step behind the position estimate. It is possible to estimate \( v(t + \Delta t) \), thus synchronizing the two estimates, but only at the expense of accuracy:

\[
v(t + \Delta t) = \frac{1}{\Delta t} \left[ x(t + \Delta t) - x(t) \right] + O(\Delta t)
\]
