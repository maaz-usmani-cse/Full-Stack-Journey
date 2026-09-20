'''
Check karo kya string me koi duplicate adjacent character hai (jaise "apple" me "pp").
'''
# def is_dublicate_adjacent_char(s):
#     res=any(s[i]==s[i+1] for i in range(len(s)-1))
#     return res

# user=input("enter your word")
# result=is_dublicate_adjacent_char(user)
# print(result)



'''
Check karo kya string ke saare vowels lowercase hain
'''
# def is_lowercase_vowel(s):
#   vowels='AEIOU'
#   for i in s:
#      if i in vowels:
#         return False
#   return True

# user=input("enter your word")
# result=is_lowercase_vowel(user)
# print(result)



'''
Check karo kya list me koi number Armstrong number hai
'''
# def is_arm_strong(n):
#     temp=n
#     total=0
#     power=len(str(n))
#     while n>0:
#         last_digit=n%10
#         cube=last_digit**power
#         total+=cube
#         n=n//10
#     if total==temp:
#         return True
#     return False


# def is_check_arm_number(l):
#     return any(is_arm_strong(i) for i in l)

# user=eval(input("enter your list"))
# result=is_check_arm_number(user)
# print(result)




'Check karo kya list ka har element range [10, 99] ke andar hai'
# def is_valid_limit_range(l):
#     return all(i>=10 and i<=99 for i in l)

# user=eval(input("enter your list"))
# result=is_valid_limit_range(user)
# print(result)    
    



