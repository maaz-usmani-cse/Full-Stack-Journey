
'''
 Majority Element (Sabse Zyada Shor)List mein wo number dhoondo jo list ki aadhi
 length se zyada baar aaya ho.Example: [3, 2, 3] $\rightarrow$ Output: 
 3 (Kyunki 3 do baar aaya hai aur list ki length 3 hai).Hint: Isme tumhe ek loop ke andar dusra loop 
chalakar "count" karna padega ki kaun kitni baar aaya.

'''
# def find_elemnt(n):
#     half_list=len(n)/2
#     for i in n:
#         count=0
#         for j in n:
#             if i==j:
#                 count=count+1
#         if count >half_list:
#             return i
#     return 'no majority element'


# user=eval(input("enetr your list"))
# result=find_elemnt(user)
# print(result)







'.	Count even numbers '
# def count_even(l):
#     count=0
#     for i in l:
#         if i%2==0:
#             count=count+1
#     return count

# user=eval(input("enetr your list"))
# result=count_even(user)
# print(result)







'Remove all even numbers '
# def remove(n):
#     l=[]
#     for i in n:
#         if i%2!=0:
#             l.append(i)
#     return l

# user=eval(input("enetr your list"))
# result=remove(user)
# print(result)









'.	Replace even numbers with 0 '
# def replace_even_number(l):
#     replace=[]
#     for i in l:
#         if i%2==0:
#             replace.append(0)
#         else:
#             replace.append(i)
#     return replace


# user=eval(input("enter your list"))
# result=replace_even_number(user)
# print(result)







'Remove numbers divisible by 5 '
# def remove_5(n):
#     l=[]
#     for i in n:
#         if i%5!=0:
#             l.append(i)
#     return l

# user=eval(input("enter your list"))
# result=remove_5(user)
# print(result)









'Replace negative numbers with 0 '
# def replace_negative_number(l):
#     repalce=[]
#     for i in l:
#         if i<0:
#             repalce.append(0)
#         else:
#            repalce.append(i)
#     return repalce

# user=eval(input("enter your list"))
# result=replace_negative_number(user)
# print(result)








'''

.	Count numbers greater than 10 

'''
# def count_greater_10(n):
#     count=0
#     for i in n:
#         if i>10:
#             count=count+1
#     return count

# user=eval(input("enter your list"))
# result=count_greater_10(user)
# print(result)
