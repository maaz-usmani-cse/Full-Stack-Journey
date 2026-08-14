'program for fibonacci series'

# def fibbonacci_series(n):
#     n1=0
#     n2=1
#     for i in range(n):
#         print(n1,end=' ')
#         add=n1+n2
#         n1=n2
#         n2=add


# user=int(input("enter your number"))
# fibbonacci_series(user)




'''
Move All Zeros to End
Task: List me se saare 0 ko end mein shift karo, baaki numbers ka order same rehna chahiye.

Input: nums = [0, 1, 0, 3, 12]

Expected Output: [1, 3, 12, 0, 0]
'''


# def shift_zero_end(l):
#     position=0
#     for i in range(len(l)):
#         if l[i] !=0:
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp
#             position=position+1
#     return l

# user=eval(input("enter your list"))
# result=shift_zero_end(user)
# print(result)




'''
 Check karo ki kya string mein koi bhi do adjacent (consecutive) characters same nahi hain.
 Input: s = "abababa" $\rightarrow$ Output: True
 Input: s = "abaabba" $\rightarrow$ Output: False (Kyunki 'bb' continuous aagaya)
'''
# def is_adjacent_char_same(s):
#     for i in range(1,len(s)):
#         if s[i]==s[i-1]:
#             return False
#     return True

# user=input("enter your word")
# result=is_adjacent_char_same(user)
# print(result)






'''
Longest Strictly Increasing Sub-array
Task: Continuous strictly increasing numbers ki sabse badi length nikalo.

Input: nums = [1, 2, 3, 1, 2, 3, 4, 2]

Expected Output: 4 (Kyunki [1, 2, 3, 4] length 4 ka hai)
'''
# def longest_increasing_subarray(l):
#     longest=1
#     current=1
#     for i in range(len(l)-1):
#         if l[i+1]>l[i]:
#             current=current+1
#         else:
#             if current>longest:
#                 longest=current
#             current=1

#     if current>longest:
#         longest=current
#     return f'longest subarray is: {longest}'


# user=eval(input("enter your list"))
# result=longest_increasing_subarray(user)
# print(result)





'''
Consecutive characters ko compress karo, lekin agar count 1 ho toh number mat lagao.

Input: s = "aabcccccaaa"

Expected Output: "a2bc5a3" (Notice: 'b' ke aage 1 nahi laga)
'''

# def compress_consecutive_char(s):
#     res=''
#     count=1
#     for i in range(1,len(s)):
#         if s[i]==s[i-1]:
#             count=count+1

#         else:
#             res=res+s[i-1]
#             if count>1:
#                 res=res+str(count)
#             count=1
#     res=res+s[-1]
#     if count>1:
#       res=res+str(count)

#     return res

# user=input("enter your word")
# result=compress_consecutive_char(user)
# print(result)



