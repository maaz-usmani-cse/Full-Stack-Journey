'''
Aapko ek password string di hai. Security ke liye, aapko us password ke shuruat ke
saare aksharon को badal kar star ("*") lagana hai, par niyam yeh hai ki aakhri ke 2 characters
saaf-saaf dikhne chahiye, baaki sab chhup jayein!
Real Example: password = "maazusmani123"
'''

# def map_password(password):
#     star='*' * (len(password)-2)
#     last_two=password[-2:]
#     return star+last_two

# user=input("enter your password")
# result=map_password(user)
# print(result)





'''
Ek user ne apni email ID dali, jaise "maaz123@gmail.com". Security ke liye 
aapko email ke username (yani @ se pehle ka hissa) ke pehle akshar ko chhod kar baaki sabko
* mein badalna hai, aur @gmail.com waale hisse ko bilkul nahi chhedna hai!
Real Example: email = "maaz123@gmail.com"

Output: "m******@gmail.com"

'''

# def map_email(email):
#     first_letter=email[0]
#     skip=email.find('@')
#     stars='*' * (skip-1)
#     domain=email[skip:]
#     return first_letter+stars+domain

# user=input("enter your email")
# result=map_email(user)
# print(result)






'''
Agar aapke blog par koi comment mein bad-word likhta hai, toh use censor karna hai.
Aapko ek sentence diya jayega. Agar usme "bad" word aata hai, toh use "***" (teen stars) se replace kar dena hai.
Real Example: sentence = "This project design is very bad"

Output: "This project design is very ***"

'''
# def censor_cmnt(word):
#     for i in range(len(word)):
#       clean= word.replace('bad','***')
#       return clean

# user=input("enter your password")
# result=censor_cmnt(user)
# print(result)
      





'''
Aapko ek string di hai. Aapko us string ke andar se saare vowels (a, e, i, o, u)
ko hatana (remove) hai aur bachi hui string ko return karna hai.
Real Example: s = "django"

Output: "djng"

'''

# def remove_vowels(word):
#     res=''
#     for i in word:
#         if i not in ['a','e','i','o','u']:
#             res=res+i
#     return res


# user=input("enter your word")
# result=remove_vowels(user)
# print(result)





'''
 Aapko users ki ek list di hai jahan har user ek dictionary hai: users = [{"name": "Maaz", "age": 21, "is_active": True}, {"name": "Rahul", "age": 16, "is_active": True}, {"name": "Amit", "age": 25, "is_active": False}].
Aapko sirf ek line mein un users ke naam (name) nikaal kar nayi list banani hai jo Active bhi hon (True) aur unki age 18 ya 18 se zyada bhi ho!
Real Example: users ki upar wali list ka output aana chahiye $\rightarrow$ ["Maaz"] (Kyunki Rahul active hai par chota hai, aur Amit bada hai par inactive hai).
'''


# def filter_data(l):
#     res=[i['name']for i in l if 'is_active'in i and 'age' in i and i['is_active']==True and i['age']>18 ]
#     return res

# user=eval(input("enter your list"))
# result=filter_data(user)
# print(result)





'''
Aapko ek Matrix (2D List) di hai jisme alag-alag numbers hain. Aapko Nested List 
Comprehension (loop ke andar loop) ka use karke is matrix ko ek single 1D list mein badalna hai,
par niyam yeh hai ki sirf Even numbers hi us list mein jaana chahiye, Odd numbers gayab ho jana chahiye!
Real Example: matrix = [[1, 2, 3], [4, 5, 6], [7, 8]]

Output: [2, 4, 6, 8]
'''

# def even_1d_list(l):
#     res=[j for i in l for j in i if j%2==0]
#     return res


# user=eval(input("enter yyour list"))
# result=even_1d_list(user)
# print(result)


'''

Aapko employees ki salaries ki ek list di hai. Agar kisi ki salary 50,000 ya usse zyada hai, 
toh usme se 10% tax minus karna hai (yani salary ko 0.9 se multiply karna hai). Aur agar salary 50,000 se kam hai,
toh use bina chhede ditto rkhna hai. Yeh poora kaam single line mein hona chahiye!
Real Example: salaries = [40000, 60000, 50000, 30000]

Output: [40000, 54000.0, 45000.0, 30000]

'''

# def calculate_tax(l):
#     res=[i*0.9 if i>=50000 else i for i in l ]
#     return res

# user=eval(input("enter your list"))
# result=calculate_tax(user)
# print(result)







'''
Aapko alag-alag emails ki ek list di hai. Aapko ek line ke andar saare emails mese unka Domain Name
(yani @ ke baad aur .com se pehle ka naam) nikaalna hai!
Real Example: emails = ["maaz@gmail.com", "bhopal@yahoo.com", "cbr@outlook.com"]

Output: ["gmail", "yahoo", "outlook"]

'''

# def find_domain_email(l):
#    res=[i.split('@')[1].split('.')[0]for i in l]
#    return res


# user=eval(input("enter your list"))
# result=find_domain_email(user)
# print(result)
    


'''
Aapko alag-alag emails ki ek list di hai. Aapko ek line ke andar 
saare emails mese unka
Username (yani @ se pehle ka naam) nikaal kar list banani hai.
Real Example: emails = ["maaz@gmail.com", "bhopal@yahoo.com", 
"cbr@outlook.com"]

Output: ["maaz", "bhopal", "cbr"]

# '''
# def find_user_name(l):
#     res=[i.split('@')[0]for i in l]
#     return res


# user=eval(input("enter your list"))
# result=find_user_name(user)
# print(result)










'''
Ek user ne form fill karte waqt kuch fields khali chhod diye ya sirf spaces de diye.
Aapko strings ki ek list di hai, aapko ek line mein saare khali elements (empty strings ""
ya sirf space " ") ko filter karke baahar nikaalna hai.
Real Example: inputs = ["Maaz", "", "Bhopal", "   ", "Django"]

Output: Ek user ne form fill karte waqt kuch fields khali chhod diye ya sirf spaces de diye. Aapko strings ki ek list di hai, aapko ek line mein saare khali elements (empty strings "" ya sirf space " ") ko filter karke baahar nikaalna hai.
Real Example: inputs = ["Maaz", "", "Bhopal", "   ", "Django"]

Output: ["Maaz", "Bhopal", "Django"]
'''

# def clean_data(l):
#    result=[i for i in l if isinstance(i,str) and i.strip()]
#    return result


# user=eval(input("enter your list"))
# result=clean_data(user)
# print(result)




