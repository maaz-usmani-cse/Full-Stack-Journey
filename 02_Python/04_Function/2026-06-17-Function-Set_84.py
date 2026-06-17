'''
Find pair with given sum 

'''
# def find_pair(l,k):
#     d={}
#     for i in l:
#         required=k-i
#         if required in d:
#             return f'pair is {required,i}'
#         d[i]=True

# user=eval(input("enter your list"))
# target=int(input("enter your target number"))
# result=find_pair(user,target)
# print(result)







'Find all pairs with sum = k '
# def find_all_pair(l,k):
#     d={}
#     res=[]
#     for i in l:
#         required=k-i
#         if required in d:
#             res.append((required,i))
#             del d[required]
#         d[i]=True
#     return res


# user=eval(input("enter your list"))
# target=int(input("enter your target number"))
# result=find_all_pair(user,target)
# print(result)






'''
Find maximum difference between elements 
'''
# def find_maximum_diffrence(l):
#     smallest=None
#     largest=None
#     for i in l:
#         if smallest is None or i<smallest:
#             smallest=i
#         if largest is None or i>largest:
#             largest=i
#     difference=largest-smallest
#     return difference








'Find longest increasing sequence '
# def find_longest_sequence(l):
#     longest=1
#     current=1
#     for i in range(len(l)-1):
#         if l[i+1]>l[i]:
#             current=current+1
#         else:
#             if current>longest:
#                 longest=current
#             current=1
#     if current>longest:
#         longest=current
    
#     return f'longest increasinfg sequence hai {longest}'


# user=eval(input("enter your list"))
# result=find_longest_sequence(user)
# print(result)






'''Replace element with next greater element '''
# def replace_next_greater(l):
#    res=[-1]*len(l)
#    for i in range(len(l)-2,-1,-1):
#       if l[i+1]>l[i]:
#          res[i]=l[i+1]
#       elif res[i+1]>l[i]:
#          res[i]=res[i+1]
#    return res
         
      
      
# user=eval(input("enter your list"))
# result=replace_next_greater(user)
# print(result)







        