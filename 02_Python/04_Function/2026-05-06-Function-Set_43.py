'Replace element with next greater element '
# def replace_next_greater(l):
#     next_greater=[-1]*len(l)
#     for i in range(len(l)):
#         for j in range(1,len(l)):
#            index=(i+j)%len(l)
#            if l[index]>l[i]:
#                next_greater[i]=l[index]
#                break
#     return next_greater

# user=eval(input("enter your list"))
# result=replace_next_greater(user)
# print(result)








'Replace element with previous smaller element '

# def replace_with_previous_smaller_element(l):
#     previous_smaller=[-1]*len(l)
#     for i in range(len(l)):
#         for j in range(len(l)-1,0,-1):
#             index=(i-j)%len(l)
#             if l[index]<l[i]:
#                 previous_smaller[i]=l[index]
#     return previous_smaller

# user=eval(input("enter your list"))
# result=replace_with_previous_smaller_element(user)
# print(result)








'Find equilibrium index (left sum = right sum)'
# def iquilibrium_index(l):
#     iquilibrium_index=[]
#     for i in range(len(l)):
#        left_sum=0
#        right_sum=0
#        for j in range(0,i):
#            left_sum=left_sum+l[j]
#        for k in range(i+1,len(l)):
#            right_sum=right_sum+l[k]
#        if left_sum==right_sum:
#             iquilibrium_index.append(i)
#     return iquilibrium_index

# user=eval(input("enter your list"))
# result=iquilibrium_index(user)
# print(result)










'''
Ek list di gayi hai emails ki, 
usme se sirf wahi emails filter karo jo 
.com se end hote hain.
'''
# email=["maaz@gmail.com", "test@yahoo.in", "admin@outlook.com", "user@rits.edu"]
# result=list(filter(lambda x: x.endswith('.com'),email))
# print(result)







'''
Tumhare paas users ki list hai aur tumhe sirf wo users chahiye jo is_active hain aur jinke paas staff status hai.

Python
users = [
    {"username": "maaz", "is_active": True, "is_staff": True},
    {"username": "rahul", "is_active": False, "is_staff": True},
    {"username": "amit", "is_active": True, "is_staff": False},
]

'''
# users = [
#     {"username": "maaz", "is_active": True, "is_staff": True},
#     {"username": "rahul", "is_active": False, "is_staff": True},
#     {"username": "amit", "is_active": True, "is_staff": False},
# ]
# result=list(filter(lambda x: x['is_active']and x['is_staff'],users))
# print(result)





'''
Kayi baar users form mein kuch fields khali chhod dete hain 
ya sirf spaces bhar dete hain. 
Database mein kachra (null values) save karne se pehle use filter karna zaruri hai.

'''
# form_data = ["Maaz", "   ", "Bhopal", "", None, "India"]
# result=list(filter(lambda x: x and x.strip(),form_data))
# print(result)





'''
Question: Ek aisa function banao jo password ko tabhi True de jab:

Length kam se kam 8 ho.

Kam se kam ek Uppercase (A-Z) letter ho.

Kam se kam ek Digit (0-9) ho.

Kam se kam ek Special Character (@, #, $, etc.) ho.

'''
# import string
# def is_strong(password):
#     for i in password:
#         cond1_upper=any(i.upper()for i in password)
#         cond2_digit=any(i.isdigit() for i in password)
#         cond3_char=any(i.isalpha()for i in password)
#         cond4_special_char=any(i in string.punctuation for i in password)
#     if not cond1_upper:
#         return 'please enter a one upper case'
#     if not cond2_digit:
#         return 'please enter minimum one digit'
#     if not cond3_char:
#         return 'please enter minimum one alphabet'
#     if not cond4_special_char:
#         return 'please enter minimum one speacial character'
    

# user=(input("enter your list"))
# result=is_strong(user)
# print(result)




'''

Ek string di gayi hai jisme alphabets, symbols aur numbers mix hain. Tumhe sirf Even Numbers nikalne hain ek list ke andar.

Input: "a1b2c3d4e5f6@8#"

Expected Output: ['2', '4', '6', '8']
'''
# s="a1b2c3d4e5f6@8#"
# result=list(map(int,filter(lambda x: x.isdigit() and int(x)%2==0,s)))
# print(result)