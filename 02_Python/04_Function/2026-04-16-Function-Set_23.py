'check data type'
# def check_data_type(n):
#     try:
#         val=eval(n)
#         print(type(val))
#     except:
#         print(type(n))

# user=input("enter your data")
# check_data_type(user)





'kon aysa number h jo do bar aa rha hai'
# def extaly_twice(n):
#     l=[]
#     total=0
#     for i in n:
#         count=0
#         for j in n:
#             if i==j:
#                 if i not in l:
#                  count=count+1
#         if count==2:
#          l.append(i)
#     for i in l:
#        total=total+1
#     return total


# user=eval(input("enter your list"))
# result=extaly_twice(user)
# print(result)




'jo value do s zyadh ayi h waha waha 0'
# def replace_element(n):
#     l=[]
#     for i in n:
#         count=0
#         for j in n:
#             if i==j:
#                 count=count+1
#         if count>2:
#             l.append(0)
#         else:
#             l.append(i)
#     return l


# user=eval(input("enetr your list"))
# result=replace_element(user)
# print(result)




'Create a program to rotate list'
# def rotate_list(l,steps,direction):
#     direction=direction.lower()
#     temp_left=l[0]
#     temp_right=l[-1]
#     for i in range(steps):
#         if direction=='left':
#             for i in range(len(l)-1):
#                 l[i]=l[i+1]
#             l[-1]=temp_left
#         elif direction=='right':
#             for i in range(len(l)-1,0,-1):
#                 l[i]=l[i-1]
#             l[0]=temp_right
#     return l


# list=eval(input("enter your list"))
# steps=int(input("enter your number"))
# direction=input("enter your direction")
# result=rotate_list(list,steps,direction) 
# print(result)      
    











