'''
Ek list hai students ki: users = [{'name': 'maaz'}, {'name': 'ali'}, {'name': 'rohit'}]. 
Loop chala kar check karo agar 'maaz' naam ka banda list mein hai ya nahi.
'''
# def find_user(d,check):
#     for i in d:
#         if i['name']==check:
#             return 'yes hai'
#     return 'nahi hai'


# d=eval(input("enter your list"))
# check=input("enter your word to find")
# result=find_user(d,check)
# print(result)








'''
l = [{'name': 'A', 'marks': 40}, {'name': 'B', 'marks': 25}, {'name': 'C', 'marks': 50}]
. Sirf un bachon ke naam print karo jinke marks 30 se zyada hain.

'''
# def find_marks_above_30(l):
#   name=[]
#   for i in l:
#     if i['marks']>30:
#       name.append(i['name'])
#   return name

# user=eval(input("enter your list"))
# result=find_marks_above_30(user)
# print(result)










'''
l = [{'name': 'maaz', 'score': 100}, {'name': 'amjad', 'score': 50}]. Loop ke andar logic likho ki agar name 'maaz' mile,
 toh uska score update karke 150 kar do.
'''
# def update_score(l):
#     for i in l:
#      if 'name' in i and i['name']=='maaz':
#             i['score']=150
#     return l

# user=eval(input("enter your list"))
# result=update_score(user)
# print(result)










'''
l = [{'id': 1, 'city': 'bhopal', 'pin': 462001}]. Bina .keys() method ke,
 ek loop se saari keys nikaal kar list mein daalo.

'''
# def key_transfer_in_list(l):
#     all_keys=[]
#     for i in l:
#       for keys in i:
#          all_keys.append(keys)
#     return all_keys

# user=eval(input('enter your list'))
# result=key_transfer_in_list(user)
# print(result)










'''
l = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]. 
Isse ek simple list banao jo aisi dikhe: [1, 2, 3, 4]. (Nested loop use hoga).

'''

# def complex_to_simple(l):
#     simple_list=[]
#     for i in l:
#         for key in i:
#             value=i[key]
#             simple_list.append(value)
#     return simple_list


# user=eval(input("enetr your list"))
# result=complex_to_simple(user)
# print(result)





'''
l = [{'gender': 'M'}, {'gender': 'F'}, {'gender': 'M'}]. 
Loop chala kar gino ki 'M' kitni baar aaya hai.
'''
# def Count_Occurrences(l):
#     count=0
#     for i in l:
#         for key in i:
#             if i[key]=='M':
#                 count=count+1
#     return count

# user=eval(input("enter your list"))
# result=Count_Occurrences(user)
# print(result)







'''
l = [{'price': 100}, {'price': 500}, {'price': 200}].
 Loop chala kar sabse badi price (max price) find karo.
# '''

# def find_max_price(l):
#     max_price=None
#     for i in l:
#         if 'price' in i and (max_price is None or i['price']>max_price):
#             max_price=i['price']
#     return max_price


# user=eval(input("enter your list"))
# result=find_max_price(user)
# print(result)

