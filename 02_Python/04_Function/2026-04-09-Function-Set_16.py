
'.Replace digits appearing exactly twice with 1.'
# def digits_appearing_exactly_twice_with_1(n):
#     l=[]
#     for i in n:
#         count=0
#         for j in n:
#             if i==j:
#                 count=count+1
#         if count==2:
#             l.append(1)
#         else:
#             l.append(i)
#     return l

# user=input("enter a number")
# result=digits_appearing_exactly_twice_with_1(user)
# print(result)








'.	Replace digits appearing once with 2.'
# def Replace_digits_appearing_once_with_2(n):
#     l=[]
#     for i in n:
#         count=0
#         for j in n:
#             if i==j:
#                 count=count+1
#         if count==1:
#             l.append(2)
#         else:
#             l.append(i)
#     return l

# user=input("enter your number")
# result=Replace_digits_appearing_once_with_2(user)
# print(result)









'''
ek aysa program bnao jaha user 1 se 10 k beech daley to even odd nikaley number ka
aur user 11 se 20 k beech daley to 2 s us number ka multiply
aur 21 se 30 k beech daley to square
aur 31 se 40 k beech root square 
aur 41 se 50 k beech cube nikle

'''
# def user_required(n):
#     if n>0 and n<=10:
#         if n%2==0:
#             return "even"
#         else:
#             return "odd"
#     elif n>10 and n<=20:
#         multiply=n*2
#         return multiply
#     elif n>20 and n<=30:
#         square=n**2
#         return square
#     elif n>30 and n<=40:
#         rootsquare=n**0.5
#         return rootsquare
#     elif n>40 and n<=50:
#         cube=n**3
#         return cube


# user=int(input("enter your number"))
# result=user_required(user)
# print(result)









'.Replace digits forming prime numbers with 7.'

# def replace_digit_into7_with_primedigit(n):
#     l=[]
#     for i in n:
#          if int(i)>1:
#             for j in range(2,int(i)):
#                 if int(i)%j==0:
#                      l.append(i)
#                      break
        
#             else:
#              l.append(7)
#          else:
#              l.append(i)
#     return l



# user=input("enter your number")
# result=replace_digit_into7_with_primedigit(user)
# print(result)





'lcm kisi v number ka '
# def lcm(n1,n2):
#     if n1>n2:
#         maaximum=n1
#     else:
#         maaximum=n2
#     for i in range(maaximum,n1*n2+1):
#         if i%n1==0 and i%n2==0:
#           return "lcm is :",i
        
# user1=int(input("enter your number"))
# user2=int(input("enter your number"))
# result=lcm(user1,user2)
# print(result)    
               







'Replace digits forming Fibonacci positions with 8.'
# def replace_fibonacci_series(n):
#     s=str(n)
#     n1=0
#     n2=1
#     fib=[]
#     for i in s:
#         fib.append(n1)
#         add=n1+n2
#         n1=n2
#         n2=add
#     index=0
#     l=[]
#     for i in s:
#         if index in fib:
#             l.append(8)
       
#         else:
#             l.append(int(i))
#         index=index+1
#     return l

# user=int(input("enter your number"))
# result=replace_fibonacci_series(user)
# print(result)





