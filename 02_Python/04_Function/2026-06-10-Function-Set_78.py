'''
Aapko ek $3 \times 3$ ki matrix (2D List) di hai. Aapko uske Primary
Diagonal (yani top-left se bottom-right) ke saare elements ka Sum (jod)
nikalna hai.
Real TCS Example: > ```python
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
'''



# def daiogonal_sum(l):
#     total=0
#     for i in range(len(l)):
#         total=total+l[i][i]
#     return total


# user=eval(input("ente your list"))
# result=daiogonal_sum(user)
# print(result)







'''
Front-end se product prices ki ek list aayi hai. Kuch prices string mein hain
(jaise "500"), kuch integers hain (1200), aur kuch fields khali (None) hain. 
Aapko ek normal loop chalakar saare valid prices ko pure integer format (int)
mein badalna hai, aur None ko safely filter out (delete) kar dena hai bina code crash kiye.
Real Django Example: prices = ["400", 1500, None, "2000"]

Output: [400, 1500, 2000] (Saare elements number hone chahiye).

'''

# def filter_out_string(l):
#     res=[]
#     for i in l:
#        if i is not None and isinstance(i,str) and i.strip():
#            res.append(int(i))
#        elif isinstance(i,int):
#            res.append(i)
#     return res


# user=eval(input("enter your list"))
# result=filter_out_string(user)
# print(result)







'''
Aapko database se users ki ek list mili hai jahan har user ek dictionary hai. 
Aapko un users ke naam (name) nikaal kar nayi list banani hai jo Active hon (is_active: True) aur unka role "Author" ho. Baaki sabko reject kar dena hai.
Real Django Example:

Python
users = [
    {"name": "Maaz", "role": "Author", "is_active": True},
    {"name": "Amit", "role": "Reader", "is_active": True},
    {"name": "Rahul", "role": "Author", "is_active": False}
]
Output: ["Maaz"]

'''

# def is_active_user(l):
#     res=[]
#     for i in l:
#         if 'is_active' in i and 'role' in i:
#             if i['is_active']==True and i['role']=='Author':
#                 res.append(i['name'])

#     return res

       


# user=eval(input("enter your list"))
# result=is_active_user(user)
# print(result)








'''

Django admin dashboard ke liye aapko registered emails ki ek list di gayi hai. 
Aapko ek loop chalakar saare valid emails mein se unka domain name (gmail, yahoo, etc.) 
nikaalna hai. Par dhyan rahe, agar list mein koi None ya number aa jaye, toh code crash nahi 
hona chahiye!
Real Django Example: emails = ["maaz@gmail.com", None, "bhopal@yahoo.com", 555, "invalid-email"]

Output: ["gmail", "yahoo"]
'''


# def find_domain_name(l):
#     res=[]
#     for i in l:
#         if i is not None and isinstance(i,str) and '@' in i and '.' in i:
#             domain=i.split('@')[1].split('.')[0]
#             res.append(domain)
#     return res

# user=eval(input("enter your list"))
# result=find_domain_name(user)
# print(result)









'''
Aapko emails ki ek list di gayi hai jisme kachra data bhi mix hai. Aapko un 
saare valid emails mese unka Username (yani @ se pehle ka naam) nikaalna hai. Agar koi element string nahi hai, ya usme @ nahi hai, ya wo khali string "" hai, toh use bina crash kiye skip kar dena hai.
Real Django Example: data = ["maaz@gmail.com", 404, None, "bhopal@yahoo.com", 
"invalid-email", "   "]

Output: ["maaz", "bhopal"]

# '''
# def clean_data(l):
#     res=[]
#     for i in l:
#         if i is not None:
#               if isinstance(i,str) and i.strip() and '@' in i:
#                    name=i.split('@')[0]
#                    res.append(name)
#     return res


# user=eval(input("enter your list"))
# result=clean_data(user)
# print(result)














'''
Ek input list di hai jisme alag-alag tarah ka data hai. Aapko sirf unhi 
strings ko UPPERCASE (.upper()) mein badalna hai jo asli strings hon aur khali na hon.
None, numbers, ya sirf spaces wali string list se safely delete ho jani chahiye.
Real Django Example: inputs = ["django", 102, "   ", None, "bhopal"]

Output: ["DJANGO", "BHOPAL"]
'''
          
# def upper_case(l):
#     res=[]
#     for i in l:
#         if i is not None and isinstance(i,str) and i.strip():
#             upper=i.upper()
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# result=upper_case(user)
# print(result)
            