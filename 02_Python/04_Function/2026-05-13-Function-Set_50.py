# multipliers = [lambda x: i * x for i in range(4)]
# # Agar hum ye execute karein:
# print([m(2) for m in multipliers])


'''
Find difference between max and min
'''
# def find_max_min(l):
#     max_val=None
#     min_val=None
#     for i in l:
#         if max_val is None or i>max_val:
#             max_val=i
#         if min_val is None or i<min_val:
#             min_val=i
#     diff=max_val-min_val
#     return diff


# user=eval(input("enter your list"))
# result=find_max_min(user)
# print(result)



'Keep only numbers divisible by 2 '
# def keep_only_divisible_by_2(l):
#     even=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#     return even

# user=eval(input("enter your list"))
# result=keep_only_divisible_by_2(user)
# print(result)




'chek karo ki user n jo password diya wo pure trh s strong h n'
# def is_password_strong(password):
#     has_digit=any(i.isdigit() for i in password)
#     has_alphabet=any(i.isalpha() for i in password)
#     has_symbol=any(not i.isalnum() for i in password)
#     if not(has_alphabet and has_symbol and has_symbol):
#         return 'security k liye ek number ek digit ek alphabet hona zrrori hai bhai mere'
#     return 'succes'

# user=input('enter your message')
# result=is_password_strong(user)
# print(result)






# s='m@1'
# symbol=any(not i.isalnum() for i in s)
# if symbol:
#     print('symbol hai')
# else:
#     print('symbol nahi hai')





'"Kya koi number 100 se bada hai? whith genarator"'
# user=eval(input("enter your list"))
# result=any(i>100 for i in user)
# print(result)






' W.A.P. to display unique value in a tuple.'
# def unique_value(l):
#     unique=[]
#     for i in l:
#         if i not in unique:
#             unique.append(i)
#     return tuple(unique)


# l=eval(input("enter your list"))
# result=unique_value(l)
# print(result)





' W.A.P. to find squrw root of any number without using pre defined '

# def find_sqrt_desi(n):
#     if n < 0: return "Not possible"
#     if n == 0: return 0
    
#     # Humne guess kiya ki root n hi hai
#     guess = n
    
#     # Loop chalao (jaise tumne count ke liye chalaya tha)
#     # 10-20 baar mein hi ye ekdam sahi answer par pahunch jata hai
#     for i in range(20): 
#         # Bina kisi operator ke, bas basic math
          # guess = (guess + (n / guess)) / 2
        
#     return guess



# user=int(input("enter your number"))
# result=find_sqrt_desi(user)
# print(result)







' W.A.P.  to find the sum of prime number in a list.'
# def find_square_root(n):
#     squarer_root=n
#     for i in range(20):
#         squarer_root=(squarer_root+(n/squarer_root))/2
#     return squarer_root


# user=int(input("enter your number"))
# result=find_square_root(user)
# print(result)
        




'check the symbol in given string'

# s='123maaz'
# has_digit=any(not i.isalnum() for i in s)
# if has_digit:
#     print('symbom hai')
# else:
#     print('symbol nahi hai ')



