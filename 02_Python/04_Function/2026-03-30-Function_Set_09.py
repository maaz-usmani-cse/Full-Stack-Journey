'''
ek function likho jo saare zeros ko utha kar list ke aakhri mein phenk de, lekin baaki numbers ka order wahi rahe.

Input: [0, 1, 0, 3, 12]

Output: [1, 3, 12, 0, 0]

# '''
# def oneside_zero(n):
#     l1=[]
#     l2=[]
#     for i in n:
#         if i==0:
#             l1.append(i)
#     for j in n:
#         if j!=0:
#             l2.append(j)
#     re=l2+l1
#     return re

# user=eval(input("enter your number"))
# result=oneside_zero(user)
# print(result)



'''
ek list di hai, usme har number kitni baar aaya hai uska count batao. Wo chahte hain ki aap Dictionary ka use karo.

Input: [1, 2, 8, 3, 2, 2, 2, 5, 1]

Output: {1: 2, 2: 4, 8: 1, 3: 1, 5: 1}


'''


# def list_frequency_count(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1

#     return d

# user=eval(input("enter your number"))
# result=list_frequency_count(user)
# print(result)



' Leap Year Function (TCS Interview Logic)'
# def leap_year(n):
#     if n%100==0 and n%4==0 or n%400==0:
#         return n,"leap year hai"
#     else:
#         return n, "leap year nahi hai "
    
# user=int(input("enter your number"))
# result=leap_year(user)
# print(result)

