import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import  colors

# (Square) grid side length.
m = 100
# Maximum numbter of iterations.
nitmax = 200
# Number of particles in the simulation.
nparticles = 10
# Output a frame (plot image) every nevery iterations.
nevery = 2
# Constant maximum value of z-axis value for plots.
zmax = 50

# Create the 3D figure object.
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')
# We'll need a meshgrid to plot the surface: this is X, Y.
x = y = np.linspace(-m//2,m//2,m)
X, Y = np.meshgrid(x, y)

vmin, vmax = 0, zmax
norm = colors.Normalize(vmin=vmin, vmax=vmax)

# Initialize the location of all the particles to the centre of the grid.
locs = np.zeros((nparticles, 2), dtype=int)
print(locs.shape)
filenames = []

h = np.sqrt(425600*2e-13)
dt = 425600

def source(time):
  tau = 5
  init = 5000
  return int(np.floor(init*np.exp(-time/tau)))

def wind(coords):
  return [-coords[1], coords[0]]/((dt/2*h)*15)

def l(coords):
  return 0.25 + (dt/2*h)*(wind(coords)[0])

def r(coords):
  return 0.25 - (dt/2*h)*(wind(coords)[0])

def t(coords):
  return 0.25 + (dt/2*h)*(wind(coords)[1])

for i in range(nitmax):
  nparticles += source(i*dt)

  for i in range(source(i*dt)):
    locs = np.append(locs, [[0,0]], axis=0) 

  for j in range(nparticles):
    x = np.random.rand()
    if 0 < x <= l(locs[j]):
      locs[j][0] += 1 
    elif l(locs[j]) < x <= r(locs[j]) + l(locs[j]):
      locs[j][0] -= 1
    elif r(locs[j]) + l(locs[j]) < x <= r(locs[j])+l(locs[j])+t(locs[j]):
      locs[j][1] += 1
    else:
      locs[j][1] -= 1

  if not (i+1) % nevery:
      grid = np.zeros((m, m))
      for k in range(nparticles):
          x, y = locs[k]
          if -m //2 <= x < m //2 and -m //2  <= y < m //2 :
              grid[x + m//2, y+ m//2] += 1
      print(i+1,'/',nitmax)

      ax.clear()
      ax.plot_surface(X, Y, grid, rstride=1, cstride=1, cmap=plt.cm.hot,
                        linewidth=1, vmin=vmin, vmax=vmax, norm=norm)
      ax.set_zlim(0, zmax)
      # Save to 'diff-000.png', 'diff-001.png', ...
      filenames.append('diff-{:03d}.png'.format(i//nevery))
      plt.savefig('diff-{:03d}.png'.format(i//nevery))

import imageio
import glob

images = []
for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('movie.gif', images)