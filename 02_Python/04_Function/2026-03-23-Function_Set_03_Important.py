
'Count Kr K Btao Ki Koi word M Kon sa Letter Kitni Dffa Aayaa HAi'

# def counter(n):
#     result=''
#     for i in n:
#         if i not in result:
#             total=0
#             for j in n:
#                 if i==j:
#                    total=total+1
#             print(i,total,end=' ')
#             result=result+i



# user=input('enter your number')
# result=counter(user)
# print(result)
        


'''
**kwargs ka use karke ek student profile generator function banao.
'''

# def student_profile(name,**kwrgs):
    
#       return kwrgs

# result=student_profile("rahul",Age=20,Course="Python",City="Bihar")
# print(result)


'Global variable ko function ke andar modify karke dikhao. kya iska btao'

# x=10
# def modify_variable():
#     global x
#     x=x+10
#     return x

# result=modify_variable()
# print(result)




'Ek function jo list mein se "n" smallest elements return kare.'
# def smallest_element(n):
#     smallest=None
#     for i in n:
#         if smallest is None or i<smallest:
#             smallest=i
#     return smallest

# user=eval(input("enter your number"))
# result=smallest_element(user)
# print(result)



'Ek function jo di gayi string mein har character ki frequency count kare.'
# def frequency_count(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# user=input("enter your number")
# result=frequency_count(user)
# print(result)


'Ek function jo random password generate kare (Length user se le).'

# import random
# import string
# def generated_password(password):
#     letters=string.ascii_letters
#     digit=string.digits
#     symbol=string.punctuation
#     all_characters=letters+digit+symbol
#     if password<8:
#         return "Error: Security ke liye kam se kam 8 characters rakhein!"
#     passwords=''.join(random.choice(all_characters)for i in range(password))
#     return passwords

# result=generated_password
# print(result)



