

height=int(input('waht is your heigt?'))
if height>120:
    print('you can ride the rollercoster')
    age=int(input("enter your age: ?"))
    if age<=12:
        print('pay $7')
    elif age<=18 and age>=12:
        print('pay $8')
    else:
        print('your age is too old')
else:
    print("you can't ride the rollercoster")

checkNumber=int(input("enter a number between 1 and 10: ?"))
if(checkNumber%2==0):
    print('even')
else:
    print('odd')

    height=int(input('waht is your height?'))
    weight=int(input('waht is your weight?'))
    bmi=weight/(height**2)
    if bmi<18.5:
        print('normal')
    elif bmi>=25:
        print('overweight')

    else:
        print('underweight')

print('welcome tp python pizza dilvery')

size=(input('enter your size: L, M , S'))
peppeRoni=input('Do you want to pepperONE ON your pizza ? Y or N')
extra_cheeses=(input('enter your extra cheese?:y or N '))
bill=0
if size=='S':
    bill+=15
elif size=='M':
    bill+=20
elif size=='L':
    bill+=25
else:
    print('you write the wrong inputs')
if peppeRoni=='Y':
    if size=='S':
        bill+=2
    else:
         bill+=3
if extra_cheeses=='Y':
     bill+=1
print(f"your final bill is ${bill}")


