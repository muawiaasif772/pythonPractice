# frinds=['hamza','ali','talha','muawia','zakria','babur']
# for frind in frinds:
#     print(frind)
#     student_exam_scores=[150,23,145,56,78,97,56,157,89]
#     # print(sum(student_exam_scores))
# sum=0
# for scores in student_exam_scores:8
#  sum+=scores
#
# print(sum)
# printstudent_exam_scores = [85, 92, 78, 90, 88]
#
# print(f"By built-in method, max is {max(student_exam_scores)}")
# print(f"By built-in method, min is {min(student_exam_scores)}")
# max_score=student_exam_scores[0]
# for scores in student_exam_scores:
#     if scores>max_score:
#        max_score=scores
# print(max_score)
# min_score=student_exam_scores[0]
#
# for scores in student_exam_scores:
#     if scores<min_score:
#         min_score=scores
#
# print(min_score)
# sum=0
# for scores in student_exam_scores:
#     if(scores>min_score):
#        sum+=scores
# print(f" sum without minimum {sum}")
#
# sum=0
# for scores in student_exam_scores:
#    if scores<max_score:
#        sum+=scores
# print(f" sum without max {sum}")
# # range(start,end,step)
# sum=0
# for number in range(1,11):
#     sum+=number
# print(sum)
import random

# task password genrator
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*']
lengthPassWord=int(input("Enter the length of your password: ?\n"))
no_letters=int(input('how many letters do you want?\n'))
no_symbols=int(input('how many symbols do you want?\n'))
no_numbers=int(input('how many numbers do you want?\n'))
# totalPassWord=no_letters+no_symbols+no_numbers
passwordList=[]
# sum=0
for char in range(1,no_letters+1):
   passwordList.append(random.choice(letters))
 # passwordList+=random.choice(letters)
for char in range(1,no_symbols+1):
    passwordList.append(random.choice(symbols))
    # passwordList+=random.choice(symbols)

for char in range(1,no_numbers+1):
    # passwordList+=random.choice(numbers)
  passwordList.append(random.choice(numbers))


random.shuffle(passwordList)

print(passwordList)
sum=''
for char in passwordList:
   sum+=char
print(sum)









# print(totalPassWord)
# print(letters)




