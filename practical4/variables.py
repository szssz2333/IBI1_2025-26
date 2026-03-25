a,b,c=5.08,5.33,5.55
d=b-a
e=c-b
if d>e:
    print('2004-2014 quicker')
elif d<e:
    print('2014-2024 quicker')
else:
    print("it's the same")
#d>e, which means the popolation growth is decelerating

X,Y=True,False
W=X or Y
print(W)
#W is True
#X	Y	X or Y	X and Y
#True	True	True	True
#True	False	True	False
#False	True	True	False
#False	False	False	False
