'.	Replace digits equal to sum of neighbors with 7.'

# def Replace_digits_equal_to_sum_of_neighbors(n):
#   l=n[:]
#   for i in range(1,len(n)-1):
#     left_neighbors=n[i-1]
#     right_neighbors=n[i+1]
#     total=left_neighbors+right_neighbors
#     if total==n[i]:
#       l[i]=7
#   return l


# user=eval(input("enter your list"))
# result=Replace_digits_equal_to_sum_of_neighbors(user)
# print(result)








'Replace digits equal to sum of neighbors with 7.  userinput like- 1213524'

# def replace_with_neghbours(n):
#     s=str(n)
#     l=[int(s[0])]
#     for i in range(1,len(s)-1):
#         left=int(s[i-1])
#         right=int(s[i+1])
#         if left+right==int(s[i]):
#             l.append(7)
#         else:
#             l.append(int(s[i]))
#     if len(l)>1:
#         l.append(int(s[-1]))

    
#     return l

# user=int(input("enter your number"))
# result=replace_with_neghbours(user)
# print(*result,sep='')








'	Replace digits equal to product of neighbors with 9.'
# def Replace_digits_equal_to_product_of_neighbors(n):
#     s=str(n)
#     l=[int(s[0])]
#     for i in range(1,len(s)-1):
#         left=s[i-1]
#         right=s[i+1]
#         if int(left)*int(right)==int(s[i]):
#             l.append(9)
#         else:
#             l.append(int(s[i]))
#     if len(s)>1:
#         l.append(int(s[-1]))
#     return l



# user=int(input("enter your number"))
# result=Replace_digits_equal_to_product_of_neighbors(user)
# print(*result,sep='')







'.	Replace digits whose square > 50 with 5.'
# def replace_whose_square_greater50(n):
#     l=[]
#     for i in n:
#         if int(i)**2>50:
#             l.append(5)
#         else:
#             l.append(int(i))
#     return l

# user=input("enter your number")
# result=replace_whose_square_greater50(user)
# print(*result,sep='')









'.	Replace digits whose cube > 200 with 3.'
# def replace_digit_whose_cube_greater200(n):
#     l=[]
#     for i in n:
#         if int(i)**3>200:
#             l.append(3)
#         else:
#             l.append(int(i))
#     return l


# user=input("enter your number")
# result=replace_digit_whose_cube_greater200(user)
# print(*result,end=' ')



