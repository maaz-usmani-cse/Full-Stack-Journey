''''
Django admin dashboard ke liye aapko registered emails ki ek list di gayi hai. 
Aapko ek loop chalakar saare valid emails mein se unka domain name (gmail, yahoo, etc.) 
nikaalna hai. Par dhyan rahe, agar list mein koi None ya integer number aa jaye, toh code 
crash nahi hona chahiye!
Real Django Example: emails = ["maaz@gmail.com", None, "bhopal@yahoo.com", 555, "invalid-email"]

Output: ["gmail", "yahoo"]
'''

# def find_domain(l):
#     res=[]
#     for i in l:
#         if i is not None and isinstance(i,str) and '@' in i and '.' in i:
#             domain=i.split('@')[1].split('.')[0]
#             res.append(domain)
#     return res


# user=eval(input("enter your list"))
# result=find_domain(user)
# print(result)






'''
Django user signup form mein kuch users ne apne naam ke aage-piche ya beech mein _ 
(underscore) daal diya hai. Aapko ek loop chalakar saare usernames mese _ ko poori tarah 
saaf karna hai, unhe lowercase mein badalna hai, aur None values ko filter out karna hai.
Real Django Example: usernames = ["maaz_usmani", None, "bhopal_", "_django_developer"]

Output: ["maazusmani", "bhopal", "djangodeveloper"]
'''


# def filter_name(l):
#     res=[]
#     for i in l:
#         if i is not None and isinstance(i,str):
#             remove_underscore=i.replace('_','')
#             res.append(remove_underscore)
#     return res


# user=eval(input("enter your list"))
# result=filter_name(user)
# print(result)







'	Rotate list left by 1 '

# def rotate_list(l):
#     temp=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[-1]=temp

#     return l

# user=eval(input("enter your list"))
# result=rotate_list(user)
# print(result)







'	Rotate list right by 1 '
# def rotate_list(l):
#     temp=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=temp
#     return l


# user=eval(input("enter your list"))
# result=rotate_list(user)
# print(result)







'Rotate list left by k positions '
# def rotate_k_position(l,k):
#     k=k%len(l)
#     position=l[k:]+l[0:k]
#     return position

# user=eval(input("enter your list"))
# k=int(input("enter your number"))
# result=rotate_k_position(user,k)
# print(result)







'Rotate list right by k positions '
# def rotate_lis_k_position(l,k):
#     k=k%len(l)
#     position=l[len(l)-k:]+l[0:len(l)-k]
#     return position


# user=eval(input("enter your list"))
# k=int(input("enter your number"))
# result=rotate_lis_k_position(user,k)
# print(result)   











'Move all zeros to end '
# def move_zero_end(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]!=0:
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp
#             position=position+1
#     return l


# user=eval(input("enter your list"))
# result=move_zero_end(user)
# print(result)


    





'Separate even and odd numbers '
# def separate_even_odd(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]%2==0:
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp
#             position=position+1
#     return l


# user=eval(input("enter your list"))
# result=separate_even_odd(user)
# print(result)




'Sort list without using sort '
# def sort_list(l):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 temp=l[i]
#                 l[i]=l[j]
#                 l[j]=temp
#     return l


# user=eval(input("enter your list"))
# result=sort_list(user)
# print(result)







'Merge two lists '
# def merge_two_list(l1,l2):
#     return l1+l2



# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=merge_two_list(l1,l2)
# print(result)
    








