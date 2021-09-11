import path_setup
#setup path to include external recourses
nb_dir = path_setup.path_setup()
data_dir = nb_dir + '/Data/'

# The modules used for actually crunching the simulation numbers (nDim_Symbolic_Function, Integrator) were made by me and are
# covered under the MIT free license. Please respect these terms and keep the license file with the code, Thank you!

import nDim_Symbolic_Function as vfunc
import matplotlib.pyplot as plt
import Integrator as numInt
import matplotlib as mpl
import sympy as sym
import numpy as np
import torch
import math

# this is a major player in computational speed using c evaluatable lambda functions
# Without this module, we lose about on the highend, on the order of 100 cpu cycles to return a result fronm python vs c lambdas
from sympy.utilities.lambdify import lambdastr 
# set output precision so as to not spam the screen with long numbers
np.set_printoptions(precision=2)
# needs ipympl for realtime interactive displays using vs code
from IPython.display import display, Markdown, Latex
# Shebang line for interactive output in vs_code, comment this out if you have troubles running the notebook
# %matplotlib widget

t = sym.symbols('t')

# Sympy Functions
x = sym.Function('x')(t)
y = sym.Function('y')(t)
z = sym.Function('z')(t)

dxdt = x.diff(t)
dydt = y.diff(t)
dzdt = z.diff(t)

Cd = 0.35       # unitless coefficent of drag : https://blogs.fangraphs.com/exploring-the-variation-in-the-drag-coefficient-of-the-baseball/
# according to this websight, the values of the Cd for a baseball depending on the season using a typical regulation baseball range from around
# 0.3 to o.375 (unitless), So I will be using a 0.35 for Cd. This differs from the 0.45 of a perfect sphere due to surface imperfections causing
# turbulance similar to a golfball, thereby lowering the Cd.
rho = 1.205     # kg/m^3 <=> 1.205 g/L : this is the density of air at astp
S_a = 0.004145  # m^2 : this is the minimum cross-sectional area of a regulation baseball, it was supprising to me that the top end of this can be 
# as much as 5% greater! A bit of a loose regulation if you ask me!
drag_const = Cd*rho*S_a/2 # this is the constant for the drag equation
print(f'The drag constant is equal to {drag_const} kg/m')

# Force components in cartesian coords set equal to the mass times the acceleration and then later integrated numerically
Fx = - drag_const*dxdt**2
Fy = - drag_const*dydt**2
Fz = - 9.81 - drag_const*dzdt**2 # assuming nominal Earth gravity in meters per second

F_ = vfunc.nDim_Symbolic_Function([Fx,Fy,Fz],[dxdt,dydt,dzdt],[[dxdt],[dydt],[dzdt]])

real_time = int(input('Enter durration of (positive integer) time in seconds to simulate: '))

dt = 2.5E-03# seconds

# The variable time_slice sets the output frequency so that we are not capturing more data then needed from the
# simulation, IE we dont need to follow the baseball every millimeter, but looking at it in say 5 centimeter
# increments is much less data by an order of magnitude or more, but gives a proper picture of the ball moving overall
# With this in mind, I set the output time step at 1 second after a little bit of experimenting and this seems to be a
# good compromise between granularity and memory for longer running simulations (say, a minute of real time or more).
output_time_step = 1 # second

# initial conditions
# We throw the baseball such that we can see it has proper behavior in 3D, it is thrown at a pi/4 angle from the xy plane and at a pi/4 angle from the xz plane.
Vx = 45*np.cos(np.pi/4)*np.sin(np.pi/4)
Vy = 45*np.sin(np.pi/4)**2
Vz = 45*np.sin(np.pi/4)
x_0 = 0
y_0 = 0
z_0 = 2 # meters. 2 meters is close enough to 6 feet. Eew american freedom units lol

print(f'The initial speed is {np.sqrt(Vx**2+Vy**2+Vz**2)} meters per second')

F = numInt.Integrator(F_,0,real_time,output_time_step,dt,x_0,y_0,z_0,Vx,Vy,Vz)

fig, ax = plt.subplots(1,2,constrained_layout=True)
ax = plt.axes(projection ='3d')

plot_vals_1 = F.Euler_Cromer(check_val=True) # this line can be changed to F.Euler, F.Euler_Cromer, or F.RK4 to test the different methods if you so wish
ax.plot3D(plot_vals_1[:,0], plot_vals_1[:,1], plot_vals_1[:,2], 'green')
plt.show()

del F