
'''
Ek list di gayi hai emails ki: ['a@b.com', 'c@d.com',
'a@b.com']. Ek function likho jo check kare ki naya email
 list mein pehle se hai ya nahi.
 Agar hai, toh error message return karo.

# '''
# def check_email(email_list,new_email):
#     for i in email_list:
#         if new_email in i:
#             return 'already exist'
#         else:
#             return 'not exist'
   
# email_list=eval(input("enetr your list"))
# new_email=input("enter your email")
# result=check_email(email_list,new_email)
# print(result)






'''
Ek logic banao jo check kare ki password ki length kam se kam 8 
characters hai aur usme kam se kam ek number (0-9) hona chaiye a kuch v matlab matlb aur ek symbol koi sa v ex-@#%.
mtlb ki password me 8character v ho aur digit v aur symbol v
'''
# import string

# def check_heavy_password(password):
#     if len(password)<8:
#         return 'minimum 8 character is required'
#     has_digit=any(i.isdigit() for i in password)
#     has_letter=any(i.isalpha() for i in password)
#     has_special_symbol=any(i in string.punctuation for i in password)
#     if not has_digit:
#         return 'kam se kam 1 digit dalo'
#     if not has_letter:
#         return 'kam se kam ek letter dalo'
#     if not has_special_symbol:
#         return 'ek special symbol to chhaiye '
#     return 'password ekdm mazboot hai'


# password=input("enter your password")
# result=check_heavy_password(password)
# print(result)



        


    

'''
User ne naam dala "  RAHUL kumar  ". 
Ek function likho jo extra spaces hataye aur har
word ka pehla letter capital kar de ("Rahul Kumar").
'''

# def clean_user_name(name):
#     cleaned_name=name.strip().title()
#     return cleaned_name

# user_name=input("enter your user_name")
# result=clean_user_name(user_name)
# print(result)






'''
OTP Generator (Custom): random module ka use karke ek function banao
 jo sirf "Even" 
(sam) digits wala 6-digit OTP generate kare (Example: 246802).

'''
# import random
# def genarate_even_otp():
#     otp_list=[0,2,4,6,8]
#     otp=''
#     for i in range(6):
#         number=random.choice(otp_list)
#         otp=otp+str(number)
#     return otp

# result=genarate_even_otp()
# print(result)

        
