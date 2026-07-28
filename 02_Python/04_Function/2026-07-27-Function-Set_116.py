'''

Century Milestone Questions List Cleanup (Remove Falsy Entries)

Task: Dictionary comprehension ka 100th Question! Dict se saari falsy values (0, False, None, "", []) ko filter karke hatana hai.

Input: data = {"a": "Maaz", "b": 0, "c": True, "d": None, "e": "",'l':[]}

Expected Output: {"a": "Maaz", "c": True}

'''
# def remove_falsy_value(d):
#     res={}
#     for i in d:
#         if d[i] is not None:
#             if d[i]:
#                 res[i]=d[i]
#     return res


# user=eval(input("enter your dict"))
# result=remove_falsy_value(user)
# print(result)



'''
Merge Two Dicts with Summing Common Keys

Task: Do dicts d1 aur d2 ki unique keys ki dict comprehension banao jahan agar key dono mein ho toh values add ho jayein.

Input: d1 = {"a": 10, "b": 20}, d2 = {"b": 30, "c": 40}

Expected Output: {"a": 10, "b": 50, "c": 40}
'''

# def common_keys_value_sum(d1,d2):
#     d={}
#     for i in d1:
#        d[i]=d1[i]

#     for j in d2:
#         if j in d:
#             d[j]=d[j]+d2[j]
#         else:
#             d[j]=d2[j]
#     return d


# d1=eval(input("enter your dict"))
# d2=eval(input("enter your dict"))
# result=common_keys_value_sum(d1,d2)
# print(result)








'''
Django default validators ke alawa custom check: At least 8 characters, 1 Uppercase, 
1 Digit, aur 1 Special Character (@, $, !, %).Task: List comprehension ya function se check karo ki 
password strong hai ya nahi.Input: "maaz123" $\rightarrow$ (False, "Password must 
contain uppercase and special char")Input: "Maaz@1234" $\rightarrow$ (True, "Strong password")

'''

# def is_strong_password(password):
#     char=any(i.isalpha() for i in password)
#     upper=any(i.isupper() for i in password)
#     digit=any(i.isdigit() for i in password)
#     symbol=any(not i.isalnum() for i in password)
#     if not (char and digit and symbol and upper):
#         return False , "Password must contains upper case and specaial char"

#     return True ,"Strong password"


# user=input("enter your password")
# result=is_strong_password(user)
# print(result)







'''
Case-Insensitive Unique Email Validation

Scenario: Database mein maaz@gmail.com hai. Naya user signup kar raha hai MAAZ@GMAIL.COM se.

Task: Django query / List filter logic likho jo new email ko .lower() karke existing database
 emails se compare kare taaki duplicate signup na ho.

Input: Existing = ["maaz@gmail.com"], New = "Maaz@Gmail.Com"

Expected Output: (False, "Email already registered")

'''

# def check_dublicat_email_exixt(email,new_email):
#     new_email=new_email.lower()
#     if new_email in email:
#         return (False, "Email already registered")
#     return (True, "Email available")



# email=eval(input('enter your email'))
# new_email=input('enter your email')
# result=check_dublicat_email_exixt(email,new_email)
# print(result)







'''
Django Custom AbstractUser mein jab user create hota hai toh username aur
email normalize hote hain.Task: Ek function banao jo email domain ko 
lowercase kare aur phone number se spaces/dashes hataye ("+91 98765-43210" 
$\rightarrow$ "+919876543210").Input: {"email": "MAAZ@GMAIL.COM", "phone": 
"+91 98765-43210"}Expected Output: {"email": "maaz@gmail.com", "phone": "+919876543210"}

'''

# def normalize_user_data(d):
#     res={}
#     if 'email' in d and d['email']:
#         res['email']=d['email'].lower()


#     if 'phone' in d and d['phone']:
#         clean_phone=d['phone'].replace(' ','').replace('-','')
#         res['phone']=clean_phone

#     return res


# user=eval(input('enter your dict'))
# result=normalize_user_data(user)
# print(result)





'Reverse chunks having even length only '



# def reverse_even_chunks(l,k):
#     for i in range(0,len(l),k):
#         start=i
#         end=i+k
#         end=len(l) if end>len(l) else end
#         chunk_len=end-start
#         if chunk_len%2==0:
#             l[start:end]=l[start:end][::-1]
#     return l


# user=eval(input('enter your list'))
# k=int(input("enter your k"))
# result=reverse_even_chunks(user,k)
# print(result)





'''
OTP 5-Minute Expiry Checker (Timestamp Logic)Scenario: User ko OTP 12:00:00 PM par bheja gaya. 
Expiry = 5 mins ($300$ seconds). User enter kar raha hai 12:06:00 PM par.Task: Function banao jo 
created_at timestamp aur current_time timestamp ko subtract karke check kare ki $300$ seconds pass huye 
hain ya nahi.Input: created_time = 1700000000,
 current_time = 1700000350Expected Output: (False, "OTP Expired! Request a new one")


'''
# import time

# def check_otp_expiry(created_time,validity_second=300):
#     Current_time=time.time()
#     diff=created_time-Current_time
#     if diff>validity_second:
#         return False ,'otp expire'
#     return True ,'otp valid'



# created_time=time.time()
# result=check_otp_expiry(created_time)
# print(result)








'''

Complete Auth Payload Validator (Master Function)

Scenario: Real Django Signup View/Serializer Payload validation.

Task: Ek master function jo poore payload tuple ko ek sath test kare: No Empty Fields + Valid Email Format + Strong Password + Passwords Match.

Input: {"username": "maaz", "email": "maaz@gmail.com", "pass1": "Pass@123", "pass2": "Pass@123"}

Expected Output: (True, "Payload Valid")

'''
# def is_auth_validate(data):
   
#     required_fields = ['username', 'email', 'pass1', 'pass2']
    
   
#     for field in required_fields:
#         if field not in data or not str(data[field]).strip():
#             return (False, f"Field '{field}' cannot be empty")

#     email = data['email'].strip().lower()
#     pass1 = data['pass1']
#     pass2 = data['pass2']

   
#     if '@' not in email or '.' not in email.split('@')[-1]:
#         return (False, "Invalid email format")

  
#     if pass1 != pass2:
#         return (False, "Passwords do not match")

   
#     if len(pass1) < 8:
#         return (False, "Password must be at least 8 characters long")

#     lower = any(i.islower() for i in pass1)
#     upper = any(i.isupper() for i in pass1)
#     digit = any(i.isdigit() for i in pass1)
#     symbol = any(not i.isalnum() for i in pass1)

#     if not (lower and upper and digit and symbol):
#         return (False, "Password is not strong enough")

   
#     return (True, "Payload Valid")


# data = {
#     "username": "maaz",
#     "email": "maaz@gmail.com",
#     "pass1": "Pass@123",
#     "pass2": "Pass@123"
# }

# result = is_auth_validate(data)
# print(result)





    
