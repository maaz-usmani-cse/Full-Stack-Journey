'''
Numbers ki list mein pehla number waise hi rakho, baaki har number ke liye pichhle number se uska difference (current - previous) likho.

Input: nums = [10, 14, 12, 18, 25]

Expected Output: [10, 4, -2, 6, 7]

'''
# def diffrence_number(l):
#     res=[l[0]]
#     for i in range(1,len(l)):
#         diff=l[i]-l[i-1] 
#         res.append(diff)
#     return res

# user=eval(input("enter your list"))
# result=diffrence_number(user)
# print(result)
    


'''
insert Hash Between Alternate Odd Numbers

Task: String/List mein agar lagaataar do Odd numbers aayein, toh unke beech '#' insert karo.

Input: s = "13479"

Expected Output: "1#347#9" (1 aur 3 odd hain, 7 aur 9 odd hain)
'''
# def hash_between_alternate_odd(s):
#     if not s:
#         return ''
#     res=s[0]
#     for i in range(1,len(s)):
#         if s[i-1].isdigit() and s[i].isdigit():
#             if int(s[i-1])%2!=0 and int(s[i])%2!=0:
#                 res=res+'#'
#         res=res+s[i]
#     return res


# user=input("enter your word")
# result=hash_between_alternate_odd(user)
# print(result)




'''
Collapse Consecutive Zeros to Count

Task: List mein non-zero numbers ko waise hi rakho, lekin continuous zeros ke group ko unke total count se replace karo.

Input: nums = [1, 0, 0, 0, 5, 0, 0, 8]

Expected Output: [1, "3z", 5, "2z", 8]

'''

# def collapse_consecutive_zeros(l):
#     res=[]
#     zero_count=0
#     for i in l:
#         if i==0:
#             zero_count+=1
#         else:
#             if zero_count>=1:
#                 res.append(f"{zero_count}z")
#                 zero_count=0
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# result=collapse_consecutive_zeros(user)
# print(result)




'''
Find the First Repeating Adjacent Element

Task: Poori string ya list mein pehla aisa element return karo jo apne turant agle element ke barabar ho.

Input: s = "abcaaddeee"

Expected Output: 'a' (kyunki 'aa' sabse pehle aaya)
'''

# def find_first_repeating_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             return f"first repeatins {i}"
#         else:
#             d[i]=True
#     return f"no one is dublicate"

# user=input("enter your word")
# result=find_first_repeating_element(user)
# print(result)



'''
Compress String with Uppercase-Lowercase Mix

Task: Consecutive characters ko count karo, lekin case-insensitive tareeqe se ('a' aur 'A' ko same maano) aur compressed format mein lowercase character use karo.

Input: s = "aAaBbBcC"
Expected Output: "a3b3c2"
'''
# def compress_string_upper_lower(s):
#     s=s.lower()
#     total=1
#     res=''
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             total+=1
#         else:
#             res=res+f"{s[i]}{total}"
#             total=0
#     res=res+f"{s[-1]}{total}"
#     return res

# user=input("enter your word")
# result=compress_string_upper_lower(user)
# print(result)



'''
Truncate Consecutive Repeated Words in Sentence

Task: Sentence mein agar koi word lagaataar do ya zyada baar aaye, toh use sirf ek baar rakho.

Input: s = "this is is a a good good day"

Expected Output: "this is a good day"
'''

# def truncate_consecutive_repeated(s):
#     s=s.split()
#     res=''
#     for i in range(len(s)-1):
#         if s[i]!=s[i+1]:
#             res=res+' ' +s[i]
#     res+=' '
#     return res

# user=input("enter your word")
# result=truncate_consecutive_repeated(user)
# print(result)



