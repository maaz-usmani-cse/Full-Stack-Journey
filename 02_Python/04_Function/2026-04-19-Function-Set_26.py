'.Move all zeros to end '
# def shift_zero_end(n):
#     l=[]
#     for i in n:
#         if i==0:
#             l.append(0)
#         else:
#             l.insert(0,i)
#     return l

# user=eval(input("enter your list"))
# result=shift_zero_end(user)
# print(result)








'.Separate even and odd numbers '
# def separate_even_odd(n):
#     even=[]
#     odd=[]
#     for i in n:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return 'even :',even,'odd :',odd

# user=eval(input("enter your list"))
# result=separate_even_odd(user)
# print(result)






'Sort list (without using sort) '
# def sort_list(n,required):
#     if required=='assending':
#         for i in range(len(n)-1):
#             for j in range(i+1,len(n)):
#                 if n[i]>n[j]:
#                     temp=n[i]
#                     n[i]=n[j]
#                     n[j]=temp
#         return n
#     elif required=='dessending':
#         for i in range(len(n)-1):
#             for j in range(i+1,len(n)):
#                 if n[i]<n[j]:
#                     temp=n[i]
#                     n[i]=n[j]
#                     n[j]=temp
#         return n

# list=eval(input("enter your list"))
# user_required=input("what do you want? assending/dessending")
# result=sort_list(list,user_required)
# print(result)









'Merge two lists '
# def merge_twolist(l1,l2):
#     add=l1+l2
#     return add


# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=merge_twolist(l1,l2)
# print(result)









'Check if list is palindrome '
# def list_palindrom(n):
#     rev=[]
#     for i in n:
#         rev.insert(0,i)
#     if n==rev:
#         return 'pollindrom hai'
#     else:
#         return 'pollindrom nahi hai'    



# user=eval(input("enter your list"))
# result=list_palindrom(user)
# print(result)










'Find pair with given sum '
# def find_pai(n,target):
#     l=[]
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[i]+n[j]==target:
#                 l.append((n[i],n[j]))
#     return l

# user=eval(input("entr your list"))
# target=int(input('enter your trget'))
# result=find_pai(user,target)
# print(result)





    
             
    



'Find maximum difference between elements '
# def maximum_diffrence(n):
#     maximum=None
#     minimum=None
#     for i in n:
#         if maximum is None or i>maximum:
#             maximum=i
#         if minimum is None or i<minimum:
#            minimum=i
#     difference=maximum-minimum
#     return difference

# user=eval(input('enter your list'))
# result=maximum_diffrence(user)
# print(result)    










'Find minimum difference '
# def find_minimum(n):
#     first=None
#     second=None
#     for i in n:
#         if first is None or i>first:
#             second=first
#             first=i

#         elif i!=first and (second is None or i>second):
#             second=i
#     minimum_diifrence=first-second
#     return minimum_diifrence

# user=eval(input("enter your list"))
# result=find_minimum(user)
# print(result)





'Find longest increasing sequence '
# def longest_sequence(n):
#     length = len(n)
#     L = [1] * length    
#     for i in range(1, length):
#         for j in range(0, i):
#             if n[i] > n[j]:
#                 if L[i] < L[j] + 1:
#                     L[i] = L[j] + 1
#     max_ans = 0
#     for x in L:
#         if x > max_ans:
#             max_ans = x
            
#     return max_ans

# user_list = [10, 20, 5, 30, 8, 40]
# print(longest_sequence(user_list))






'Find longest decreasing sequence '
# def find_longest_decreasing_sequence(n):
#     l=[1]*len(n)
#     for i in range(1,len(n)):
#         for j in range(0,i):
#             if n[i]<n[j]:
#                 if l[i]>l[j]+1:
#                     l[i]=l[j]+1
#     smallest=None
#     for i in l:
#         if smallest is None or i>smallest:
#             smallest=i
#     return smallest


# user=eval(input("enter your list"))
# result=find_longest_decreasing_sequence(user)
# print(result)