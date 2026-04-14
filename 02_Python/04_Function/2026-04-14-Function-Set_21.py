'list k element m check kro sbse zyadh bar kon aya hai '
# def frequency_count(n):
#     d={}
#     for i in n:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     max_count=0
#     ans=None
#     for i in d:
#         if d[i]>max_count:
#             max=d[i]
#             ans=i
#     return 'ye sbse zayadh bar aya hai',ans


# user=eval(input("enter your list"))
# result=frequency_count(user)
# print(result)










'replace dublicate with 0'
# def replace_dublicate(n):
#    l=[]
#    for i in n:
#       if i in l:
#          l.append(0)
#       else:
#          l.append(i)
#    return l

# user=eval(input("enter your list"))
# result=replace_dublicate(user)
# print(result)











'right shift or left shift kro listk element k sath '
# def right_shift_or_left_shift(n1,n2):
#     temp1=n1[0]
#     temp2=n2[-1]
#     for i in range(len(n1)-1):
#         n1[i]=n1[i+1]   
#     n1[-1]=temp1
    
#     for j in range(len(n2)-1,0,-1):
#         n2[j]=n2[j-1]
#     n2[0]=temp2
#     return 'ye left shift hai',n1, 'ye right shift hai',n2



# left_shift=eval(input("enter your list"))
# right_shift=eval(input("enter your list"))
# result=right_shift_or_left_shift(left_shift,right_shift)
# print(result)










'T print kro T shape me '
# def t_shape(n):
#     mid=(n//2)+1
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i==1 or j==mid:
#                 print('T',end=' ')
#             else:
#                 print(" ",end=' ')
#         print()


# user=int(input("enter your number"))
# t_shape(user)
            












'z pattern s print kro bhai aap'
# def z_shape(n):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i==1 or i==n or i+j==n+1:
#                 print('Z',end=' ')
#             else:
#                 print(' ',end=' ')
#         print()

# user=int(input("enter your number"))
# z_shape(user)





