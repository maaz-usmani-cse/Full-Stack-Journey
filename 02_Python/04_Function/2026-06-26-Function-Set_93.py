
'''
Dictionary Filtering & Sorting by ValueSawaal: Ek dictionary mein students ke 
naam aur unke marks hain. Pehle un students ko hatao (del karo) jinke marks 33 se kam hain, 
aur bache hue students ko unke marks ke ascending order mein sort karke dikhao (bina inbuilt zip/lambda 
ke, pure logic se).Input: {'Maaz': 85, 'Rohit': 25, 'Amit': 65} $\rightarrow$ 
Output: {'Amit': 65, 'Maaz': 85}
'''



# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i<pivot:
#             left.append(i)
#         elif i==pivot:
#             middle.append(i)
#         else:
#             right.append(i)
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)


# def filter_student_data(d):
#     filter={}
#     l=[]
#     for i in d:
#         if d[i]>33:
#             marks=d[i]
#             filter[marks]=i
#             l.append(d[i])

#     sorting_data=quick_sort_pivot(l)
#     final_res= {}
#     for i in sorting_data:
#         name=filter[i]
#         final_res[name]=i
#     return final_res


# user=eval(input("enter your dict"))
# result=filter_student_data(user)
# print(result)







'Ek dictionary di hai jahan keys logo ke naam hain aur values unki city. '
'Ek function banao jo city ke basis par logo ko group kare.'

# def group_by_city(d):
#     group={}
#     for i in d:
#         city=d[i]
#         if city not in group:
#             group[city]=[]
#             group[city].append(i)
#         else:
#             group[city].append(i)
#     return group


# user=eval(input("enter your dict"))
# result=group_by_city(user) 
# print(result)   




        


'target number'
# def target_number(l,target):
#     d={}
#     for i in range(len(l)):
#         required=target-l[i]
#         if required in d:
#             return d[required],i
#         else:
#             d[l[i]]=i

# user=eval(input("enter your list"))
# target=int(input("enter your target number"))
# result=target_number(user,target)
# print(result)








'Ek dictionary mein products aur unke prices hain. Top 2 sabse mehnge products ke naam return karo.'

# def top_two_expensive_product(d):
#     first=None
#     second=None
#     first_name=None
#     second_name=None
#     for i in d:
#         if first is None or d[i]>first:
#             second=first
#             first=d[i]
#             second_name=first_name
#             first_name=i
#         elif i!=first and (second is None or d[i]>second):
#             second=d[i]
#             second_name=i

#     return [first_name,second_name]


# user=eval(input("enter your list"))
# result=top_two_expensive_product(user)
# print(result)



    