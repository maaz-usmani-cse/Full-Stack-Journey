'''
Numbers ki list mein pehla number waise hi rakho, baaki har number ke liye pichhle number se uska difference (current - previous) likho.

Input: nums = [10, 14, 12, 18, 25]

Expected Output: [10, 4, -2, 6, 7]

'''

# def encode_with_diffrenc(l):
#     res=[l[0]]
#     for i in range(1,len(l)):
#         diff=l[i]-l[i-1]
#         res.append(diff)
#     return res

# user=eval(input("enter your list"))
# result=encode_with_diffrenc(user)
# print(result)


'''
Insert Hash Between Alternate Odd Numbers

Task: String/List mein agar lagaataar do Odd numbers aayein, toh unke beech '#' insert karo.

Input: s = "13479"

Expected Output: "1#347#9"
'''
# def insert_hash_between_alternate_odd_number(s):
#     res=''
#     for i in range(len(s)-1):
#       if int(s[i])%2!=0 and int(s[i+1])%2!=0:
#          res=res+s[i]+'#'

#       else:
#          res=res+s[i]
#     res=res+s[-1]
#     return res

# user=input("enter your word")
# result=insert_hash_between_alternate_odd_number(user)
# print(result)

    
    

'''
Question 3: Collapse Consecutive Zeros to Count

Task: List mein non-zero numbers ko waise hi rakho, lekin continuous zeros ke group ko unke total count se replace karo.

Input: nums = [1, 0, 0, 0, 5, 0, 0, 8]

Expected Output: [1, "3z", 5, "2z", 8]
'''
        
# def collapse_consecutive_zerocount(l):
#     res=[]
#     total=0
#     for i in range(len(l)):
#         if l[i]==0:
#             total+=1
#         else:
#             if total>1:
#                 res.append(f"{total}z")
#                 total=0
#             res.append(l[i])
#     if total>0:
#         res.append(f"{total}z")

#     return res

# user=eval(input("enter your list"))
# result=collapse_consecutive_zerocount(user)
# print(result)



'''
Find the First Repeating Adjacent Element

Task: Poori string ya list mein pehla aisa element return karo jo apne turant agle element ke barabar ho.

Input: s = "abcaaddeee"

Expected Output: 'a'
'''
# def find_first_repeating_adjacent(s):
#     d={}
#     for i in s:
#         if i in d:
#             return f"first repeating element is {i}"
#         else:
#             d[i]=True
#     return 'koi number repeat n hua hai'

# user=input("enter your word")
# result=find_first_repeating_adjacent(user)
# print(result)



'''
Compress String with Uppercase-Lowercase Mix

Task: Consecutive characters ko count karo, lekin case-insensitive tareeqe se ('a' aur 'A' ko same maano) aur compressed format mein lowercase character use karo.

Input: s = "aAaBbBcC"

Expected Output: "a3b3c2"
'''
# def compress_string(s):
#     s=s.lower()
#     res=''
#     total=1
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             total+=1

#         else:
#             res=res+s[i]+str(total)
#             total=1

#     res=res+s[-1]+str(total)

#     return res

# user=input("enter your word")
# result=compress_string(user)
# print(result)        



'''
Truncate Consecutive Repeated Words in Sentence

Task: Sentence mein agar koi word lagaataar do ya zyada baar aaye, toh use sirf ek baar rakho.

Input: s = "this is is a a good good day"

Expected Output: "this is a good day"
'''

# def truncate_consecutive_repeated_sentence(s):
#     word=s.split()
#     res=''
#     for i in word:
#         if i not in res:
#             res=res+' '+i
#     return res

# user=input("enter your word")
# result=truncate_consecutive_repeated_sentence(user)
# print(result)

