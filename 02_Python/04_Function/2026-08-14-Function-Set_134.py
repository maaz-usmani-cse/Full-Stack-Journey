'''
Given a list of strings, group the anagrams together using a dictionary. Order of groups does not matter.
Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
'''
# def quick_sort_pivot(s):
#     if len(s)<=1:
#         return s
#     pivot=s[0]
#     left=''
#     middle=''
#     right=''
#     for i in s:
#         if i<pivot:
#             left+=i

#         elif i==pivot:
#            middle+=i

#         else:
#             right+=i
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)



# def group_anagram(s):
#     d={}
#     for i in s:
#         sorted=quick_sort_pivot(i)
#         if sorted not in d:
#             d[sorted]=[]
#         d[sorted].append(i)

#     res=[]
#     for i in d.values():
#         res.append(i)
#     return res



# user=eval(input("enter your list"))
# result=group_anagram(user)
# print(result)





'''

Longest Subarray with Sum Equals K (Difficulty: Medium-Hard)

Given an array of integers nums (positive, negative, aur zero ho sakte hain) aur ek integer k, find karo longest subarray ki length jiska sum strictly k ke barabar ho.

Input: nums = [1, -1, 5, -2, 3], k = 3

Output: 4 (Subarray [1, -1, 5, -2] ka sum 3 hai aur length 4 hai).

'''


# def max_sub_array_len(nums, k):
#     prefix_sum = 0
#     max_len = 0
   
#     sum_map = {}

#     for i, num in enumerate(nums):
#         prefix_sum += num

       
#         if prefix_sum == k:
#             max_len = i + 1

       
#         rem = prefix_sum - k
#         if rem in sum_map:
#             sub_len = i - sum_map[rem]
#             max_len = max(max_len, sub_len)

     
#         if prefix_sum not in sum_map:
#             sum_map[prefix_sum] = i

#     return max_len


# nums = [1, -1, 5, -2, 3]
# k = 3
# print("Longest Subarray Length:", max_sub_array_len(nums, k))
