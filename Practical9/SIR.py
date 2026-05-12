#1. Import required libraries
    #IMPORT numpy AS np
    #IMPORT matplotlib.pyplot AS plt

#2. Define model parameters
    #SET N = 10000, beta = 0.3, gamma = 0.05, time_steps = 1000
    
#3. Initialize SIR compartments
    #SET I = 1, S = N - I, R = 0
    #CREATE S_list = [S], I_list = [I], R_list = [R]

#4. Run simulation loop
    #FOR t IN 0 TO time_steps - 1
        #infection_prob = beta * I / N
        #new_infections = np.random.binomial(S, infection_prob)
        #new_recoveries = np.random.binomial(I, gamma)
        
        #S = S - new_infections
        #I = I + new_infections - new_recoveries
        #R = R + new_recoveries
        
        #APPEND S TO S_list, I TO I_list, R TO R_list


#5. Generate and save plot
   

import numpy as np
import matplotlib.pyplot as plt
N=10000
beta=0.3
gamma=0.05
time_steps=1000
I=1
S=N-I
R=0
S_list=[S]
I_list=[I]
R_list=[R]
for t in range(time_steps):
    Infection_probability=beta*I/N
    New_infections=np.random.binomial(S,Infection_probability)
    New_recoveries=np.random.binomial(I,gamma)
    S-=New_infections
    I+=New_infections-New_recoveries
    R+=New_recoveries
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)   
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list,label='Susceptible')
plt.plot(I_list,label='Infected')
plt.plot(R_list,label='Recovered')
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected People')
plt.title('SIR Model')
plt.legend()
plt.savefig('/Users/zhanghanmeng/Downloads/IBI 1/IBI1_2025-26/Practical9/SIR_result.png')
plt.show()