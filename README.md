# PINN-Torch
Physics informed neural network using pytorch

---
Note: 

**Displaying Math**: This repository contains a lot of math equations. Github currently does not display latex equations. If you want to see the equations, I reccomend installing xhub google chrome: https://github.com/nschloe/xhub 

**Creating GIFs**:To save gif files you need to have imagemagick installed and added to your **path** variable
https://imagemagick.org/script/download.php 

Imagemagick does not work on windows even with legacy version. I will need to try with mac or linux

---

All of these examples are presented on a 2D Domain of x and y. The importance of the Physics based neural network is that it doesn't require a mesh in order to obtain a solution; all you need is enough samples within your domain.

# List of Examples
- [Viscous Burgers](burgers): Burgers equation describes the viscous movement of fluid at each location on a 2D space as a function of time. 
- [Poisson Equation for Heat Conduction](Poisson): This example shows how to use poisson's equation to describe the heat conduction through a plate 
- [Euler 2D](euler): This example shows how neural networks to solve euler's equation in gas dynamics for a 2D flow field 
