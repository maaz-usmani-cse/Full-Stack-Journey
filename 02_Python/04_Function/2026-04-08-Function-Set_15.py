'jo value do s zyadh ayi h waha waha 0'

# def replace(n):
#     l=[]
#     for i in n:
#         count=0
#         for j in n:
#             if i==j:
#                 count=count+1
#         if count>2:
#             l.append(int(0))
#         else:
#             l.append(int(i))
#     return l

# user=input("enter your number")
# result=replace(user) 
# print(*result)       





'bina ** ka use kiye cube kro kisi number k'
# def cube(n):
#     l=[]
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 l.append(k)
#     return len(l)
        


# while True:
#   user=int(input("enter your number"))
#   if user==1:
#      break
#   result=cube(user)
#   print(result)








'.	Replace digits appearing exactly twice with 1.'


# def Replace_digit_appearing2_with_1(n):
#    l=[]
#    for i in n:
#       count=0
#       for j in n:
#          if i==j:
#             count=count+1
#       if count==2:
#          l.append(1)
#       else:
#          l.append(int(i))
#    return l


# user=input("enter your number")
# result=Replace_digit_appearing2_with_1(user)
# print(result)





'Ek list ke numbers ko divide karo, lekin agar beech mein 0 aaye toh skip kar do.'

# def devide_skip0(n):
#     l=[]
#     for i in n:
#         try:
#            devide= 100/i
#            l.append(i)
#         except:
#             l.append(i)

#     return l
# user=eval(input("enetr your list"))
# result=devide_skip0(user)
# print(result)







'Ek list mein numbers aur strings dono hain, sirf numbers ko add karo.'
# def only_add_numbers(n):
#     add=0
#     for i in n:
#        try:
#           add=add+i
#        except:
#           pass 
#     return add



# user=eval(input("enter your list"))
# result=only_add_numbers(user)
# print(result)          





'User se fruit ka naam pucho, agar wo menu mein nahi hai toh error handle karo.'

# def check_items(menu,fruitsname):
#     for i in menu:
#         try:
#             return "items availabe:",user[menu]
#         except:
#             return "item not avialable"
        

 
# menu=eval(input("enter your dict"))
# user=input("kya chaiyer??")
# result=check_items(menu,user)
# print(result)






'if else kl through key check '

# def keys(d,key):
#         if key in d:
#                 return "available hai"
#         else:
#                 return "availabler nahi hai bhai"


# d=eval(input("enter your dict"))
# key=input("enter your key")
# result=keys(d,key)
# print(result)






