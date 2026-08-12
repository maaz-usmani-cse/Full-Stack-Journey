'''
Ek 2D matrix ko flatten karke 1D list banao, lekin sirf wahi numbers rakho jo even hain aur 5 se bade hain.

Input: matrix = [[1, 8, 3], [4, 10, 6], [7, 2, 12]]

Expected Output: [8, 10, 6, 12]
'''

# def flatten_id(l):
#     return [j for i in l for j in i if j%2==0 and j>5]


# user=eval(input("enter your list"))
# result=flatten_id(user)
# print(result)






'''
Ek sorted list mein se har element aur uski frequency (count) ka tuple (element, count) banao, without using itertools or collections.

Input: nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]

Expected Output: [(1, 3), (2, 2), (3, 1), (4, 4)]
'''

# def element_frequency_tuple(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return [(i,d[i])for i in d]


# user=eval(input("enter your list"))
# result=element_frequency_tuple(user)
# print(result)







'''
Consecutive identical characters wale group banakar unki counts ki list banaon (Jaise compression mein hota hai).

Input: s = "AAABBBCCDAA"

Expected Output: [('A', 3), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]

'''

# def consecutive_identical_character_group(s):
#     if not s:
#         return None

#     res=[]
#     count=1
#     for i in range(1,len(s)):
#         if s[i]==s[i-1]:
#             count=count+1
#         else:
#             res.append((s[i-1],count))
#             count=1

#     res.append((s[-1],count))
#     return res

# user=input('enter your word')
# result=consecutive_identical_character_group(user)
# print(result)
    




'apple a1 p2 l1 e1 output chaiye aysa' 

def count_word_consecutive(s):
    if not s:
        return ""

    res = ""
    count = 1

   
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res += f"{s[i-1]}{count} "
            count = 1

    
    res += f"{s[-1]}{count}"
    return res





user=input("enter your word")
result=count_word_consecutive(user)
print(result)