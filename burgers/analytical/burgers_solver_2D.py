import numpy as np
import copy 

def burgers_timestep(x:np.ndarray,y:np.ndarray,u:np.ndarray,v:np.ndarray,nt:int,dt:float,nu:float=0.1):
    """Solving burgers equation using finite difference with euler time step (1st order approximation) 

    Args:
        x (np.ndarray): domain x direction
        y (np.ndarray): domain y direction
        u (np.ndarray): matrix describing x-velocity field in i,j space
        v (np.ndarray): matrix describing y-velocity field in i,j space
        nt (int): number of time advances
        dt (float): time step to use for first order approximation
        nu (float, Optional): Viscosity. Defaults to 0.1
    
    Returns:
        (tuple): containing

            **u_history** (np.ndarray): history for u velocity 
            **v_history** (np.ndarray): history for v velocity 
    """


    dx = x[1]-x[0] # We can do it this way because x and y are initialized using linspace which guarantees constant spacing 
    dy = y[1]-y[0]

    u_history = list()
    v_history = list() 
    u_history.append(u)
    v_history.append(v)

    for n in range(nt):
        u_future = u.copy()
        v_future = v.copy()
        for i in range(1,len(x)-1):
            for j in range(1,len(y)-1):
                # Uses backward difference in space to solve first order derivative
                # Central differencing for second order derivative 
                u_future[i,j] = (u[i, j] -(u[i, j] * dt / dx * (u[i, j] - u[i-1, j])) -v[i, j] * dt / dy * (u[i, j] - u[i, j-1])) + (nu*dt/(dx**2))*(u[i+1,j]-2*u[i,j]+u[i-1,j])+(nu*dt/(dx**2))*(u[i,j-1]-2*u[i,j]+u[i,j+1])
                
                v_future[i,j] = (v[i, j] -(u[i, j] * dt / dx * (v[i, j] - v[i-1, j]))-v[i, j] * dt / dy * (v[i, j] - v[i, j-1])) + (nu*dt/(dx**2))*(v[i+1,j]-2*v[i,j]+v[i-1,j])+(nu*dt/(dx**2))*(v[i,j-1]-2*v[i,j]+v[i,j+1])
        
        u_future[:,0] = 0       # At all i values when j = 0
        u_future[:,-1] = 0      # At all i values when j = jmax
        u_future[0,:] = 0       # At all j values and i = 0
        u_future[-1,:] = 0      # At all j values and i = imax

        v_future[:,0] = 0
        v_future[:,-1] = 0
        v_future[:,0] = 0
        v_future[:,-1] = 0

        u_history.append(copy.deepcopy(u_future))
        v_history.append(copy.deepcopy(u_future))
    return u_history, v_history
    
