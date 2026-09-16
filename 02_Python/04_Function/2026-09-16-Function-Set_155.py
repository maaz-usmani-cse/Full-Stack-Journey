'''
String ko consecutive count format (jaise "a3b2") mein compress karo, 
lekin compressed string tabhi return karo agar uski length original string se choti ho. 
Agar choti na ho, toh original string hi return karo.Input 1: s = "aabcccccaaa" 
Output: "a2b1c5a3" (Compressed choti hai)Input 2: s = "abc"  Output: "abc" (Kyunki compressed "a1b1c1" lambi hai)
'''

# def compress_consecutive_count(s):
#     res=''
#     total=1
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             total=total+1
#         else:
#             res=res+s[i]+str(total)
#             total=1

#     res=res+s[-1]+str(total)

#     if len(res)<len(s):
#         return res

#     return s

# user=input("enter your word")
# result=compress_consecutive_count(user)
# print(result)



'''
Remove All Consecutive Pairs (String Reducer)
Task: String mein agar do same characters bagal-bagal aate hain toh dono ko delete kar do.
 Yeh process tab tak repeat karo jab tak koi pair na bache.
 Input: s = "baab"Expected Output: "" (Explanation: 'aa' delete hua 
 bacha 'bb', phir 'bb' delete hua 
'''

# def remove_all_consecutive_pair(s):
#     stack=[]
#     for i in s:
#         if stack and i==stack[-1]:
#             stack.pop()
#         else:
#             stack.append(i)
#     return ''.join(stack)

# user=input("enter your woord")
# result=remove_all_consecutive_pair(user)
# print(result)
    
    

'''
Separate Duplicate Adjacent Characters with a Star

Task: Agar koi character lagaataar repeat ho raha ho, toh un dono ke beech mein '*' insert karo.

Input: s = "hello"

Expected Output: "hel*lo"
'''

# def dublicate_consecutive_char_with_star(s):
#     res=''
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             res=res+s[i]+'*'
#         else:
#             res=res+s[i]
#     res=res+s[-1]

#     return res

# user=input("enter your word")
# result=dublicate_consecutive_char_with_star(user)
# print(result)




'''
Find Longest Continuous Sequence of Same Number

Task: Integers ki list mein sabse lambe continuous identical number ka sequence aur uski length return karo.

Input: nums = [1, 2, 2, 3, 3, 3, 3, 2, 2]

Expected Output: (3, 4) (Kyunki number 3 lagaataar 4 baar aaya hai)
'''
# def find_continuous_sequence_of_same_number(l):
#    longest=1
#    current_element=0
#    current_num=1
#    for i in range(len(l)-1):
#       if l[i]==l[i+1]:
#         current_num+=1

#       else:
#          if current_num>longest:
#             longest=current_num
#             current_element=l[i]
      
#          current_num=1

#    if current_num>longest:
#       longest=current_num
#       current_element=l[-1]

#    return current_element,longest

# user=eval(input("enter your list"))
# result=find_continuous_sequence_of_same_number(user)
# print(result)




'''Count Local Minima (Valleys)

Task: List mein kitne elements apne left aur right dono neighbors se strictly chote hain, unki count nikalo.

Input: nums = [5, 2, 7, 3, 6, 1, 8]

Expected Output: 3 (Numbers: 2, 3, 1)
'''
# def find_local_minima(l):
#     total=0
#     for i in range(1,len(l)-1):
#         if l[i]<l[i-1]and l[i]<l[i+1]:
#             total+=1
#     return total

# user=eval(input("enter your list"))
# result=find_local_minima(user)
# print(result)





'''
Check if String is Monotonic (Non-decreasing or Non-increasing)
Task: Check karo ki kya string ke characters alphabetical order mein hamesha aage badh rahe hain ya hamesha peeche ja rahe hain.
Input 1: s = "abccde"Output: True Input 2: s = "acba"  Output: False

'''

# def is_monotonic_or_not(s):
#     is_increasing=True
#     is_decreasing=True
#     for i in range(len(s)-1):
#         if s[i]>s[i+1]:
#             is_increasing=False
#         if s[i]<s[i+1]:
#             is_decreasing=False

#     return is_decreasing or is_increasing

# user=input("enter your word")
# result=is_monotonic_or_not(user)
# print(result)



         




