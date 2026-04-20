## i have already solve this questons(longest sequence) in my previous Set but one more time i am doing practice

'longest sequence'
# def longest_sequence(n):
#     l=[1]*len(n)
#     for i in range(1,len(n)):
#         for j in range(0,i):
#             if n[i]>n[j]:
#                 if l[i]<l[j]+1:
#                     l[i]=l[j]+1
#     maximum=None
#     for i in l:
#         if maximum is None or i>maximum:
#             maximum=i

#     return maximum

# user=eval(input("enter your list"))
# result=longest_sequence(user)
# print(result)








'do list m jo common nahi h wo nikalo '
# def symmentric_diffrence(l1,l2):
#     l=[]
#     for i in l1:
#         if i not in l2 and i not in l:
#             l.append(i)
#     for j in l2:
#         if j not in l1 and j not in l:
#             l.append(j)
#     return l

# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=symmentric_diffrence(l1,l2)
# print(result)









'find subset of twolist'
# def subset(l1,l2):
#     l=[]
#     for i in l1:
#         if i not in l2 and i not in l:
#             l.append(i)
   
#     return l

# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=subset(l1,l2)
# print(result)









'check kro kya list1 list 2 k subset h ki nahi '
# def check_subsets(l1,l2):
#     for i in l2:
#         if i not in l1:
#             return False
#     else:
#         return True
    
# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=check_subsets(l1,l2)
# print(result)










'Replace element with next greater element '
# def next_greater_element(n):
#     l=[-1]*len(n)
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[j]>n[i]:
#                 l[i]=n[j]
#                 break
#     return l

# user=eval(input("enter your list"))
# result=next_greater_element(user)
# print(result)





'Replace element with previous smaller element '
# def previous_smallest(n):
#     l=[-1]*len(n)
#     for i in range(len(n)):
#         for j in range(i-1,-1,-1):
#             if n[j]<n[i]:
#                 l[i]=n[j]
#                 break
#     return l


# user=eval(input("enter your list"))
# result=previous_smallest(user)
# print(result)






