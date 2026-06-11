''''
Ek user registration form se ages (umar) ki ek list aayi hai. Kuch data string mein hai (jaise "21"), kuch pehle se integers hain (25), aur kuch None ya khali strings ("", "   ") hain. Aapko ek normal loop chalakar saare valid ages ko pure integer format (int) mein badalna hai, aur kachra data (None, khali strings) ko safely delete kar dena hai.
Real Django Example: ages = [18, "22", None, "   ", 30, ""]

Output: [18, 22, 30]

'''
# def filter_age_data(l):
#     res=[]
#     for i in l:
#         if i is not None and isinstance(i,str) and i.strip():
#             res.append(int(i))
#         elif isinstance(i,int):
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# result=filter_age_data(user)
# print(result)








'''
Front-end se mobile numbers ki ek list aayi hai. Kuch numbers ke beech mein extra spaces hain (jaise "98765 43210"), kuch pure integer hain, aur kuch None hain. Aapko ek loop chalakar saare numbers ke saare spaces khatam karne hain, unhe string format mein badalna hai, aur None ko filter out karna hai.
Real Django Example: numbers = ["91234 56789", 9876543210, None, " 88888 99999 "]

Output: ["9123456789", "9876543210", "8888899999"]

'''


# def remove_extra_space(l):
#     res=[]
#     for i in l:
#         if i is not None:
#             num_str=str(i)
#             cleann_num=num_str.replace(' ','')
#             if cleann_num:
#                 res.append(cleann_num)
#     return res


# user=eval(input("enter your list"))
# result=remove_extra_space(user)
# print(result)
            








'''
Aapko numbers ki ek list di hai aur ek key number diya hai. Aapko normal 
for loop chalakar batana hai ki wo key list mein kaun se index par baithi hai. 
Agar wo number list mein nahi hai, toh -1 return karna hai.
Real TCS Example: l = [10, 20, 30, 40, 50], key = 40

Output: 3 (Kyunki 40 ka index 3 hai).

'''

# def find_key_position(l,key):
#     for i in range(len(l)):
#         if l[i]==key:
#             return f'index position:{i}'
#     return -1

# user=eval(input("enter your list"))
# key=int(input("enter your key"))
# result=find_key_position(user,key)
# print(result)












'''
E-commerce site ke titles ki ek list aayi hai. Aapko saare valid product titles 
ka pehla akshar Capital (.title()) karna hai. Agar list mein koi number, None, ya
khali string hai, toh use chupchaap filter out (delete) kar dena hai.
Real Django Example: titles = ["python book", 101, "django framework", None, "   "]

Output: ["Python Book", "Django Framework"]

'''


# def first_letter_capitsl(l):
#     res=[]
#     for i in l:
#         if i is not None and isinstance(i,str) and i.strip():
#             first_letter=i.title()
#             res.append(first_letter)
#     return res


# user=eval(input("enter your list"))
# result=first_letter_capitsl(user)
# print(result)










'''

Aapko integers ki ek list di hai. Aapko ek normal loop chalakar ginti karni hai ki list mein total kitne Even (sam) numbers hain aur kitne Odd (vishama) numbers hain, aur unka count ek dictionary ke roop mein return karna hai.
Real TCS Example: nums = [1, 2, 3, 4, 5, 6]

Output: {"even": 3, "odd": 3}
'''

# def count_even_odd(l):
#     even=0
#     odd=0
#     d={}
#     for i in l:
#          if i%2==0:
#             even=even+1
#             d['even']=even
#          else:
#             odd=odd+1
#             d['odd']=odd
#     return d




# user=eval(input("enter your list"))
# result=count_even_odd(user)
# print(result)