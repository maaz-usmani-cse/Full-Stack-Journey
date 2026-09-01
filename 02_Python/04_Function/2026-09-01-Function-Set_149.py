'''
1.	First Non-Repeating Element 
'''
# def find_first_non_repeating(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
    
#     for j in l:
#         if d[j]==1:
#             return f'first non repeating is {j}'

# user=eval(input("enter your list"))
# result=find_first_non_repeating(user)
# print(result)



'2.	First Repeating Element '
# def first_repeating_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             return f'first repeating element is {i}'
#         else:
#             d[i]=True
# user=eval(input("enter your list"))
# result=first_repeating_element(user)
# print(result)



'''
3.	Leaders in Array 
'''
# def leaders_element(l):
#     leaders=[]
#     max_from_right=l[-1]
#     leaders.append(max_from_right)
#     for i in range(len(l)-1,-1,-1):
#         if l[i]>max_from_right:
#             leaders.insert(0,l[i])
#             max_from_right=l[i]
#     return leaders

# user=eval(input("enter your list"))
# result=leaders_element(user)
# print(result)



'4.	Next Greater Element '
# def next_greater(l):
#     res=[-1]*len(l)
#     stack=[]
#     for i in range(len(l)-1,-1,-1):
#       while stack and stack[-1]<=l[i] :
#          stack.pop()
#       if stack:
#          res[i]=stack[-1]
#       else:
#          stack.append(l[i])
#     return res


# user=eval(input("enter your lit"))
# result=next_greater(user)
# print(result)
                