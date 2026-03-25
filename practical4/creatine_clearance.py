age=int(input('Please enter your age,it should be a integer under 100'))
weight=float(input('enter your weight,it should be between 20-80kg'))
gender=input('enter your gender,it should only be male or female')
Cr=float(input('enter creatine concentration,in µmol/l'))
CrCl=0
error=False
if age >= 100:
    print('your age is bigger than 100')
    error=True
if weight < 20 or weight > 80:
    print('your weight is not in range')
    error=True
if gender != 'male' and gender != 'female':
    print('gender should only be male or female')
    error=True
if Cr > 100:
    print('creatine concentration is not in range')
    error=True
if error == False:
    if gender == 'male':
        CrCl=(140-age)*weight/72/Cr
    else:
        CrCl=(140-age)*weight/72/Cr*0.85
    print('Your creatine clearance rate is:',CrCl)
