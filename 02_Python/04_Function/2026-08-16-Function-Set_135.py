'''
Kisi bhi character ko lagaataar maximum 2 baar hi aane do; agar 2 se zyada baar aaye toh extra characters hata do.

Input: s = "aaabbbccccd"
Expected Output: "aabbccd"

'''

# def max_2_time_every_char(s):
#     res=''
#     prev=None
#     count=0
#     for i in range(len(s)):
#         if s[i]==prev:
#             count=count+1
        
#         else:
#             prev=s[i]
#             count=1

#         if count<=2:
#             res=res+s[i]
#     return res
        

   
# user=input("enter your word")
# result=max_2_time_every_char(user)
# print(result)
    





'find longest consecutive in list'
# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l

#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i<pivot:
#             left.append(i)

#         elif i==pivot:
#             middle.append(i)

#         else:
#             right.append(i)

#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)


# def find_longest_consecutive(l):
#     if not l:
#         return 'no longest consecutive'
#     current=1
#     longest=1
#     sorting=quick_sort_pivot(l)

#     for i in range(len(sorting)-1):

#         if sorting[i+1]==sorting[i]:
#             continue

#         elif sorting[i+1]==sorting[i]+1:
#             current=current+1
#         else:
#             if current>longest:
#                 longest=current
#             current=1

#     if current>longest:
#         longest=current

#     return f'longest consecutive {longest}'


# user=eval(input("enter your list"))
# result=find_longest_consecutive(user)
# print(result)


        
        



'''
Count State Flips (Transitions)Task: String mein character kitni baar badla (transition hua) uski total count nikalo.
Input: s = "001100110"Expected Output: 4
'''

# def count_flips(s):
#     count=0
#     for i in range(1,len(s)):
#         if s[i]!=s[i-1]:
#             count=count+1

#     return count


# user=input("enter your word")
# result=count_flips(user)
# print(result)





'''
Poori string mein sabse lamba lagaataar (consecutive) aane wala character aur uski length return karo.

Input: s = "aaabbbaaaaacc"

Expected Output: ('a', 5) (Kyunki continuous 5 baar 'a' aaya hai)

'''

# def longest_consecutive_character(s):
#     longest=1
#     current=1
#     longest_char=s[0]
#     current_char=s[0]
#     for i in range(len(s)-1):
#         if s[i+1]==s[i]:
#             current+=1
#             current_char=s[i]
#         else:
#             if current>longest:
#                 longest=current
#                 longest_char=current_char
#             current_char=s[i]
#             current=1

#     if current>longest:
#         longest=current
#         longest_char=current_char

#     return (longest_char,longest)


# user=input("enter your word")
# result=longest_consecutive_character(user)
# print(result)



