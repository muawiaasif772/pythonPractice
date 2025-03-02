
# # print(len('muawia'))
# # print(len(12345))
# print(type(("muawia")))
# print(type(12355))
# print(type(34.5))
# print(type(False))
# print(int('123')+int('123'))
# name=input("waht is your name?")
# # print('number of letters in your name is: ' +len((name))) this give us error because string type and integer type can't print
# print(type(name))
# print(type (len(name)))
# print('number of letters in your name is:'+ str(len(name)))
# print(7-3)
# print(3*3)
# print(5/3)
# print(5//3)
# print(2**3)
height = 1.65
weight = 84
bmi=weight/height**2
print(round(bmi,2))
score= 0
height=1.5
is_winning=True
# f is use to combine all data types other wise it give us error
print(f"YOUR SCORE IS = {score} your height is {height}.you are winning is {is_winning}")
height=int(input("enter your height in cm?: "))

# # task 1
# print('welcom to the tip calculator')
# totalAmount=int(input('enter the total amount you want?$'))
# tipAmount=int(input('How much tip would you like to give? 10, 12, or 15 ?$'))
# num_people=int(input('How many people want to split the bill? $'))
# amount_withTip=totalAmount*(1+tipAmount/100)
# amount_per_person=amount_withTip/num_people
# print(f"Each person should pay: ${amount_per_person:.2f}")