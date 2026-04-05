'Implement a program to find the frequency of each element in an list.'

# def frequency_count_list(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# user=eval(input("enter your list"))
# result=frequency_count_list(user)
# print(result)







'implement a program to count positive and negative numbers in list'
# def check_positive_negative_in_list(n):
#     possitive=0
#     negative=0
#     for i in n:
#         if i>0:
#             possitive=possitive+1
#         else:
#             negative=negative+1
#     return "possitive:" , possitive, "negative:", negative


# user=eval(input("enter your list"))
# result=check_positive_negative_in_list(user)
# print(result)






'Implement a program to sort a list in ascending order'
# def sort_assending_list(n):
#     
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[i]>n[j]:
#                 temp=n[i]
#                 n[i]=n[j]
#                 n[j]=temp
#     return n

# user=eval(input('entyer your list'))
# result=sort_assending_list(user)
# print(result)









'Implement a program to sort a list in decending order.'
# def sort_desending_order(n):
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[i]<n[j]:
#                 temp=n[i]
#                 n[i]=n[j]
#                 n[j]=temp
#     return n

# user=eval(input("enter your list"))
# result=sort_desending_order(user)
# print(result)









' Check if a list is sorted in ascending order.'
# def check_list_is_sorted(n):
#     for i in range(len(n)-1):
#         if n[i]>n[i+1]:
#             return False 
#     return True


# user=eval(input("enter your list"))
# result=check_list_is_sorted(user)
# print(result)










' Check if a list is sorted in  descending order.'

# def check_lis_is_assending(n):
#     for i in range(len(n)-1):
#         if n[i]<n[i+1]:
#             return False
#     return True

# user=eval(input("enter your list"))
# result=check_lis_is_assending(user)
# print(result)