'Replace each element with double value '
# def replace_double_each_element(l):
#     double=[]
#     for i in l:
#         double.append(i**2)
#     return double


# user=eval(input("enter your list"))
# result=replace_double_each_element(user)
# print(result)








'Replace each element with half value '
# def replace_each_half(l):
#     half=[]
#     for i in l:
#         half.append(i/2)
#     return half


# user=eval(input("enter your list"))
# result=replace_each_half(user)
# print(result)








'Replace even numbers with cube'
# def even_cube(l):
#     even_cube=[]
#     for i in l:
#         if i%2==0:
#             cube=i**3
#             even_cube.append(cube)
#     return even_cube

# user=eval(input("enter your list"))
# result=even_cube(user)
# print(result)







'Replace odd numbers with square '
# def replace_odd_squre(l):
#     odd_square_cube=[]
#     for i in l:
#         if i%2!=0:
#            cube=i**3
#            odd_square_cube.append(cube)
#     return odd_square_cube



# user=eval(input("enter your list"))
# result=replace_odd_squre(user)
# print(result)








'user se string lo aur even indexing print kro'
# def even_indexing(s):
#     for i in range(len(s)):
#         if i%2==0:
#             print(s[i])
       


# user=input('entr your message')
# even_indexing(user)






'''


'use a list comprehenshion to square eac odd number in a list
the list is input by a sequence of comma separated numbers 
suppose the following input is supplied to the program 1,2,3,4,5,6,7,8,9'
then the out put should be 1,3,5,7,9
'''
# def odd_number_list(s):
#     l=[]
#     res=s.split(',')
#     for i in res:
#         if int(i)%2!=0:
#             l.append(i)
#     return l


# user=input("enter your word")
# result=odd_number_list(user)
# print(*result)








'user n ayse "math:80,science:90,english:70" list diya ise dictionary m badlna hai '
student_data = [
    ["math", 80, "Sharma Sir", 101], 
    ["science", 90, "Verma Sir", 102]
]
d = {}

for i in student_data:
    for j in i:
        d[i]=id[i]

print(d)
