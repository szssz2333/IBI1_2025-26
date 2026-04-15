import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2) 
population[outbreak[0],outbreak[1]]=1

tot=10000
beta,gamma=0.3,0.05
vaccine_rates =[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
dev=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

for counts in range(101):
    
    if counts%10==0:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.title(f'Time step {counts}')
        plt.show()
    
    inf=np.argwhere(population==1)
    new_pop=population.copy()
    for i,j in inf:
        for di,dj in dev:
            if not (0<=i+di<100 and 0<=j+dj<100):
                continue
            if new_pop[i+di,j+dj]==0:
                new_pop[i+di,j+dj]=np.random.choice([0,1],p=[1-beta,beta])
        new_pop[i,j]=np.random.choice([1,2],p=[1-gamma,gamma])
    population=new_pop
    

    
        