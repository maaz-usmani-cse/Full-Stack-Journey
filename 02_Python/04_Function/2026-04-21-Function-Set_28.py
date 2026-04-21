
'dictionary ko list m dalo bina kisi inbuilt k phir usi dict ko dusri dict m dalo'
# def convert(d):
#     new_dict={}
#     l=[]
#     for i in d:
#         l.append([i,d[i]])
#     for i in l:
#         new_dict[i[0]]=i[1]
#     return new_dict


# user=eval(input("enetr your dict"))
# result=convert(user)
# print(result)








'Do lists ko bina zip() ke ek dictionary mein convert karo. (Ek key ki list hogi, ek value ki).'
# def convert_twolist(l1,l2):
#     d={}
#     for i in range(len(l1)):
#         key=l1[i]
#         value=l2[i]
#         d[key]=value
#     return d

# keys=input("enetr your list").split(',')
# value=input("enetr your value").split(',')
# result=convert_twolist(keys,value)
# print(result)





'check iquilibrioum index'

# def iqulibrioum_index(n):
#     for i in range(len(n)):
#         left_sum=0
#         for j in range(0,i):
#             left_sum=left_sum+n[j]
#         right_sum=0
#         for k in range(i+1,len(n)):
#             right_sum=right_sum+n[k]
#         if left_sum==right_sum:
#             return 'iquilibrium index',i
#     return -1

# user=eval(input("enetr your list"))
# result=iqulibrioum_index(user)
# print(result)






'Ek dictionary se wo saari keys delete karo jinki value Even hai.'
# def delete_even(d):
#     new_dict={}
#     for i in d:
#         if d[i]%2==0:
#             pass
#         else:
#             new_dict[i]=d[i]
#     return new_dict



'Ek list di hai [1, 2, 2, 3, 3, 3], ek dictionary banao jo dikhaye kaunsa number kitni baar aaya hai. {1:1, 2:2, 3:3}.'
# def count_list_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# user=eval(input("enetr your list"))
# result=count_list_element(user)
# print(result)




'Dictionary ki saari keys aur values ko swap (interchange) kardo.'
# def swap(d):
#     new_dict={}
#     for i in d:
#         value=d[i]
#         key=i
#         new_dict[value]=key
#     return new_dict

# user=eval(input("enetr your dict"))
# result=swap(user)
# print(result)






'Ek list ke andar dictionaries hain (jaise employees ka data), usme se wo employee dhoondo jiski salary sabse zyada hai.'
'''
##You can check from this example
[
    {"name": "Maaz", "salary": 25000},
    {"name": "Ali", "salary": 45000},
    {"name": "Rohit", "salary": 30000}
]


'''
# def find_highest_salary(l):
#     max_salary=None
#     for i in l:
#         if max_salary is None or i['salary']>max_salary:
#             max_salary=i['salary']
#     return max_salary



# user=eval(input("enter your dict"))
# result=find_highest_salary(user)
# print(result)






'Do dictionaries ko merge karo bina | ya update() ke. Agar key same ho, toh values ko add kar dena.'
# def merge_dict(d1,d2):
#     new_dict={}
#     for i in d1:
#         new_dict[i]=d1[i]
#     for j in d2:
#         if j in new_dict:
#             new_dict[j]=new_dict[j]+d2[j]
#         else:
#             new_dict[j]=d2[j]
#     return new_dict

# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 5, 'c': 10, 'd': 50}
# result=merge_dict(dict1,dict2)
# print(result)






'Ek dictionary ko uski Values ke basis par sort karo (bina sorted() ke, manual bubble sort logic se try karo).'
# def sort(d):
#     l=[]
#     new_dict={}
#     for i in d:
#         l.append([i,d[i]]) 
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i][1] > l[j][1]:
#                 temp=l[i]
#                 l[i]=l[j]
#                 l[j]=temp
#     for i in l:
#         new_dict[i[0]]=i[1]
#     return new_dict


# user=eval(input("enetr your dict"))
# result=sort(user)
# print(result)

    






