'''
Ek function is_valid_password(password) banao jo True return kare agar password ye saari 
conditions follow kare:Kam se kam ek Capital letter ho (isupper())Kam se kam ek Small letter ho
(islower())Kam se kam ek Digit/Number ho (isdigit())Password ki length kam se kam 8 characters hoInput:
"Python3Rulez" Expected Output: TrueInput: "python" Expected Output: False
'''

# def is_password_strong(password):
#     if len(password)<8:
#         return 'password kalebgth kam hai'
#     capital=any(i.isuppue() for i in password)
#     lower=any(i.islower() for i in password)
#     digit=any(i.isdigit() for i in password)

#     if not (capital and lower and digit ):
#         return f'password validf nahi hai'


# user=input("enter your password")
# result=is_password_strong(user)
# print(result)



'''
Ek words ki list check karo. Agar usme koi bhi aisa word hai jo aage aur peeche se same padha jata hai (jaise "radar", "madam"), 
toh True aana chahiye.Input: ["apple", "banana", "radar", "mango"] 
Expected Output: True
'''
# def is_pallindrom(l):
#     return any(i[::-1]==i for i in l)

# user=eval(input("enter your list"))
# result=is_pallindrom(user)
# print(result)



'''
Ek words ki list di gayi hai. Check karo ki kya saare ke saare words poore CAPITAL (Uppercase) me hain.Input 
1: ["PYTHON", "JAVA", "HTML"] Expected 
Output: TrueInput 2: ["PYTHON", "Java", "HTML"]  Expected Output: False
'''
# def is_all_capital(l):
#     return all(i.isupper() for i in l)

# user=eval(input("enter your list"))
# result=is_all_capital(user)
# print(result)

