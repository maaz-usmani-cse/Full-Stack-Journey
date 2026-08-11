'	Find largest element '
# def find_largest(l):
#     largest=None
#     for i in l:
#         if largest is None or i>largest:
#             largest=i
#     return largest


# user=eval(input("enter your list"))
# result=find_largest(user)
# print(result)






'Find second largest element '

# def second_largest_element(l):
#     first=None
#     second=None
#     for i in l:
#         if first is None or i>first:
#             second=first
#             first=i

#         elif i!=first and (second is None or i>second):
#             second=i

#     return f'second largest is:{second}'


# user=eval(input("enter your list"))
# result=second_largest_element(user)
# print(result)





'Reverse array '
# def reverse_array(l):
#     for i in range(len(l)//2):
#         temp=l[i]
#         l[i]=l[len(l)-1-i]
#         l[len(l)-1-i]=temp

#     return l


# user=eval(input("enter your list"))
# result=reverse_array(user)
# print(result)





'Rotate array by k positions '

# def rotate_array_k_time(l,position,k):
#     for i in l:
#         if position=='left':
#            return l[k:]+l[:k]

#         elif position=='right':
#            return l[-k:]+l[:-k]



# user=eval(input("enter your list"))
# position=input("enter your position")
# k=int(input("ener your k"))
# result=rotate_array_k_time(user,position,k)
# print(result)
    

