'1.	Find largest element '
# def largest_element(n):
#     largest=None
#     for i in n:
#         if largest is None or i>largest:
#             largest=i
#     return largest

# user=eval(input("enter your list"))
# result=largest_element(user)
# print(result)






'.	Count even numbers  in list'
# def count_even(n):
#     count=0
#     for i in n:
#         if i%2==0:
#             count=count+1
#     return count

# user=eval(input("enter your list"))
# result=count_even(user)
# print(result)







'.	Count odd numbers '
# def count_odd(n):
#     count=0
#     for i in n:
#         if i%2!=0:
#             count=count+1

#     return count


# user=eval(input("enter your list"))
# result=count_odd(user)
# print(result)
        








'	Find average of list '
# def average_list(n):
#    total=0
#    count=0
#    for i in n:
#       total=total+i
#       count=count+1

#    average=total/count
#    return average

# user=eval(input("enter your lisst"))
# result=average_list(user)
# print(result)









'	Print elements greater than average '
# def greter_than_average(n):
#     total=0
#     count=0
#     l=[]
#     for i in n:
#         total=total+i
#         count=count+1
#     average=total/count
#     for j in n:
#         if j>average:
#             l.append(j)
#     return l

# user=eval(input("enter your list"))
# result=greter_than_average(user)
# print(result)         









'.	Print elements less than average '
# def less_than_average(n):
#     total=0
#     count=0
#     l=[]
#     for i in n:
#         total=total+i
#         count=count+1
#     average=total/count
#     for j in n:
#         if j<average:
#             l.append(j)
#     return l

# user=eval(input("enter your list"))
# result=less_than_average(user)
# print(result)









'.	Remove all even numbers '
# def remove(n):
#     l=[]
#     for i in n:
#         if i%2!=0:
#             l.append(i)
#     return l

# user=eval(input("enter your list"))
# result=remove(user)
# print(result)









'.	Remove all odd numbers '
# def remove_odd(n):
#     l=[]
#     for i in n:
#         if i%2==0:
#             l.append(i)
#     return l

# user=eval(input("enter your list"))
# result=remove_odd(user)
# print(result)









'	Replace even numbers with 0 '
# def replace_even_with_0(n):
#     l=[]
#     for i in n:
#         if i%2==0:
#             l.append(0) 
#         else:
#             l.append(i)
#     return l


# user=eval(input("enter your list"))
# result=replace_even_with_0(user)
# print(result)








'user s input lena hai 10 bar aur usse assending order m krna hai'
# def assending_order():
#     l=[]
#     a=1
#     while a<=10:
#         user=int(input("enter your number"))
#         l.append(user)
#         a=a+1
#     for i in range(len(l)-1):
#         for j in range(i+1,len(l)):
#             if l[i]>l[j]:
#                 temp=l[i]
#                 l[i]=l[j]
#                 l[j]=temp

#     return l


# result=assending_order()
# print(result)









'5input lo user s aur jo input aye uska sum print kro '
# def sum():
#     total=0
#     a=1
#     while a<=5:
#         user=int(input("enter your number"))
#         total=total+user
#         a=a+1
#     return total

# result=sum()
# print(result)
    









'user s 5 in put lo aur list m dalo'
# def insert_5_element ()  :
#     l=[]
#     a=1
#     while a<=5:
#         user=int(input("enetr your number"))
#         l.append(user)
#         a=a+1
#     return l

# result=insert_5_element()
# print(result)



