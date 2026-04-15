import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

tot=10000
beta,gamma=0.3,0.05
vaccine_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.figure(figsize=(6,4), dpi=150)

for i in vaccine_rates:
    S,I,R=int(tot*(1-i)-1),1,int(tot*i)
    S_list,I_list,R_list=[S],[I],[R]
    if S<0:
        S,I,R=0,0,10000
    for j in range(1000):
        inf_p=beta*I/10000
        infect=sum(np.random.choice([0,1],S,p=[1-inf_p,inf_p]))
        recover=sum(np.random.choice([0,1],I,p=[1-gamma,gamma]))
        S-=infect
        I=I+infect-recover
        R+=recover
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
    plt.plot(I_list,color=cm.viridis(i),label=f'{int(i*100)}% vaccination')

plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('Vaccinated SIR Model')
plt.legend()
plt.savefig(f'SIR_vaccination.png',dpi=300)
plt.show()