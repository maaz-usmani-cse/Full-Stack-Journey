'.	Count unique elements '
# def unique_element(l):
#     unique_list=[]
#     count=0
#     for i in l:
#         if i not in unique_list:
#             unique_list.append(i)
#             count=count+1
#     return count

# user=eval(input("enter your list"))
# result=unique_element(user)
# print(result)





'Replace duplicates with 0 '
# def replace_dublicate(n):
#     l=[]
#     for i in n:
#         if i not in l:
#             l.append(i)
#         else:
#             l.append(0)
#     return l


# user=eval(input("enter your list"))
# result=replace_dublicate(user)
# print(result)










'Find first non-repeating element '
# def find_first_non_repeating(n):
#     for i in n:
#         count=0
#         for j in n:
#             if i==j:
#                 count=count+1
#         if count==1:
#             return f'first non repeating is: {i}'
#     return 'koi v unique nahi hai bhai'


# user=eval(input('enter your list'))
# result=find_first_non_repeating(user)
# print(result)





'Find second most frequent element '
# def second_most_frequent_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     first_frequent=None
#     second_frequent=None
#     first_elemnt=None
#     second_element=None
#     for i in d:
#         if first_frequent is None or d[i]>first_frequent:
#             second_frequent=first_frequent
#             second_element=first_elemnt
#             first_frequent=d[i]
#             first_elemnt=i

#         elif d[i]!=first_frequent and (second_frequent is None or d[i]>second_frequent):
#             second_frequent=d[i]
#             second_element=i
#     return f'first most frequment elemnt{first_elemnt},  second most frequent element:{second_element}'



# user=eval(input("enter your list"))
# result=second_most_frequent_element(user)
# print(result)            





'Reverse a list '
# def reverse_list(l):
#     for i in range(len(l)-1,-1,-1):
#         print(l[i])


# user=eval(input("enter your list"))
# result=reverse_list(user)
# print(result)





'Rotate list left by 1 '
# def rotate_list(l):
#     temp= l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]  
#     l[-1]=temp
#     return l

# user=eval(input("enter your list"))
# result=rotate_list(user)
# print(result)






'Rotate list by k positions '

# def rotate_list_k_position(l,k_time,position):
#     for i in range(len(k_time)):
#         if position=='right':
#             for j in range(len(l)-1,0,-1):
#                 temp=l[-1]
#                 l[j]=l[j-1]
#             l[0]=temp
#         elif position=='left':
#             for k in range(len(l)-1):
#                 temp=l[0]
#                 l[k]=l[k+1]
#             l[-1]=temp

#     return l
# l=eval(input("enter your list"))
# k_time=int(input("enter your number"))
# position=input("enter your position")
# result=rotate_list_k_position(l,k_time,position)




'Move all zeros to end '
# def move_zero_end(l):
#     zero=[]
#     non_zero=[]
#     for i in l:
#        if i==0:
#            zero.append(i)
#        else:
#            non_zero.append(i)
#     result=non_zero+zero
#     return result

# user=eval(input("enter your list"))
# result=move_zero_end(user)
# print(result)           




