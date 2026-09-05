'''
Secret Code Checker (Symmetric check)Ek function likho is_symmetric_code(code) 
jo check kare:Code ka pehla character aur aakhri character same hona chahiye.Code kam se kam 2
 characters ka hona chahiye.Example:is_symmetric_code("radar") $\rightarrow$ True 
 (dono taraf 'r')is_symmetric_code("1001") $\rightarrow$ True (dono taraf '1')is_symmetric_code("apple")
 $\rightarrow$ False (start 'a', end 'e')

'''
# def is_valid_code(code):
#     if len(code)<2:
#         return False
#     elif code[0]!=code[-1]:
#         return False

#     return True

# code=input("enter your code")
# result=is_valid_code(code)
# print(result)



'''
Check if String is Monotonic (Non-decreasing or Non-increasing)
Task: Check karo ki kya string ke characters alphabetical order mein hamesha aage
badh rahe hain ya hamesha peeche ja rahe hain.Input 1: 
s = "abccde"  Output: True Input 2: s = "acba"  Output: False
'''

# def is_string_monotonic_or_non_monotonic(s):
#     is_increasing=True
#     is_decreasing=True
#     for i in range(len(s)-1):
#         if s[i] >s[i+1]:
#             is_increasing=False
#         if s[i]<s[i+1]:
#             is_decreasing=False

#     return is_increasing or is_increasing

    
    
# user=input("enter your word")
# result=is_string_monotonic_or_non_monotonic(user)
# print(result)


'second greatest element'
# def second_greatest_element(l):
#     first=None
#     second=None
#     for i in l:
#         if first is None or i>first:
#             second=first
#             first=i
#         elif i!=first and  (second is None or i>second ):
#             second=i
#     return f"second largest is: {second}"


# user=eval(input("eter your list"))
# result=second_greatest_element(user)
# print(result)

        


'''
Group Consecutive Booleans / Signs

Task: List mein positive aur negative numbers ke continuous groups banao.

Input: nums = [1, 2, -1, -3, 4, 5, 6, -2]

Expected Output: [[1, 2], [-1, -3], [4, 5, 6], [-2]]
'''

# def continuous_group_possitive_negative(l):
#     if not l:
#         return []
#     res=[]
#     current_group=[l[0]]
#     for i in range(len(l)-1):
#         same_sign=(l[i]>=0)==(l[i+1]>=0)
#         if same_sign:
#             current_group.append(l[i+1])
#         else:
#             res.append(current_group)
#             current_group=[l[i+1]]
#     res.append(current_group)
#     return res

# user=eval(input("enter your list"))
# result=continuous_group_possitive_negative(user)
# print(result)




'''
Agar koi character lagaataar repeat ho raha ho, toh un dono ke beech mein '*' insert karo.

Input: s = "hello"

Expected Output: "hel*lo"
'''

# def replace_stra_with_consecutive_char(s):
#     res=''
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             res=res+s[i]+'*'
#         else:
#             res=res+s[i]
#     res=res+s[-1]
#     return res

# user=input("enter your character")
# result=replace_stra_with_consecutive_char(user)
# print(result)




'''
Expand Encoded Pattern with Multipliers

Task: Pattern string jahan bracket ke bahar count ho use expand karo.

Input: s = "3[a]2[bc]"

Expected Output: "aaabcbc"
'''


        
        


