'Common Elements in Two Lists'
# def is_common_list(l1,l2):
#     res=[]
#     d={}
#     for i in l1:
#         d[i]=True
#     for j in l2:
#         if j in d and j not in res:
#             res.append(j)
#     return res

# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# res=is_common_list(l1,l2)
# print(res)
            

'Check Armstrong Number'
# def is_arm_strong(n):
#     total=0
#     temp=n
#     power=len(str(n))
#     while n>0:
#         digit=n%10
#         cube=digit**power
#         total+=cube
#         n=n//10
#     if total==temp:
#         return True
#     return False


# user=int(input("enter your number"))
# res=is_arm_strong(user)
# print(res)


'Character Frequency in a String'
# def character_freq(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# user=input("enter your dict")
# result=character_freq(user)
# print(result)


'List se ek specific element ke saare occurrences hatao bina .remove() function use kiye.'
# def remove_element(l,target):
#     return[i for i in l if i!=target]

# user=eval(input("enter your list"))
# target=int(input("enter your number"))
# result=remove_element(user,target)
# print(result)



'Find the Longest Word in a Sentence'
# def is_longegest_word(word):
#     longest=None
#     word=word.split()
#     for i in word:
#         if longest is None or i>longest:
#             longest=i
#     return f"longest word is {longest}"

# user=input("enter your sentence")
# result=is_longegest_word(user)
# print(result)

'''
'Sort a List of Strings by Length'

Ek list mein alag-alag lambai (length) ke words diye gaye hain,
unko unki length ke hisaab se ascending order mein sort karo.

'''
# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if len(i)<len(pivot):
#             left.append(i)
#         elif len(i)==len(pivot):
#             middle.append(i)
#         else:
#             right.append(i)

#     return quick_sort_pivot(left)+middle+quick_sort_pivot(right)

# user=eval(input("enter your list"))
# result=quick_sort_pivot(user)
# print(result)


'''
k list ke andar multiple dictionaries hain (jaise students ka data),
unko unke 'marks' ya 'age' ke hisaab se sort karo. Yeh bohot zyada pucha jata hai.
'''
# def sort_students_by_marks(students):
#     if len(students) <= 1:
#         return students

#     # Pivot ke liye pehli dictionary ko chun lo
#     pivot = students[0]

#     left = []
#     middle = []
#     right = []

#     for s in students:
#         if s["marks"] < pivot["marks"]:
#             left.append(s)
#         elif s["marks"] == pivot["marks"]:
#             middle.append(s)
#         else:
#             right.append(s)

   
#     return (
#         sort_students_by_marks(left) + middle + sort_students_by_marks(right)
#     )

# students_list = [
#     {"name": "Maaz", "marks": 85},
#     {"name": "Aadil", "marks": 92},
#     {"name": "Safdar", "marks": 78},
#     {"name": "Rahul", "marks": 95},
#     {"name": "Aman", "marks": 85},  # Same marks wala case check karne ke liye
# ]

# result = sort_students_by_marks(students_list)

# print(result)
