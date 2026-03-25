import matplotlib.pyplot as plt
heart_rates=[72,60,126,85,90,59,76,131,88,121,64]
sum=0
avg=0
for i in heart_rates:
    sum+=i
avg=sum/len(heart_rates)
print('There are',len(heart_rates),'patients. The mean rate is',round(avg,2))

dic={'low':0,'normal':0,'high':0}
for i in heart_rates:
    if i<60:
        dic['low']+=1
    elif i<=120:
        dic['normal']+=1
    else:
        dic['high']+=1
print('low:',dic['low'],'normal:',dic['normal'],'high:',dic['high'])
max=max(dic.values())
for key in dic.keys():
    if max == dic[key]:
        print('The biggest category is',key,'with',max,'patients')
plt.pie(dic.values(),labels=dic.keys(),autopct='%0.1f%%')
plt.title('Heart Rate Categories Distribution')
plt.show()



