'.	Replace digits forming Fibonacci positions with 8.'
# def replace_digit_fibonacci(n):
#     fib=[]
#     n1=0
#     n2=1
#     for i in n:
#         fib.append(n1)
#         add=n1+n2
#         n1=n2
#         n2=n1
#     l=[]
#     index=0
#     for i in fib:
#         if index in fib:
#             l.append(8)
#         else:
#             l.append(int(i))
#         index=index+1
#     return l

# user=input("enter your number")
# result=replace_digit_fibonacci(user)
# print(result)   




'.	Replace digits whose index is prime with square. with the help of while lopp'
# def prime_position_square(n):
# n=int(input("enter your no. "))
# index=len(str(n))
# new=0
# while n>0:
#     digit=n%10
#     count=0
#     for i in range(1,index+1):
#         if index%i==0:
#             count=count+1
#     if count==2:
#         digit=digit**2
#     n=n//10
#     index=index-1
#     new=new*10+digit
# res=0
# while new>0:
#     digit=new%10
#     res=res*10+digit
#     new=new//10
# print(res)

    
    
'Replace digits whose index is prime with square.'
# def replace_prime_digit(n):
#     l=[]
#     for i in range(len(n)):
#         if i >1:
#             count=0
#             for j in range(2,i):
#                 if i%j==0:
#                     count=count+1
#             if count==0:
#                 digit=int(n[i])
#                 l.append(digit**2)
#             else:
#                 l.append(n[i])
#         else:
#             l.append(n[i])
        
#     return l




# user=input("enter your number")
# result=replace_prime_digit(user)
# print(result)
  








'.	Replace digits whose index is composite with cube.'
# def replace_digit_composite_cube(n):
#     l=[]
#     for i in range(len(n)):
#         if i>1:
#             count=0
#             for j in range(2,i):
#                 if i%j==0:
#                  count=count+1
#             if count==1:
#                 digit=int(n[j])
#                 l.append(digit**3)
#             else:
#                 l.append(n[i])
#         else:
#             l.append(n[i])
#     return l


# user=input("enter your number")
# result=replace_digit_composite_cube(user)
# print(*result ,sep=' ')
        
            


