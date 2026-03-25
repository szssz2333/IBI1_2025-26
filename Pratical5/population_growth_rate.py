import matplotlib.pyplot as plt
pop={'UK':[66.7,69.2],'China':[1426,1410],'Italy':[59.4,58.9],'Brazil':[208.6,212.0],'USA':[331.6,340.1]}
change={}
for i in pop.keys():
    a=round((pop[i][1]-pop[i][0])/pop[i][0],4)*100
    print('The population change in',i,'is:',a,'%')
    change[i]=a
new_change=dict(sorted(change.items(), key=lambda x: x[1], reverse=True))

max=max(change.values())
min=min(change.values())

for key in change.keys():
    if max == change[key]:
        print('The country with the largest increase is',key,'with rate of',max,'%')
    if min == change[key]:
        print('The country with the largest decrease is',key,'with rate of',min,'%') 

colors=[]
for c in new_change.values():
    if c>0:
        colors.append('green')
    else:
        colors.append('red')

plt.bar(new_change.keys(),new_change.values(),color=colors)
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")
plt.title("Population Change from 2020 to 2024")
for j,k in zip(new_change.keys(),new_change.values()):
    plt.text(j,k if k > 0 else k-0.23,k,ha='center', va='bottom')
plt.show()