'''
Dictionary Inversion with Values as Length of Keys

Task: Dict keys ko value banao, lekin nayi values purani keys ki length honi chahiye.

Input: {"django": 101, "python": 102}

Expected Output: {101: 6, 102: 6}

'''

# def swap_key_length_valus(d):
#     res={}
#     for i in d:
#         res[d[i]]=len(i)
#     return res


# user=eval(input("enter your dict"))
# result=swap_key_length_valus(user)
# print(result)








'''
Sum of Digits as Dictionary Values

Task: Numbers list se key = number, aur value = us number ke saare digits ka sum (jod).

Input: [123, 45, 99]

Expected Output: {123: 6, 45: 9, 99: 18}

'''

# def sum_of_digits_as_dict_values(l):
#     res={}
#     for i in l:
#         total=0
#         for j in str(i):
#             total=total+int(j)
#         res[i]=total

#     return res



# user=eval(input("enter your list"))
# result=sum_of_digits_as_dict_values(user)
# print(result)









'''
Find triplet whose sum equals target 

'''

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









# def find_tripplet_sum_target(l,target):
#     res=quick_sort_pivot(l)
#     for i in range(len(res)-2):
#         left=i+1
#         right=len(res)-1

#         while left<right:
#             current_sum=res[i] + res[left] + res[right]
#             if current_sum==target:
#               return res[i],res[left],res[right]

#             if current_sum>target:
#                 right=right-1

#             else:
#                 left=left+1



# user=eval(input("enter your list"))
# target=eval(input("enter your target"))
# result=find_tripplet_sum_target(user,target)
# print(result)











'pata kro list assending order m sortedhai ya nahi'

# def is_list_sorted(l):
#      for i in range(len(l)-1):
#           if l[i]>l[i+1]:
#                return False
#           return True


# user=eval(input("enter your list"))
# result=is_list_sorted(user)
# print(result)