
'a se z tak right angle triangle print kro'
# def a_z_rightangle(n):
#     x=ord('A')
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             if x<=90:
#                 print(chr(x),end=' ')
#                 x=x+1
#         print()

# user=int(input("enter your number"))
# a_z_rightangle(user)




'list me maximum number and minimum number find out kro'
# def maximimum_minimum_find(n):
#     maximum=None
#     minimum=None
#     for i in n:
#          if maximum is None or i>maximum:
#               maximum=i
#          if minimum is None or i <minimum:
#               minimum=i
#     return 'maximum:',maximum ,"minimum:", minimum

# user=eval(input("enter your list"))
# result=maximimum_minimum_find(user)
# print(result)




'swapping from first lo last'
# def swapping(n):
#     first=n[0]
#     last=n[-1]
#     middle=''
#     res=''
#     for i in range(1,len(n)-1):
#         middle=middle+n[i]
#     res=res+last+middle+first
#     return res

# user=input("enter your word")
# result=swapping(user)
# print(result)    





'mplement a program to find the frequency of each element in list'
# def frequency_count(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# user=eval(input("enter your list "))
# result=frequency_count(user)
# print(result)



'Check if a list is sorted in ascending order'
# def chech_list(n):
#     for i in range(len(n)-1):
#         if n[i]>n[i+1]:
#             return False
    
#     return True
    
# user=eval(input("enter your list"))
# result=chech_list(user)
# print(result)
        




'Check if a list is sorted in ascending order'
# def check_list_desending_order(n):
#     for i in range(len(n)-1):
#         if n[i]<n[i+1]:
#             return False
#     return True
    
# user=eval(input("enter your list"))
# result=check_list_desending_order(user)
# print(result)




'. Write a program to find the intersection of two list'

# def find_intersection_list_element(l1,l2):
#     l=[]
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 if i not in l:
#                     l.append(i)
#     return l

# user1=eval(input("enter your list"))
# user2=eval(input("enter your list"))
# result=find_intersection_list_element(user1,user2)
# print(result)




