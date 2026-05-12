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