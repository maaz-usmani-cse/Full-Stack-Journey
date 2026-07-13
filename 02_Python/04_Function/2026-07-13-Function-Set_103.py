'''
Case-Insensitive User Management

Task: Map normal usernames to uppercase values, lekin sirf unhe jinka naam 'm' se start hota ho.

Input: users = ["maaz", "rohit", "mohit"]

Expected Output: {"maaz": "MAAZ", "mohit": "MOHIT"}

'''

# def map_username_start_m(l):
#     d={}
#     for i in l:
#         if i[0]=='m':
#             d[i]=i.upper()
#     return d


# user=eval(input("enter your list"))
# result=map_username_start_m(user)
# print(result)







'''
Number and its Cube Mapping

Task: range(1, 6) tak ke saare numbers aur unke cubes ki ek dictionary banani hai.

Expected Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

'''

# def cube_dictioanry(n):
#     d={i:i**3 for i in range(1,n+1) }
#     return d


# user=int(input("enter your number"))
# result=cube_dictioanry(user)
# print(result)







'''
Vowels Count in Words

Task: Ek words ki list di gayi hai. Har word mein kitne vowels (a, e, i, o, u) hain, unka count nikal kar nayi list banani hai.

Input: words = ["apple", "banana", "sky"]

Expected Output: [2, 3, 0]

'''

# def count_vowel_and_consonant(l):
#     d={'a','e','i','o','u','A','E','I','O','U'}
#     res=[]
#     for i in l:
#         count=0
#         for j in i:
#             if j in d:
#                 count=count+1
#         res.append(count)
#     return res


# user=eval(input("enter your list"))
# result=count_vowel_and_consonant(user)
# print(result)







'''
Extract Values from Nested Dictionary

Task: Ek employees details dict se sirf unka name aur salary extract karke nayi dict banani hai jahan key employee_id ho.

Input: data = {101: {"name": "Maaz", "sal": 50000}, 102: {"name": "Vikas", "sal": 30000}}

Expected Output: {101: 50000, 102: 30000}

'''

# def name_saray(d):
#     res={i:d[i]['sal'] for i in d }
#     return res


# user=eval(input("enter your list"))
# result=name_saray(user)
# print(result)








'''
Task: Ek words list se character-to-word mapping banani hai jahan key word ka pehla akshar ho aur value word khud ho (Dhyan rahe, single match map karna hai).

Input: fruits = ["apple", "banana", "cherry"]

Expected Output: {'a': 'apple', 'b': 'banana', 'c': 'cherry'}

'''

# def word_mapping(l):
#     res={i[0]:i for i in l}
#     return res

# user=eval(input("enter your list"))
# result=word_mapping(user)
# print(result)








'''

Task: Student marks dict ko convert karna hai jahan marks ki jagah agar 
$\ge 50$ ho toh "Pass" likha aaye aur chota ho toh "Fail".Input: marks = 
{"Maaz": 90, "Rahul": 40}Expected Output: {"Maaz": "Pass", "Rahul": "Fail"}
'''
# def check_marks(d):
#     res={i: 'pass' if d[i]>=50 else 'fail' for i in d}
#     return res

# user=eval(input("enter your dict"))
# result=check_marks(user)
# print(result)







'''
Combine Two Lists into Dict (With Length Constraint)

Task: zip() ka use karke keys aur values ko jodna hai, lekin wahi keys select karni hain jinki length even ho.

Input: k = ["ab", "abc", "abcd"], v = [1, 2, 3]

Expected Output: {"ab": 1, "abcd": 3}

'''

# def filter_even_keys(l1,l2):
#     res={key:value for key, value in zip(l1,l2) if len(key)%2==0 }
#     return res


# user=eval(input("enter your list"))
# user2=eval(input("enter your list"))
# result=filter_even_keys(user,user2)
# print(result)






'''
Remove Null/None Values from Dictionary

Task: Abhi humne jo not None padha tha, uska live use! Dictionary se saari entries hatani hain jinki value None ho.

Input: profile = {"name": "Maaz", "age": None, "city": "Bhopal"}

Expected Output: {"name": "Maaz", "city": "Bhopal"}

'''
# def filter_none_data(d):
#     res={i:d[i] for i in d if d[i] is not None}
#     return res

# user=eval(input("enter your dict"))
# result=filter_none_data(user)
# print(result)






