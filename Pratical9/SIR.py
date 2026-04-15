import numpy as np
import matplotlib.pyplot as plt

S,I,R=9999,1,0
S_list,I_list,R_list=[S],[I],[R]
beta,gamma=0.3,0.05

for i in range(1000):
    inf_p=beta*I/10000
    infect=sum(np.random.choice([0,1],S,p=[1-inf_p,inf_p]))
    recover=sum(np.random.choice([0,1],I,p=[1-gamma,gamma]))
    S-=infect
    I=I+infect-recover
    R+=recover
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Classic SIR Model')
plt.legend()
plt.savefig(f'SIR.png',dpi=300)
plt.show()