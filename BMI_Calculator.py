
Height = float(input('Height in centimeter:'))
Weight = float(input('Weight in Kg: '))
Height = Height/100
BMI = Weight/(Height*Height)
print('your Body Mass Index is: ',BMI)
if (BMI>0):
    if(BMI<=16):
        print('severely underweight')
    elif(BMI<=18.5):
        print('underweight')
    elif(BMI<=25):
        print('Healthy Weight')
    elif(BMI<=30):
        print('Overweight')
    else: print('Obese')
else:('eneter valid details')






