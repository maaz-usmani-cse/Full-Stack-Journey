'''
Sabse lambi aisi continuous substring ki length nikalo jisme koi bhi do adjacent characters same na hon.
Input: s = "aabbcdeffg"
Expected Output: 4
'''

# def continuous_substring_Length(s):
#     longest=0
#     current=0
#     for i in range(1,len(s)):
#         if s[i] != s[i-1]:
#             current=current+1
#         else:
#             if current>longest:
#                 longes=current
#             current=0

#     return f"sabse lamba length {longes} hai"


# user=input("enter your word")
# res=continuous_substring_Length(user)
# print(res)



'''
Split List on Decrease (Strictly Increasing Sublists)

Task: List ko wahan se todte jao jahan number apne pichhle number se chhota ho jaye (har tukda strictly increasing hona chahiye).

Input: nums = [1, 2, 4, 2, 3, 5, 1, 2]

Expected Output: [[1, 2, 4], [2, 3, 5], [1, 2]]
'''

# def split_liest_on_decrease(l):
#     if not l:
#          return []
#     res=[]
#     current=[l[0]]
#     for i in range(1,len(l)):
#         if l[i]>l[i-1]:
#             current.append(l[i])
#         else:
#             res.append(current)
#             current=[l[i]]
#     res.append(current)
#     return res

# user=eval(input("enter your list"))
# result=split_liest_on_decrease(user)
# print(result)



'''
Replace Even Runs with Single Even Mark

Task: Agar continuous even numbers ka run mile, toh use unke count aur 'E' se replace karo.

Input: nums = [1, 2, 4, 6, 7, 8, 10, 3]

Expected Output: [1, '3E', 7, '2E', 3]
'''
# def replace_continous_even_with_his_count(l):
#     res=[]
#     current_count=0
#     for i in range(len(l)):
#         if l[i]%2==0:
#             current_count=current_count+1
#         else:
#           if current_count>0:
#               res.append(f"{current_count}E")
#               current_count=0    
#           res.append(l[i]) 
#     if current_count>0:
#         res.append(f"{current_count}E")

#     return res

# user=eval(input("enter your list"))
# result=replace_continous_even_with_his_count(user)
# print(result)
            


'''
Check karo ki kya string mein 0 aur 1 barabar alternate kar rahe hain 
(jaise "0101" ya "1010").Input 1: s = "010101"
Output: True
Input 2: s = "010010" 
Output: False (Kyunki '00' aagaya)

'''
# def alternate_equal_0_1(s):
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             return False
#     return True

# user=input("enter your word")
# result=alternate_equal_0_1(user)
# print(result)



