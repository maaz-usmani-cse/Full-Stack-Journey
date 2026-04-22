'ek ayse function bnao ki jisme user jab tak user-id aur password na daley wo program aage n badhe mangte rhe is trh ka '
# def cumpolsory_required():
#    while True:
#       user_id=input('enter your user-id:')
#       user_password=input("enter your password:")
#       if not(user_id and user_password):
#          print('eroor.. please fill the user name')
#       else:
#          break
      
# cumpolsory_required()












'eroor handling program with try except'
# def divison_tool():
#     try:
#         num1=int(input("enetr your number"))
#         num2=int(input("enter your number"))
#         result=num1/num2
#         return result
#     except ValueError:
#         return 'bhai sirf value dalo number nahi'
#     except ZeroDivisionError:
#         return 'kisi v number ko 0 se devide nahi kr skte ho'


# result=divison_tool()
# print(result)











'Ek list of dictionaries ko filter karo jisme kisi specific key ki value missing ho.'
# def find_missing_keys(data):
#     # 1. Sabse pehle saari possible keys dhoondo (Ideal List)
#     all_keys = []
#     for dictionary in data:
#         for key in dictionary:
#             if key not in all_keys:
#                 all_keys.append(key)
    
#     missing_report = [] # Isme hum missing wala data rakhenge

#     # 2. Ab har bande ka data check karo
#     for person in data:
#         for k in all_keys:
#             # Check karo kya ye key is person ke paas hai?
#             found = False
#             for person_key in person:
#                 if k == person_key:
#                     found = True
            
#             # Agar nahi mili, toh report mein daal do
#             if found == False:
#                 # Hum bata rahe hain ki kiska kya missing hai
#                 detail = person["name"] + " ka " + k + " missing hai"
#                 missing_report.append(detail)
                
#     return missing_report

# # Test karne ke liye
# user_data = [
#     {"name": "Maaz", "salary": 25000, "city": "Bhopal"},
#     {"name": "Ali", "salary": 45000}, # city missing
#     {"name": "Rohit", "city": "Patna"} # salary missing
# ]

# result = find_missing_keys(user_data)

# # Print karke dekhte hain kya-kya missing mila
# for m in result:
#     print(m)               
    






