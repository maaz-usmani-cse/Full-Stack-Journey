'Find longest consecutive sequence in array -----------'
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




# def longest_consecutive_sequence(l):
#     sorting=quick_sort_pivot(l)
#     current=1
#     longest=1
#     for i in range(len(sorting)-1):
#         if sorting[i+1]==l[i]:
#             continue

#         if sorting[i+1]==sorting[i]+1:
#             current=current+1
#         else:
#             if current>longest:
#                 longest=current
#             current=1

#     if current>longest:
#         longest=current

#     return longest


# user=eval(input("enter your lisy"))
# result=longest_consecutive_sequence(user)
# print(result)





'First Non-Repeating Element '

# def firs_non_repeating_element(l):
#     if not l:
#         return None
    
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in d:
#         if d[j]==1:
#             return f'non repeting element: {j}'


# user=eval(input("enter your list"))
# result=firs_non_repeating_element(user)
# print(result)





'2.	First Repeating Element '

# def first_repeating_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             return f'first repeating element: {i}'
#         else:
#             d[i]=True


# user=eval(input("enter your list"))
# result=first_repeating_element(user)
# print(result)





'Leaders in Array '

# def find_leaders_element(l):
#     maximum=l[-1]
#     leaders=[maximum]
#     for i in range(len(l)-1,-1,-1):
#         if l[i]>maximum:
#             maximum=l[i]
#             leaders.insert(0,maximum)
#     return leaders

# user=eval(input("enter your list"))
# result=find_leaders_element(user)
# print(result)









