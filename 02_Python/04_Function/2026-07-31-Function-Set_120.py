'find longest sequesnce'
# def longest_sequence(l):
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


#     return longest


# user=eval(input("enter your list"))
# result=longest_sequence(user)
# print(result)





'Find longest subarray with equal even and odd elements '


# def longest_equal_even_odd_subarray(l):
#    seen={0:-1}
#    longest=0
#    curren_sum=0
#    for i in range(len(l)):
#       curren_sum=curren_sum+1 if l[i]%2==0 else -1
#       if curren_sum in seen:
#          length=i-seen[curren_sum]
#          if length>longest:
#             longest=length

#       else:
#          seen[curren_sum]=i
#    return longest


# user=eval(input("enter your list"))
# result=longest_equal_even_odd_subarray(user)
# print(result)




'find missing value'
# def find_missing_value(l):
#     d={}
#     for i in range(len(l)):
#         d[l[i]]=True

#     for i in range(1,len(l)+1):
#         if i not in d:
#             return f'missing value is {i}'
#     return None



# user=eval(input("enter your list"))
# result=find_missing_value(user)
# print(result)
    



42


'Arrange array so local minimums come at even indexes --done'
# def arrange_local_minimum(l):
#     for i in range(len(l)-1):
#         if i%2==0 and l[i]>l[i+1]:
#             temp=l[i]
#             l[i]=l[i+1]
#             l[i+1]=temp
#         elif i%2!=0 and l[i]<l[i+1]:
#             temp=l[i]
#             l[i]=l[i+1]
#             l[i+1]=temp
#     return l


# user=eval(input("enter your list"))
# result=arrange_local_minimum(user)
# print(result)




'Findthesecond largest element in an array.'
# def find_second_largest(l):
#     first=None
#     second=None
#     for i in l:
#         if first is None or i>first:
#             second=first
#             first=i
#         elif i != first and (second is None or i>second):
#             second=i

#     return f'second largest is {second}'


# user=eval(input("enter your list"))
# result=find_second_largest(user)
# print(result)

 




