
'''
# # Ek string ke har letter ko 3 steps aage badhao. 
# # 'Z' ke baad wapas 'A' aana chahiye. (Hint: (char + 3) % 26).

# # '''

# def encrypt(letter,steps):
#     res = ''
#     for i in letter:
#         if i.isupper():
#             oldposition = ord(i) - ord("A")
#             newposition = (oldposition + steps) % 26  # Fixed: changed newposition to oldposition
#             res = res + chr(newposition + ord('A'))
#         elif i.islower():                             # Fixed: changed isupper() to islower()
#             oldposition = ord(i) - ord('a')
#             newposition = (oldposition + steps) % 26  # Fixed: changed newposition to oldposition
#             res = res + chr(newposition + ord('a'))
#     return res
    
        
# user=input("enter your letter")
# steps=int(input("enter your number"))
# result=encrypt(user,steps)
# print(result)










'''
'aysa function bnao ki tm koi v msg likh k key set krdo aur'
' wo msg lock ho jaye jab samne wala banda jo tm key use kiye the wahi '
'same key wo jab daley tabhi wo msg dekhayi dey'
'''


# def encrypt_decrypt(message,key,choise):
#     res=''
#     if choise==2:
#         keys=-keys
#     for i in message:
#         if i.isalpha():
#             if i.isupper():
#                 oldposition=ord(i)-ord('A')
#                 newposition=(oldposition+key)%26
#                 res=res+chr(newposition+ord('A'))
#             elif i.islower():
#                 oldposition=ord(i)-ord('a')
#                 newposition=(oldposition+key)%26
#                 res=res+chr(newposition+ord('a'))

#         else:
#             res=res+i
#     return res


# message=input("enter your message")
# keys=int(input("enter your key"))
# choise=int(input("enter your choise number"))
# result=encrypt_decrypt(message,keys,choise)
# print(result)








'map emai '
# def map_email(email):
#     first=email[0]
#     index=email.find('@')
#     hidden='*'*len(email[1:index])
#     last=email[index:]
#     return first+hidden+last

# user=input("enter your email")
# result=map_email(user)
# print(result)




'''
Find All Divisors of a Number

Task: Ek integer input lekar, list comprehension se uske saare factors (divisors) nikalne hain.

Input: n = 12

Expected Output: [1, 2, 3, 4, 6, 12]

'''

# def find_divisors(n):
#     res=[i for i in range(1, n+1) if n%i==0]
#     return res

# user=int(input("enter your number"))
# result=find_divisors(user)
# print(result)







'''
Replace spaces with underscores in dictionary values within a list

Task: Dictionaries ki list mein se har employee ke city name ke spaces ko underscore (_) se badalna hai.

Input: emps = [{"name": "A", "city": "New York"}, {"name": "B", "city": "New Delhi"}]

Expected Output: ["New_York", "New_Delhi"]

'''
def add_underscore(l):
    res=[]
    for i in l:
       i['city']=i['city'].replace(' ','_')
       res.append(i)
    return res

user=eval(input('enter your list'))
result=add_underscore(user)
print(result)