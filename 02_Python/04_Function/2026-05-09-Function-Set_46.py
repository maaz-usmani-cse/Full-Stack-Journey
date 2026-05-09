'''
List mein se dusra sabse chota positive number dhoondho.

Input: [10, -2, 5, 8, 2, -20]

Output: 5 (Kyunki sabse chota 2 hai, aur uske baad 5).

Logic Hint: Do variables rakho min1 aur min2, dono ko None se shuru karo.


'''
# def second_possitive_number(l):
#     first_minimum=None
#     second_minimum=None
#     for i in l:
#        if i>0:
#            if first_minimum is None or i<first_minimum:
#                second_minimum=first_minimum
#                first_minimum=i
#            elif i!=first_minimum and (second_minimum is None or i<second_minimum):
#                second_minimum=i
#     return f'first is {first_minimum} second minimum is {second_minimum}'

# user=eval(input("enter your list"))
# result=second_possitive_number(user)
# print(result)





'''
Sawal: List mein se koi bhi do numbers uthao jinme sabse kam antar (absolute difference) ho.

Input: [1, 5, 3, 19, 18, 25]

Output: 1 (Kyunki 19 aur 18 ka antar 1 hai).
'''

# def absoulute_diffrence(l):
#     minimum_diff=None
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 dif=l[i]-l[j]
#                 if minimum_diff is None or dif<minimum_diff:
#                     minimum_diff=dif
#                 else:
#                  dif=l[i]-l[j]
#                  if minimum_diff is None or dif<minimum_diff:
#                      minimum_diff=dif
#     return minimum_diff
      
# user=eval(input("enter your list"))
# result=absoulute_diffrence(user)
# print(result)








'encrypy message logic'
# def encrypt_message(message,key,mode):
#     key=key%26
#     res=''
#     for i in message:
#         if mode==1:
#            old_position=ord(i)-97
#            new_position=(old_position+key)%26
#         elif mode==2:
#             old_position=ord(i)-97
#             new_position=(old_position-key)%26
#         res=res+chr(new_position+97)
#     return res


# user=input("enter your message")
# key=int(input("enter your kewy"))
# mode=int(input("enetr your mode"))  
# result=encrypt_message(user,key,mode)      
# print(result)






'''
Sawal: List mein jahan bhi negative number dikhe, use 0 se badal do, aur positive numbers ko waisa hi rehne do.

Input: [10, -5, 20, -1, 0]

Output: [10, 0, 20, 0, 0]

'''

# def replace_negative_number(l):
#     res=[]
#     for i in l:
#         if i<0:
#             res.append(0)
#         else:
#             res.append(i)
#     return res

# user=eval(input("enetr your list"))
# result=replace_negative_number(user)
# print(result)        





'''
List mein jitne bhi positive numbers hain, sirf unka total jod (sum)
 batao.Input: [5, -10, 15, 2, -3]Output: 22 ($5 + 15 + 2$)
'''

# def total_possitive(l):
#     total=0
#     for i in l:
#         if i>0:
#             total=total+i
#     return total

# user=eval(input("enetr your list"))
# result=total_possitive(user)
# print(result)





'''
Task: Do timestamps lo (Python datetime). Ek jab OTP generate hua aur ek abhi ka now(). 
Function bataye ki kya dono ke beech ka farq 300 seconds (5 min)
se zyada hai? (Hint: total_seconds() method). 
'''
# from datetime import datetime

# def check_otp_expiry(otp_time):
#     # Abhi ka current time nikaalo
#     abhi_ka_time = datetime.now()
    
#     # Dono ke beech ka gap (duration) nikaalo
#     fark = abhi_ka_time - otp_time
    
#     # total_seconds() use karke gap ko seconds mein convert karo
#     kitne_seconds_hue = fark.total_seconds()
    
#     # Agar 300 sec (5 min) se zyada hai toh True (Expired)
#     if kitne_seconds_hue > 300:
#         return "OTP Expire ho chuka hai!"
#     else:
#         return "OTP abhi valid hai, tension mat lo."

# # --- TEST KARNE KE LIYE ---
# # Maan lo OTP 10 minute pehle aaya tha
# purana_waqt = datetime(2023, 10, 1, 10, 0, 0) 
# print(check_otp_expiry(purana_waqt))






'check kro password me 8 characters, 1 digit, 1 letter, 1 symbol"""'
# def is_strong_password(password):
#     has_digit=any(i.isdigit() for i in password)
#     has_letter=any(i.isalpha() for i in password)
#     has_special=any(not i.isalnum() for i in password)
#     if not(has_digit and has_letter and has_special):
#         return False ,'password m digit sybol albhabet hona zroori hai'
#     return True,'success'

# password=input("enetr your password")
# result=is_strong_password(password)
# print(result)