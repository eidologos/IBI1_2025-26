import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Model parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
dt = 0.1  # Time step for ODE solver (smoother curves)

# Vaccination rates to test (0% to 100%, step 10%)
vaccination_rates = np.arange(0, 1.1, 0.1)

plt.figure(figsize=(6, 4), dpi=150)

for idx, v in enumerate(vaccination_rates):
    # Initial conditions: vaccinated = initial recovered
    S = [N * (1 - v)]
    I = [1]
    R = [N * v]
    
    for t in range(int(time_steps / dt)):
        current_S = S[-1]
        current_I = I[-1]
        current_R = R[-1]
        
        # Deterministic SIR differential equations
        dSdt = -beta * current_S * current_I / N
        dIdt = beta * current_S * current_I / N - gamma * current_I
        dRdt = gamma * current_I
        
        # Update with Euler method
        next_S = current_S + dSdt * dt
        next_I = current_I + dIdt * dt
        next_R = current_R + dRdt * dt
        
        S.append(next_S)
        I.append(next_I)
        R.append(next_R)
    
    # Plot with unique color for each rate
    plt.plot(np.arange(0, time_steps+dt, dt), I, 
             color=cm.viridis(idx / len(vaccination_rates)), 
             linewidth=1.5, 
             label=f'{int(v*100)}%')

# Plot styling
plt.xlabel('Time', fontsize=12)
plt.ylabel('Number of Infected Individuals', fontsize=12)
plt.title('SIR Model with Different Vaccination Rates', fontsize=16, pad=20)
plt.legend(loc='upper right', title='Vaccination %', fontsize=10, title_fontsize=12)
plt.grid(alpha=0.3)
plt.ylim(bottom=-100)  # Slight negative to show near-zero lines
plt.tight_layout()
plt.savefig('/Users/zhanghanmeng/Downloads/IBI 1/IBI1_2025-26/Practical9/SIR_vaccination_result.png')
plt.show()