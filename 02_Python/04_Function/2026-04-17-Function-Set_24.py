'rotate the list accordinfg to user required'


# def rotate_list(list,steps,direction):
#     direction=direction.lower()
#     for i in range(steps):
#         if direction=='left':
#            temp_left=list[0]
#            for j in range(len(list)-1):
#               list[j]=list[j+1]
#            list[-1]=temp_left
#         elif direction=='right':
#             temp_right=list[-1]
#             for k in range(len(list)-1,0,-1):
#                 list[k]=list[k-1]
#             list[0]=temp_right
#     return list



# list=eval(input("enter your list"))
# steps=int(input("enter your number"))
# direction=input("enter your direction")
# result=rotate_list(list,steps,direction)
# print(result)
        












'Write a program to find the missing numberin a series'
# def find_missing_value(n):
#     if not n:
#         return 'list empty'
#     if n[0]!=1:
#         return 1,'missisng hai'
#     for i in range(1,len(n)):
#         if n[i]!=n[i-1]+1:
#             return 'ye missing hai',n[i-1]+1
#     return 'ye missing hai',n[-1]+1


# user=eval(input("enter your list"))
# result=find_missing_value(user)
# print(result)
    












'Implement a program to count positive and negative numbers in a list'
# def count_possitive_negative(n):
#     positive=0
#     negative=0
#     for i in n:
#         if i>0:
#             positive=positive+1
#         else:
#             negative=negative+1
#     return 'possitibr',positive,'negative',negative


# user=eval(input("enter your list"))
# result=count_possitive_negative(user)
# print(result)















'Write a program to check if two lists are equal.'
# def check_list_equal(l1,l2):
#     if len(l1)!=len(l2):
#         return False
#     for i in range(len(l1)):
#         if l1[i]!=l2[i]:
#             return False
        
#     return True

# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=check_list_equal(l1,l2)
# print(result)








'Keep only numbers divisible by 3'
# def find_n_only_divide_by_3(n):
#     l=[]
#     for i in n:
#         if i%3==0:
#             l.append(i)
#     return l


# user=eval(input("enter your list"))
# result=find_n_only_divide_by_3(user) 
# print(result)       







'Remove numbers divisible by 5 '
# def remove_n_divisible_by_5(n):
#     l=[]
#     for i in n:
#         if i%5!=0:
#             l.append(i)
#     return l

# user=eval(input("enter your list"))
# result=remove_n_divisible_by_5(user)
# print(result)






'Replace negative numbers with 0 '
# def replace_position_with_negative(n):
#     l=[]
#     for i in n:
#         if i<0:
#             l.append(0)
#         else:
#             l.append(i)
#     return l

# user=eval(input("enter ypir list"))
# result=replace_position_with_negative(user)
# print(result)









'.Replace each element with its square '
# def each_position_with_square(n):
#     l=[]
#     for i in n:
#         l.append(i**2)
#     return l

# user=eval(input("entr your list"))
# result=each_position_with_square(user)
# print(result)









'Replace each element with cube '
# def each_position_with_cube(n):
#     l=[]
#     for i in n:
#         l.append(i**3)
#     return l



# user=eval(input("enter your list"))
# result=each_position_with_cube(user)
# print(result)










'.Replace even numbers with their square '
# def even_number_square(n):
#     l=[]
#     for i in n:
#         if i%2==0:
#             l.append(i**2)
#         else:
#             l.append(i)
#     return l
# user=eval(input("enter your list"))
# result=even_number_square(user)
# print(result)







'Replace numbers > 10 with 100 '
# def replace_number_greater10(n):
#     l=[]
#     for i in n:
#         if i>10:
#             l.append(100)
#         else:
#             l.append(i)
#     return l

# user=eval(input('enter your list'))
# result=replace_number_greater10(user)
# print(result)







'.Replace each element with difference from max '
# def replace_each_element_with_max(n):
#     maximum=None
#     l=[]
#     for i in n:
#         if maximum is None or i>maximum:
#             maximum=i
#     for j in n:
#         diffrence=j-maximum
#         l.append(diffrence)
#     return l

# user=eval(input("enter your list"))
# result=replace_each_element_with_max(user)
# print(result)





