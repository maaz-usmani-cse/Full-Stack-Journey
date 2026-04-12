
'left shift'
# def left_shift(n):
#     temp=n[0]
#     for i in range(len(n)-1):
#     a    n[i]=n[i+1]
#     n[-1]=temp
#     return n

# user=eval(input("enter your list"))
# result=left_shift(user)
# print(result)






'lef shift with one line through the slicing (STANDARD-WAY)'
# def left_shift(n):
#     left_shift=n[1:]+n[0:1]
#     return left_shift

# user=eval(input("enter your list"))
# result=left_shift(user)
# print(result)



'left shift with basic indexing 4 element p mene kiya hai q ki phir shift ho nnhai payega 4 se zyadh element ka q ki n[3] tak ham gye hai'
# def indexing(n):
#     if len(n)<=4:
#       temp=n[0]
#       n[0]=n[1]
#       n[1]=n[2]
#       n[2]=n[3]
#       n[3]=temp
#       return n


# user=eval(input("enter your list"))
# result=indexing(user)
# print(result)






'right shift in list'
# def right_shift(n):
#     temp=n[-1]
#     for i in range(len(n)-1,0,-1):
#         n[i]=n[i-1]
#     n[0]=temp
#     return n


# user=eval(input("enter your list"))
# result=right_shift(user)
# print(result)





'right shift with the help of slicing'
# def right_shift(n):
#     right_sfift=n[-1:]+n[:-1]
#     return right_sfift
# user=eval(input('enter your list'))
# result=right_shift(user)
# print(result)




'user s data leke check kro ki wo uska data type kya hai'
# def check_data_type(n):
#     try:
#         val=eval(n)
#         print(type(val))
#     except:
#         print(type(n))

# user=input("enter everything")
# check_data_type(user)
    






