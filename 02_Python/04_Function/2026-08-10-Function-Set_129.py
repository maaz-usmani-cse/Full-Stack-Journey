'''
 Equilibrium Index (Pivot Index)Task: Ek aisa index i dhoondho jiske left side ke sabhi numbers ka sum aur right side ke sabhi 
 numbers ka sum barabar ho.Example: [-7, 1, 5, 2, -4, 3, 0]Index 3
(value 2) ke left ka sum: $-7 + 1 + 5 = -1$Index 3 ke right ka sum: $-4 + 3 + 0 = -1$Output Index: 3

'''

# def iquilibrium_index(l):
#    total=0
#    for i in l:
#       total=total+i

#    left_sum=0
#    for j in range(len(l)):
#       right_sum=total-left_sum-l[j]

#       if left_sum==right_sum:
#          return f'iquilibrium-index: {j}'

#       left_sum=left_sum+l[j]

#    return -1


# user=eval(input("enter your list"))
# result=iquilibrium_index(user)
# print(result)    
      





'.Next Greater Element '

# def next_greater_element(l):
#     res=[-1]*len(l)
#     stack=[]
#     for i in range(len(l)-1,-1,-1):

#         while stack and stack[-1]<=l[i]:
#             stack.pop()

#         if stack:
#             res[i]=stack[-1]

#         stack.append(l[i])

#     return res


# user=eval(input("enter your list"))
# result=next_greater_element(user)
# print(result)




'	Majority Element '

# def find_majority_element(l):
#    satisfy_condition=len(l)/2
#    d={}
#    for i in l:
#       if i in d:
#          d[i]=d[i]+1

#       else:
#          d[i]=1

#    for j in d:
#       if d[j]>satisfy_condition:
#          return f'majority element is: {j}'


# user=eval(input('enter your list'))
# result=find_majority_element(user)
# print(result)
    





'Missing Number '

# def find_missing_number(l):
#     d={}
#     for i in l:
#         d[i]=True


#     for i in range(1,len(l)+1):
#         if i not in d:
#             return f'missing number is {i}'



# user=eval(input("enter your list"))
# result=find_missing_number(user)
# print(result)






'Duplicate Number '

# def is_dublicate_number(l):
#     dublicate=[]
#     d={}
#     for i in l:
#         if i in d:
#             if i not in dublicate:
#                dublicate.append(i)

#         else:
#             d[i]=True

#     return dublicate


# user=eval(input("enter your list"))
# result=is_dublicate_number(user)
# print(result)





'Pair Sum Closest to Target '
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


# def closet_sum_pair(li,target):
#     l=quick_sort_pivot(li)
#     left=0
#     right=len(l)-1
#     min_diff=float('inf')
#     best_pair=(None,None)

#     while left<right:
#         curremt_sum=l[left] + l[right]
#         diff=abs(target-curremt_sum)

#         if diff<min_diff:
#             min_diff=diff
#             best_pair=(l[left],l[right])

#         if curremt_sum>target:
#             right=right-1

#         else:
#             left=left+1

#     return best_pair


# user=eval(input("enter your list"))
# target=int(input("enter your target number"))
# result=closet_sum_pair(user,target)
# print(result)







'Longest Increasing Subarray '
# def longest_increasing_subarray(l):
#     current=1
#     longest=1
#     for i in range(len(l)-1):
#         if l[i+1]>l[i]:
#             current=current+1
#         else:
#             if current>longest:
#                 longest=current
#             current=1

#     if current>longest:
#         longest=current

#     return longest


# user=eval(input("enter your list"))
# result=longest_increasing_subarray(user)
# print(result)


    


'''
#	Two Sum 

wo Sum problem ka matlab hota hai: Ek list/array me se aise 2 numbers dhoondhna 
jinhe aapas me add (plus) karne par diya gaya target ban jaye.


'''

def two_sum(l,target):
    d={}
    for i in l:
        required=target-i
        if required in d:
            return f'two sum is {d[required],i}'

        else:
            d[i]=i

user=eval(input("enter your list"))
target=int(input("enter your target"))
result=two_sum(user,target)
print(result)


    


