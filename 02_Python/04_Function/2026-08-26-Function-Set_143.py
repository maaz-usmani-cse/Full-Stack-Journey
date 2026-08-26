'''
Dictionary ko Values ke Basis Par Sort Karna
Task: Dictionary ko uski values ke according ascending ya descending order mein sort karo.

'''
# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
    
#     pivot=l[0][1]
#     left=[]
#     middle=[]
#     right=[]

#     for i in l:
#         if i[1]<pivot:
#             left.append(i)

#         elif i[1]==pivot:
#             middle.append(i)

#         else:
#             right.append(i)

#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)




# def sort_value_basic(d):
#    l=[]
#    for i in d:
#        l.append((i,d[i]))

#    sorting=quick_sort_pivot(l)

#    res={}
#    for key, value in sorting:
#        res[key]=value
#    return res


# user=eval(input("enter your dict"))
# result=sort_value_basic(user)
# print(result)
  




'Sirf un items ko retain karo jinka stock 10 se zyada ho.'

# def filter_data(d):
#     res={}
#     for i in d:
#         if d[i]>10:
#             res[i]=d[i]
#     return res


# user=eval(input("enter your dict"))
# result=filter_data(user)
# print(result)
    




'Highest value wali key return karo bina pure dictionary ko sort kiye.'
# def find_highest_value(d):
#     first_key=''
#     max_value=None
#     for i in d:
#         if max_value is None or d[i]>max_value:
#             max_value=d[i]
#             first_key=i
#     return f'highest value key is {first_key}'

# user=eval(input("enter your list"))
# result=find_highest_value(user)
# print(result)
    



'Ek binary list di gayi hai. Lagaataar sabse zyada kitni baar 1 aaya hai uska count nikalo.Input: nums = [1, 1, 0, 1, 1, 1] $\rightarrow$ Output: 3'

# def consecutive_element_count(l):
#     res=1
#     current=1
#     for i in range(len(l)-1):
#         if l[i]==l[i+1]:
#             current=current+1
#         else:
#             if current>res:
#                 res=current
#             current=1
#     if current>res:
#         res=current

#     return res


# user=eval(input("enter your list"))
# result=consecutive_element_count(user)
# print(result)

