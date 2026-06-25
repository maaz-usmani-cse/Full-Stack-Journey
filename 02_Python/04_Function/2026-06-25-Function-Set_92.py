'dublicate remove '
# def remove_dublicate(l):
#     res=[]
#     d={}
#     for i in l:
#         if i not in d:
#             res.append(i)
#             d[i]=True
#     return res


# user=eval(input("enter your list"))
# result=remove_dublicate(user)
# print(result)







'find common value'
# def find_common(l1,l2):
#     d={}
#     res=[]
#     for i in l1:
#         d[i]=True
#     for j in l2:
#         if j in d:
#             del d[j]
#             res.append(j)
#     return res

# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=find_common(l1,l2)
# print(result)







'''
Maaz, humare paas 1 se lekar $N$ tak ke continuous Roll Numbers (IDs) ki ek list honi chahiye thi 
(jaise [1, 2, 3, 4]). Lekin system mein ek bug ki wajah se ek ID Duplicate ho gayi aur uski wajah 
se ek ID Missing (gayab) ho gayi!Mujhe bina kisi inbuilt function ke, Dictionary ka use karke ek hi 
baar mein batao ki kaun si ID duplicate hui hai aur kaun si missing hai!"Input:
 l = [1, 2, 2, 4] (Yahan 1 se 4 tak ginti honi chahiye thi)Output: Duplicate = 2, Missing = 3

'''

# def find_dublicate_and_missing_value(l):
#     d={}
#     missing=None
#     dublicate=None
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for i in range(len(l)+1):
#         if i not in d:
#             missing=l[i]
#         elif d[i]>1:
#             dublicate=l[i]
#     return f'dublicate={dublicate} missing={missing}'



# user=eval(input("enter your list"))
# result=find_dublicate_and_missing_value(user)
# print(result)










'Sort only even elements '
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


# def sort_odd_number(l):
#     odd=[]
#     for i in range(len(l)):
#         if l[i]%2!=0:
#             odd.append(l[i])
#     sort_odd=quick_sort_pivot(odd)
#     j=0
#     for i in range(len(l)):
#         if l[i]%2!=0:
#             l[i]=sort_odd[j]
#             j=j+1

#     return l



# user=eval(input("enter your list"))
# result=sort_odd_number(user)
# print(result)











'''
Dictionary Merger with Values Sum

Sawaal: Tumhein do alag-alag dictionaries di hain (jaise dukaandaron ki inventory). 
Unhe aapas mein merge karo. Agar koi key dono mein common hai, toh unki values (ginti) 
aapas mein judni (+) chahiye!

Input: d1 = {'a': 100, 'b': 200}, d2 = {'a': 300, 'c': 500}

Output: {'a': 400, 'b': 200, 'c': 500}

'''



# def merge_two_list(d1,d2):
#     add={}
#     for i in d1:
#        add[i]=d1[i]
#     for j in d2:
#         if j in add:
#             add[j]=add[j]+d2[j]
#         else:
#             add[j]=d2[j]
#     return add

# d1=eval(input("enter your list"))
# d2=eval(input("enter your list"))
# result=merge_two_list(d1,d2)
# print(result)






