'''
Task: Agar koi character lagaataar repeat ho toh uska format char(count) banao, agar single ho toh bas character hi rehne do.

Input: s = "abbbccccd"

Expected Output: "ab(3)c(4)d"

'''

# def repeat_continous_char_format(s):
#     res=''
#     count=1
#     for i in range(1,len(s)):
#         if s[i]==s[i-1]:
#             count=count+1
#         else:
#             if count>1:
#                 res=res+f'{s[i-1]}({count})'

#             else:
             
#              res=res+s[i-1]
#             count=1
#     if count>1:
#         res=res+f'{s[-1]}({count})'

#     else:
#         res=res+s[-1]
#     return res

# user=input("enter your word")
# result=repeat_continous_char_format(user)
# print(result)





'''
Check karo ki kya koi word number par khatam ho raha hai.Input: ["apple", "banana1", "cherry"] $\rightarrow$ Output: True
'''

# def is_word_end_with_digit(l):
#     return any(i[-1].isdigit() for i in l )


# user=eval(input("enter your list"))
# result=is_word_end_with_digit(user)
# print(result)





'prime number'
# def is_prime(n):
#     if n<=1:
#         return False

#     if n==2:
#         return True

#     if n%2==0:
#         return False

#     for i in range(3, int(n**0.5)+1 ,2):
#         if n%i==0:
#             return False
#     return True

# user=int(input("enter your number"))
# result=is_prime(user)
# print(result)
