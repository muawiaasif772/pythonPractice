# python_dictionary={"name":'muawia','city':'bwp','age':12}
#
# # print(python_dictionary['age'])
# python_dictionary['age']=18
# # print(python_dictionary)
# for key in python_dictionary:
#   print(key, python_dictionary[key])
#
#   studenstNumbers={'hmaza':92,'ali':34,'uzaima':56,'muawia':88,'madni':76,'usman':32,'maki':67}
#   studentgrades={}
# for student in studenstNumbers:
#        score=studenstNumbers[student]
#        if score>=91:
#            studentgrades[student]='Outstanding'
#        elif score>=80:
#            studentgrades[student]='Excellent'
#        elif score>=70:
#            studentgrades[student]='Critical'
#        elif score>=60:
#            studentgrades[student]='pass'
#        else:
#            studentgrades[student]='fail'
#
# print(studentgrades)
#
# trawal_log = {
#     'franc': ['paris', 'lilips', 'origin'],
#     'german': ['tmp', 'bwp', 'lhr', 'isl'],
#     'name': 'muawia',
#     'city': 'bwp',
#     'friends':{'name':'ali','age':12,'city':'tmp'}
# }
#
# for travel in trawal_log:
#     if isinstance(trawal_log[travel], list):  # Check if value is a list
#         for travel2 in trawal_log[travel]:
#             print(travel2)  # Print each city/country
#     elif isinstance(trawal_log[travel], dict):
#         for travel2 in trawal_log[travel]:
#             print(trawal_log[travel][travel2])
#     else:
#         print(trawal_log[travel])  # Print name or city directly
#
#
#      # task
#
# bids={}
# bidding_finished=False
# def find_highest_bidder(bidding_record):
#     higest_bidder=0
#     winner=''
#     for bidder in bidding_record:
#          bidding_amount=bidding_record[bidder]
#          if bidding_amount>higest_bidder:
#           higest_bidder = bidding_amount
#            winner=bidder
#
#
#
#
#
#  while not bidding_finished:
#
#
#     name=input('Enter your name ?')
#     biding_amount=int(input('Enter your bidding amount ?'))
#
