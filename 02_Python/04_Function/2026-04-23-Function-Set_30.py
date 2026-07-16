
'''
Ek function likho jo do numbers lower aur upper range accept kare aur uske beech ke saare prime numbers print kare. Agar range invalid ho (negative numbers), toh "Invalid Input" return kare.

Sample Input: 2, 10

Sample Output: 2 3 5 7

'''

# def prime(lower, upper):
#     if lower < 0 or upper < 0:
#         print('invalid input')
#         return 
#     l=[]
#     for i in range(lower, upper + 1):
#         if i > 1:
#             for j in range(2, int(i**0.5) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 l.append(i)
#     return l


# lower=int(input("enter your number"))
# upper=int(input("enter your number"))
# result=prime(lower,upper)
# print(result)










'count kro word m kon sa word kitne bar aya hai '

# def count(n):
#     res=''
#     for i in n:
#         if i not in res:
#           char_count=0
#           for j in n:
#             if i==j:
#                 char_count=char_count+1
#           print(i,char_count,end=' ')
#           res=res+i
   

# user=input("enetr your mesage")
# count(user)











'''
# # Ek string ke har letter ko 3 steps aage badhao. 
# # 'Z' ke baad wapas 'A' aana chahiye. (Hint: (char + 3) % 26).

# # '''


# def encrypt(letters,steps):
#     res=''
#     for i in letters:
#         if i.isupper():
#             old_position=ord(i)-ord('A')
#             new_position=(old_position+steps)%26
#             res=res+chr(new_position+ord('A'))
#         elif i.islower():
#             old_position=ord(i)-ord('Z')
#             new_position=(old_position+steps)%26
#             res=res+chr(new_position+ord('a'))
    
#         else:
#             res=res+i
#     return res


# letters=input("enter your letters:")
# steps=int(input("enter your steps"))
# result=encrypt(letters,steps)
# print(result)











'aysa function bnao ki tm koi v msg likh k key set krdo aur'
' wo msg lock ho jaye jab samne wala banda jo tm key use kiye the wahi '
'same key wo jab daley tabhi wo msg dekhayi dey'
# def encrypt_decrypt(meesage,steps,choise):
#     res=''
#     for i in meesage:
#         if i.isalpha():
#            if i.isupper():
#               old_position=ord(i)-ord('A')
#               if choise==1:
#                   new_position=(old_position+steps)%26
#               elif choise==2:
#                   old_position=ord(i)-ord('A')
#                   new_position=(old_position-steps)%26
#               res=res+chr(new_position+ord('A'))
#            elif i.islower():
#                  old_position=ord(i)-ord('a')
#                  if choise==1:
#                    new_position=(old_position+steps)%26
#                  elif choise==2:
#                      new_position=(old_position-steps)%26
#                  res=res+chr(new_position+ord('a'))
#         res=res+i
#     return res


# message=input("enter your letter:")
# steps=int(input("enetr your steps"))
# choise=int(input("enter your choise: lock for 1: unlock for 2"))
# result=encrypt_decrypt(message,steps,choise)
# print(result)




