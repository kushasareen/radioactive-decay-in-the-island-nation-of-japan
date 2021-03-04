# radioactive-decay-in-the-island-nation-of-japan

We wanted to understand why radioactive particles from the aftermath of a nuclear disaster impact the inhabitant of nearby areas for years after. Our case study was the Fukushima nuclear disaster. In 2011, Fukushima nuclear power plant, off the coast of eastern mainland Japan, had a prefecture after an earthquake and tidal wave in the area, resulting the nuclear waste that is there to the present day. Our simulation hopes to understand how different wind vector fields impact the propagation of the radioactive remnants of the disaster in space and in time.

We used a PDE commonly used to describe the motion of radioactive particles, the advection-diffusion equation, and used a Taylor expansion to convert it into a directed random walk. We then simulated the random walk for many particles to see how the gaussian plume would spread and move in a 2D lattice. We added an exponentially decaying source of particles at the plant, used the diffusion coefficient of radioactive uranium and observed its motion under different wind fields.

Some simulations with different wind patterns:
![](https://github.com/kushasareen/radioactive-decay-in-the-island-nation-of-japan/blob/main/line%20wind.gif)
![](https://github.com/kushasareen/radioactive-decay-in-the-island-nation-of-japan/blob/main/strange%20wind.gif)
![](https://github.com/kushasareen/radioactive-decay-in-the-island-nation-of-japan/blob/main/circular.gif)

[Check out our Devpost!](https://devpost.com/software/radioactive-decay-in-the-island-nation-of-japan)
