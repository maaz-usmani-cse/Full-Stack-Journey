'''

Find Common Characters Between Two Strings

Task: Bina duplicates ke, do strings ke bich ke common characters ki list banani hai.

Input: s1 = "hello", s2 = "world"

Expected Output: ['e', 'l', 'o'] (order can vary, but unique characters
'''

# def find_common_characters(s1,s2):
#     d={}
#     res=[]
#     for i in s1:
#         d[i]=True
#     for j in s2:
#         if j in d:
#             res.append(j)
#             del d[j]
#     return res

# s1=input("enter your word")
# s2=input("enter your word")
# result=find_common_characters(s1,s2)
# print(result)






'''
Find Indices of All Occurrences of an Element

Task: enumerate() se ek list mein kisi specific number ke saare indices ki list nikalni hai.

Input: nums = [1, 2, 3, 2, 4, 2], target = 2

Expected Output: [1, 3, 5]

'''


# def find_indices(l,target):
#     res=[]
#     for index,value in enumerate(l):
#         if value==target:
#             res.append(index)
#     return res

# user=eval(input("enter your list"))
# target=int(input("enter your target"))
# result=find_indices(user,target)
# print(result)






'''
Ceil and Floor Mock Modification

Task: Agar number float hai aur point ke baad value .5 ya usse badi hai toh round-up (+1 integer), nahi toh round-down (integer part only). Do it without using standard math module function.

Input: floats = [2.3, 4.7, 5.5, 1.2]

Expected Output: [2, 5, 6, 1]

'''

# def custom_round(l):
#     res=[]
#     for i in l:
#         integer_part=int(i)
#         float_part=i-integer_part
#         if float_part>=0.5:
#             res.append(integer_part+1)
#         else:
#             res.append(integer_part)
#     return res


# user=eval(input("enter your list"))
# result=custom_round(user)
# print(result)







'''
Task: Student marks dict ko grades mein convert karna hai
 ($>80 \rightarrow 'A'$, $50 \text{ to } 80 \rightarrow 'B'$, $<50 \rightarrow 'F'$).Input: marks = 
{"Maaz": 92, "Rohit": 65, "Amit": 42}Expected Output: {"Maaz": "A", "Rohit": "B", "Amit": "F"}

'''

# def convert_grade_marks(d):
#     res={i:'A' if d[i]>80  else ('B' if d[i]>=50 else 'F') for i in d}
#     return res


# user=eval(input('enter your list'))
# result=convert_grade_marks(user)
# print(result)









'''
Vowel-Consonant Count Dictionary

Task: Ek string ke words ko key banana hai aur value mein ek sub-dict rakhni hai jo vowel aur consonant count bataye.

Input: words = ["python", "app"]

Expected Output: {"python": {"v": 1, "c": 5}, "app": {"v": 1, "c": 2}}

'''

# def vowel_consonant_count(l):
#     d={}
#     vowels={'a':True,'e':True,'i':True,'o':True,'u':True}
#     for i in l:
#         d[i]={'v':0,'c':0}
#         char_lower=i.lower()
#         for j in char_lower:
#             if j.isalpha():
#               if j in vowels:
#                   d[i]['v']=d[i]['v']+1
#               else:
#                   d[i]['c']=d[i]['c']+1

#     return d


# user=eval(input("enter your list"))
# result=vowel_consonant_count(user)
# print(result)

