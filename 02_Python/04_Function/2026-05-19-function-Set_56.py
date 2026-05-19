'''
User tumhe ek list dega aur ek single target digit dega. Tumhe list ke har number ke andar jana hai aur agar usme wo target digit baithi hai, toh use hata dena hai (delete kar dena hai). Agar hatne ke baad kuch na bache, toh wahan 0 daal do.

Input Format: l = eval(input("Enter list: "))
target = input("Enter digit to remove: ")

Test Input: l = [515, 254, 55], target = "5"

Expected Output: [1, 24, 0]

'''
# def replace_traget_digit(l,target):
#    for i in range(len(l)):
#       digit=str(l[i])
#       new_num=''
#       for j in digit:
#          if int(j)==target:
#             continue
#          new_num=new_num+j
#       if new_num=='':
#          l[i]=0
#       else:
#          l[i]=int(new_num)
#    return l


# user=eval(input("enter your list"))
# target=int(input("enter your target number"))
# result=replace_traget_digit(user,target)
# print(result)    









'''

Ek list ke har element ko uthao aur uske ek-ek akshar (digit) ko check karo:

Agar akshar Prime (2, 3, 5, 7) hai, toh use 1 se replace karo.

Agar akshar Non-Prime / Composite (0, 1, 4, 6, 8, 9) hai, toh use 0 se replace karo.

Phir saare naye 1 aur 0 ko wapas chipka kar (concatenate karke) naya number bana do.

'''

# def replace_prime_1_composite_0(l):
#     for i in range(len(l)):
#          prime_digit=[2,3,5,7]
#          digit=str(l[i])
#          new_num=''
#          for j in digit:
#             if int            if int(j) in prime_digit:
#                 new_num=new_num+'1'
#             else:
#                 new_num=new_num+'0'
#          l[i]=int(new_num)
#     return l


# user=eval(input("enter your list"))
# result=replace_prime_1_composite_0(user)
# print(result)







'''

Tumhe ek aisa Generator Function banana hai jo har baar next()
 call karne par us number 
ki sirf agli
 ODD digit nikal kar yield kare. Agar number ke saare digits khatam ho jayein,
 toh generator band ho jaye.
'''

# def odd_digit_generator(n):
#     digit=str(n)
#     for i in digit:
#         if int(i)%2!=0:
#             yield int(i)

# user=input("enter your number")
# result=odd_digit_generator(user)
# print(next(result))
# print(next(result))









'''
Tumhe ek aisa Generator Function banana hai jo Fibonacci Series
($0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55\dots$) ke numbers ek-ek karke
generate kare.Lekin isme ek bahut tagda twist hai:Agar raste mein koi aisa
Fibonacci number aaye jo ek Prime Number bhi hai (jaise $2, 3, 5, 13\dots$),
toh generator ko wo number yield nahi karna hai! Prime number aate hi
 use silently continue (skip) kar dena hai
 aur agle number par badh jana hai.

'''

# def skip_prime_only_fibonacci( ):
#     x=0
#     y=1
#     while True:
#         prime=True
#         if x<2:
#             prime=False
#         else:
#             for i in range(2,int(x**0.5)+1):
#                 if x%i==0:
#                     prime=False
#                     break
#             if prime:
#                add=x+y
#                x=y
#                y=add
#                continue
#         yield x
#         add=x+y
#         x=y
#         y=add

# result=skip_prime_only_fibonacci()
# print(next(result))   
# print(next(result))   
# print(next(result))   
# print(next(result))   















'Maan lo tum Cybrom Technology ke server ke liye ek security tool bana rahe ho.'
' Server par lagatar lakhon lines ke logs generate ho rahe hain.'
' Tumhe ek aisa Generator Function banana hai jo un logs ko ek-ek karke check kare'
' (yaani stream kare) aur sirf un lines ko yield kare jisme koi suspicious activity'
' (jaise "ERROR" ya '
'"UNAUTHORIZED") likhi ho.'
'''
Agar line mein "ERROR" mile $\rightarrow$ Score 5 do.Agar line mein
 "UNAUTHORIZED" mile $\rightarrow$ Score 10 do (Yeh zyada khatarnak hai!).
 Agar dono mil 
jayein $\rightarrow$ Score 15 do!
'''


# def security_checking_in_server(l):
#     score=0
#     for i in l:
#         if 'UNAUTHORIZED' in i and' ERROR':
#             score=15
#             yield(i,score)
#         elif  'UNAUTHORIZED' in i:
#             score=10
#             yield(i,score)
#         elif  'ERROR' in i:
#             score=5
#             yield(i,score)


# user=["INFO: User maaz logged in successfully.",
#     "ERROR: Database connection timeout.",
#     "INFO: Page rendered in 24ms.",
#     "UNAUTHORIZED: Hackers trying to brute force admin page!",
#     "ERROR: UNAUTHORIZED access detected on port 8080!",
#     "INFO: System backup completed."
# ]
# result=security_checking_in_server(user)
# print(next(result))
# print(next(result))

        
