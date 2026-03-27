' wap to arrange all even and odd number at a place'
# def arrange_even_odd(n):
#     even=[]
#     odd=[]
#     for i in n:
#         if i%2==0:
#             even.append(i)
#     for j in n:
#         if j%2!=0:
#             odd.append(j)
#     result=even+odd
#     return result


# user=eval(input('enter your number'))
# result=arrange_even_odd(user)
# print(result)



'Ek function likho jo Fibonacci number return kare.'
# def fibonacci(n):
#     x=0
#     y=1
#     for i in range(n):
#         print(x,end=' ')
#         add=x+y
#         x=y
#         y=add
       


# user=int(input("enter your number"))
# print(fibonacci(user))



'ek function likho jo integer input le aur uska reverse return kare, bina use string mein convert kiye (No str() allowed).'
# def reverse_number(n):
#     rev=0
#     while n>0:
#         digit=n%10
#         rev=(rev*10)+digit
#         n=n//10
#     return rev


# user=int(input("enter your number"))
# result=reverse_number(user)
# print(result)



'Second Smallest Element in a List (TCS 2026 Trend)'
# def second_smallest_number(n):
#     if len(n)<2:
#         return "bhai kam s kam 2 element rehnma chaiye tab to aap nikal skte ho second smallest "

 
#     first = float('inf') 
#     second = float('inf')

#     for num in n:
       
#         if num < first:
#             second = first  
#             first = num    
        
#         elif num < second and num != first:
#             second = num

#     return second

# user=eval(input("enter your number"))
# result=second_smallest_number(user)
# print(result)