''''
Ek string di gayi hai: text = "Practice makes a man perfect".
Is string mein se sabhi vowels (a, e, i, o, u, case-insensitive) extract karke list mein store
'''
# def vowel_extract(s):
#     s=s.lower()
#     vowel='aeiou'
#     return [ i for i in s if i in vowel]


# user=input("enter your word")
# result=vowel_extract(user)
# print(result)



'''
Ek numbers ki list di gayi hai: nums = [12, -7, 5, -3, 0, 8, -1].

Agar number positive ya zero ho, toh "Positive"

Agar negative ho, toh "Negative"
'''
# def check_possitive_or_negative(l):
#     return ['Possitive' if i>=0  else "Negative" for i in l]

# user=eval(input("enter your list"))
# result=check_possitive_or_negative(user)
# print(result)



'''
Divisible by 3 and 5
1 se 100 ke beech ke un sabhi numbers ki list banao jo 3 aur 5 dono se divide hote hain.
'''
# def list_1_to_100():
#     return [i for i in range(1,101) if i%3==0 and i%5==0]


# result=list_1_to_100()
# print(result)




'''
Even numbers filter karna
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

'list comprehenshion'
# def filter_even_number(l):
#     return [ i for i in l if i %2==0]


'filter ()'


# def filter_even(l):
#     return l%2==0


# user=eval(input("enter your list"))
# result=list(filter(filter_even,user))
# print(result)




'negative number hatana [-5, 12, -3, 0, 45, -8, 9]'

# def filter_negative_number(l):
#     'list comprehenshion'
#     # return [i for i in l if i>=0]

#     'with filter()'
#     return list(filter(lambda x: x>=0 ,l ))


# user=eval(input("enter your list"))
# result=filter_negative_number(user)
# print(result)





'''
"Aapko ek list di gayi hai jisme mixed data types hain (strings, numbers, corrupted text). 
Aapko filter() use karke sirf wahi strings nikaalni hain jo valid float/integer
numbers hain (jaise '42', '3.14'), aur corrupted data (jaise 'abc', None) ko ignore karna hai."

raw_data = ["100", "45.8", "invalid_log", "0.005", "NaN_value", "999", "error_404"]
'''


# def is_valid_number(l):
#     try:
#         float(l)
#         return True
#     except(ValueError,TypeError):
#         return False

# user=eval(input('enter your list'))
# result=list(filter(is_valid_number,user))
# print(result)




'''
"Aapke paas e-commerce orders ka data (list of dictionaries) hai. filter() use karke sirf wahi orders nikalo jinki delivery status 'DELIVERED' ho aur total bill amount 1000 se zyada ho."

Input:
Python
orders = [
    {"order_id": 101, "amount": 1500, "status": "DELIVERED"},
    {"order_id": 102, "amount": 750,  "status": "DELIVERED"},
    {"order_id": 103, "amount": 2200, "status": "PENDING"},
    {"order_id": 104, "amount": 3100, "status": "DELIVERED"},
]
'''

# user=eval(input("enter your list"))
# result=list(filter(lambda x: x['status']=="DELIVERED" and x['amount']>1000,user))
# print(result)
 


'''
Jahan SIRF Normal Function (def) chalega (Lambda fail ho jayega)
Q1. Prime Numbers Filter Karna
Task: List se prime numbers filter karo.

Kyun def? Divisibility check karne ke liye for loop aur multiple if-else lagte hain. Lambda me loop nahi chal sakta.
numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
'''
# def filter_prime(l):
#     if l<2:.0
#         return False
    
#     elif l==2:
#         return True
#     elif l%2==0:
#         return False

#     for i in range(3,int(l**0.5)+1,2):
#         if l%i==0:
#             return False
#     return True

# user=eval(input("enter your list"))
# result=list(filter(filter_prime,user))
# print(result)






'''
API Response Validation (Try-Except / Error Handling)
Task: JSON responses me se sirf valid dates filter karo. Invalid format par error na aaye.

Kyun def? Python me try-except ek statement hai, aur Lambda sirf single expression allow karta hai.

dates = ["2026-05-12", "invalid-date", "2026-09-11", "11/09/2026"]
'''

# from datetime import datetime
# def is_valid_date(d):
#     try:
#         datetime.strptime(d,"%Y-%m-%d")
#         return True
#     except ValueError:
#         return False
    

# user=eval(input("enter your list"))
# result=list(filter(is_valid_date,user))
# print(result)




'''
Strings me se punctuation aur spaces hata kar check karo ki 
wo palindrome hai ya nahi sentences = ["Racecar", "Hello World", "A man, a plan, a canal: Panama", "Python"].

'''
# def is_valid_pallindrom(s):
#     cleaned_word=s.replace(' ','').replace(':','').replace(',','').lower()
#     if cleaned_word==cleaned_word[::-1]:
#         return True
#     return False

# user=eval(input("enter your list"))
# result=list(filter(is_valid_pallindrom,user))
# print(result)





'''
Wo numbers filter karo jinka sum of digits (recursively jab tak single digit na bane) 9 aaye.
nums = [18, 25, 45, 99, 102]
'''

# def sum_digit(num):
#     total=0
#     while num>0:
#         digit=num%10
#         total+=digit
#         num=num//10
#     if total==9:
#         return True
#     False

# user=eval(input("enter your list"))
# result=list(filter(sum_digit,user))
# print(result)



'''
List me se saare negative numbers filter karo.

nums = [-5, 12, -3, 0, 45, -99, 18]
'''
# user=eval(input("enter your list"))
# result=list(filter(lambda x:x<0,user))
# print(result)



'''
Sirf wahi usernames filter karo jinki length 5 se 10 characters ke beech hai.
usernames = ["raj", "deepak_kumar", "alex99", "superhero_coder", "vikram"]
'''
# user=eval(input("enter your list"))
# result=list(filter(lambda x: len(x)>=5 and len(x)<=10, user))
# print(result)



'''
Active users filter karo jinki age 18 se upar hai.

users = [
    {"name": "Aman", "age": 22, "is_active": True},
    {"name": "Neha", "age": 17, "is_active": True},
    {"name": "Rahul", "age": 25, "is_active": False},
]
'''

# user=eval(input("enter your list of dictionary"))
# result=list(filter(lambda x: x["is_active"] and x['age']>18 , user))
# print(result)



'''
List me se None, empty strings, ya sirf spaces wali strings ko filter out karo.

inputs = ["admin", "", "   ", "guest", None, "editor"]
'''

# user=eval(input("enter your list"))
# result=list(filter(lambda x: x and x.strip() ,user))
# print(result)



'''
Emails me se sirf "@gmail.com" wale filter karo.

emails = ["john@gmail.com", "doe@yahoo.com", "ravi@gmail.com", "hr@company.in"]
'''

# user=eval(input("enter your list"))
# result=list(filter(lambda x: x.endswith("@gmail.com"),user ))
# print(result)