'''
Ek function find_max_key(d) banao jo ek dictionary accept kare aur us key ka naam return kare
 jiski value sabse badi (maximum) ho.

Input Data: {'apple': 50, 'banana': 80, 'cherry': 30, 'orange': 75}

Expected Output: 'banana' (kyunki 80 sabse bada hai)
'''

# def greater_value(d):
#     max_value=None
#     key=None
#     for i in d:
#         if max_value is None or d[i]>max_value:
#             max_value=d[i]
#             key=i
#     return key

# user=eval(input("enter your list"))
# result=greater_value(user)
# print(result)










'value k basis p dictionary ko sort kro'
# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
    
#     pivot=l[0]
#     pivot_value=pivot[1]
#     left=[]
#     middle=[]
#     right=[]

#     for i in l:
#         if i[1]<pivot_value:
#             left.append(i)
#         elif i[1]==pivot_value:
#             middle.append(i)
#         else:
#             right.append(i)
#     return quick_sort_pivot(left)+ middle+ quick_sort_pivot(right)

# def sort_value_basic(d):
#     l=[]
#     for i in d:
#         l.append((i,d[i]))
#     sorting=quick_sort_pivot(l)
#     d={}
#     for key,value in sorting:
#         d[key]=value
#     return d


# user=eval(input("enter your list"))
# result=sort_value_basic(user)
# print(result)









'''
Remove Duplicates by Value (Ek jaisi values ko hatao)
Ek function remove_duplicate_values(d) banao jo dictionary mein se un keys ko delete ya skip kar de jinki 
values repeat ho rahi hain. Pehli baar aane wali value ko rakhna hai, baad wali duplicate ko hatana hai.

Input Data: {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

Expected Output: {'a': 10, 'b': 20, 'd': 30}
'''

# def remove_dublice_value(d):
#     new_d={}
#     seen_value={}
#     for i in d:
#        if d[i] not in seen_value:
#            new_d[i]=d[i]
#            seen_value[d[i]]=True
       
#     return new_d


# user=eval(input("enter your list"))
# result=remove_dublice_value(user)
# print(result)









'''

Jaise aapne values ko sort kiya tha, ab ek function sort_dict_by_keys(d) banao jo dictionary ko uski keys ke basis par A-Z 
(Alphabetical order) mein sort kare. Isme bhi aap apna custom sorting algorithm (jaise Selection Sort ya Quick Sort) use kar sakte hain.

Input Data: {'z': 10, 'b': 5, 'a': 20, 'm': 30}

Expected Output: {'a': 20, 'b': 5, 'm': 30, 'z': 10}

'''


# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
#     pivot=l[0]
#     pivot_key=pivot[0]
#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i[0]<pivot_key:
#             left.append(i)
#         elif i[0]==pivot_key:
#             middle.append(i)
#         else:
#             right.append(i)
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)


# def sort_by_key(d):
#     l=[]
#     for i in d:
#         l.append((i,d[i]))
#     sorting_res=quick_sort_pivot(l)
#     d={}
#     for key,value in sorting_res:
#         d[key]=value
#     return d


# user=eval(input("enter your list"))
# result=sort_by_key(user)
# print(result)






'Duplicate Number '

# def dublicate_number(l):
#     d={}
#     new=[]
#     for i in d:
#         if i in d:
#             new.append(i)
#         else:
#             d[i]=True
#     return l


# user=eval(input("enter your list"))
# result=dublicate_number(user)
# print(result)
    




'Pair Sum Closest to Target '
def quick_sort_pivot(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[]
    middle=[]
    right=[]
    for i in l:
        if i<pivot:
            left.append(i)
        elif i==pivot:
            middle.append(i)
        else:
            right.append(i)
    return quick_sort_pivot(left)+middle+ quick_sort_pivot(right)

def find_closest_pair(l,target):
    sorting=quick_sort_pivot(l)
    min_diff=float('inf')
    closest_pair=(None,None)
    left_pointer=0
    right_pointer=len(l)-1
    while left_pointer<right_pointer:
        Current_sum=sorting[left_pointer]+sorting[right_pointer]
        diff=abs(Current_sum-target)
        if diff<min_diff:
            min_diff=diff
            closest_pair=(sorting[left_pointer],sorting[right_pointer])
        if Current_sum<target:
            left_pointer=left_pointer+1
        else:
            right_pointer=right_pointer-1
    return closest_pair


user=eval(input("enter your list"))
target=int(input("enter your target number"))
result=find_closest_pair(user,target)
print(result)
    

        

        


