#1. Import required libraries
    # IMPORT numpy AS np
    # IMPORT matplotlib.pyplot AS plt

#2. Set up 2D grid and parameters
    # CREATE 100x100 grid filled with 0 (Susceptible)
    # RANDOMLY infect one cell (set to 1)
    # SET beta = 0.3, gamma = 0.05, time_steps = 100
    # DEFINE 8 surrounding directions for neighbors

#3. Prepare for animation
    # TURN ON interactive plotting
    # CREATE figure for heatmap and SIR curve as an auxiliary chart to clearly present the changes in quantity over time

#4. Main simulation loop
    # FOR each time step
        # GET current infected positions
        # Calculate and record S, I, R numbers
        
        # Infection process:
            # FOR each infected cell
                # CHECK all 8 neighbors
                # IF neighbor is susceptible, infect it with probability beta
        
        # Recovery process:
            # FOR each infected cell
                # Recover with probability gamma (set to 2)
        
        # UPDATE animation: plot heatmap and SIR curve
        # PAUSE for smooth display

#5. generate final plot
import numpy as np
import matplotlib.pyplot as plt
import time

grid_size = 100
beta = 0.3
gamma = 0.05
time_steps = 100
# Initialize the grid
population = np.zeros((grid_size, grid_size), dtype=int)
# Randomly infect one individual
outbreak = np.random.choice(range(grid_size), size=2)
population[outbreak[0], outbreak[1]] = 1  # represents infected
neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
S_list = []
I_list = []
R_list = []
plt.ion()
fig,(ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), dpi=150)

for step in range(time_steps):
    current = population.copy()
    S = np.sum(current == 0)
    I = np.sum(current == 1)
    R = np.sum(current == 2)

    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
    infected_coords = np.where(current == 1)
    for x, y in zip(infected_coords[0], infected_coords[1]):
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                if current[nx, ny] == 0 and np.random.rand() < beta:
                    population[nx, ny] = 1


    infected_coords = np.where(current == 1)
    for x, y in zip(infected_coords[0], infected_coords[1]):
        if np.random.rand() < gamma:
            population[x, y] = 2

   
    ax1.clear()
    ax1.imshow(population, cmap='viridis', interpolation='nearest')
    ax1.set_title(f'Spatial SIR | Step {step+1} | S={S}, I={I}, R={R}')

    ax2.clear()
    ax2.plot(S_list, label='S', color='purple')
    ax2.plot(I_list, label='I', color='green')
    ax2.plot(R_list, label='R', color='yellow')
    ax2.legend()
    ax2.set_title('SIR Curve')
    ax2.set_xlabel('Time Step')
    ax2.set_ylabel('Number of People')

    plt.pause(0.05)

plt.ioff()
plt.show()