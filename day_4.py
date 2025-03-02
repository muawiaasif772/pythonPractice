# print('hello')
import random
import my_modules
from jinja2.runtime import exported

numbers=random.randint(1, 10)
print(numbers)
numbers=random.uniform(2,6)
print(numbers)
print(my_modules.my_favourit_no)
# list like an array
# list methods pop ,count,clear,remove
fruits=['item1','item2','item3']
print(fruits)
print(fruits[1])
fruits[1]='item4'
print(fruits)
fruits.append("item5")
print(fruits)
fruits.extend(['item6','item7'])
print(fruits)
print(fruits[3:])
friends=['hamza','ali','talha','muawia','zakria','babur']
number=random.randint(0, len(fruits))
print(number)
# print(frinds[number])
def myPrint():
    print(random.choice(friends))


userChoice=int(input('waht do you choice ? type 0 for rock, 1 for paper,2 for seasors?\n'))
computerChoice=random.randint(0,2)
if(userChoice==computerChoice):
    print("you get tie ")
elif(userChoice<computerChoice):
    print('you lose')
else:
    print('you win')

