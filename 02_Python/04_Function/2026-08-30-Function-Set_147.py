'''
String mein agar do same characters bagal-bagal aate hain toh dono ko delete kar do.
Yeh process tab tak repeat karo jab tak koi pair na bache.
Input: s = "baab"Expected Output: "" (Explanation: 'aa' delete hua bacha 'bb', phir 'bb' delete hua empty)

'''
# def remove_consecutive_char(s):
#     stack=[]
#     for i in s:
#         if stack and stack[-1]==i:
#             stack.pop()

#         else:
#             stack.append(i)
#     return ''.join(stack)

# user=input("enter your word")
# result=remove_consecutive_char(user)
# print(result)




'''
Agar koi character lagaataar repeat ho raha ho, toh un dono ke beech mein '*' insert karo.

Input: s = "hello"

Expected Output: "hel*lo"
'''
# def insert_star_consecutive_word(s):
#     res=''
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             res=res+s[i]+'*'
#         else:
#             res=res+s[i]
#     res=res+s[-1]
#     return res

# user=input("enter your word")
# result=insert_star_consecutive_word(user)
# print(result)






'''
Find Longest Continuous Sequence of Same Number

Task: Integers ki list mein sabse lambe continuous identical number ka sequence aur uski length return karo.

Input: nums = [1, 2, 2, 3, 3, 3, 3, 2, 2]

Expected Output: (3, 4) (Kyunki number 3 lagaataar 4 baar aaya hai)
'''

# def find_longest_continuous_sequence(l):
#     if not l:
#         return (None,0)
#     number=l[0]
#     current_longest=1
#     longest=1
#     for i in range(len(l)-1):
#         if l[i]==l[i+1]:
#             current_longest+=1
           
#         else:
#             if current_longest>longest:
#                 longest=current_longest
#                 number=l[i]
#             current_longest=1
#     if current_longest>longest:
#         longest=current_longest
#         number=l[-1]

#     return (number,longest)

# user=eval(input("enter your list"))
# result=find_longest_continuous_sequence(user)
# print(result)




'''
Count Local Minima (Valleys)

Task: List mein kitne elements apne left aur right dono neighbors se strictly chote hain, unki count nikalo.

Input: nums = [5, 2, 7, 3, 6, 1, 8]

Expected Output: 3 (Numbers: 2, 3, 1)
'''
# def count_local_minima(l):
#     total=0
#     for i in range(1,len(l)-1):
#         if l[i]<l[i+1] and l[i]<l[i-1]:
#             total+=1
#     return total

# user=eval(input("enter your list"))
# result=count_local_minima(user)
# print(result)



