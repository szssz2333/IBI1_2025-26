infectors=5
grow_rate=0.4
n=91
days=0
#assign values to the initial variables
while infectors < n:
    days+=1#caluate days
    infectors*=(1+grow_rate)#caluate daily infectors
    print('infectors',infectors,'in day',days)#print out days and infectors
print('The total infection needs',days,'days')
#print days in total
