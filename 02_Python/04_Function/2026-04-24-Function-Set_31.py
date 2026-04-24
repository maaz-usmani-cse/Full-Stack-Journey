'next greater s value assign kro aap'
# def next_greater(n):
#     l=[-1]*len(n)
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[j]>n[i]:
#                 l[i]=n[j]
#                 break
#     return l

# user=eval(input("enetr your list"))
# result=next_greater(user)
# print(result)






'list m pehle dublicate jo v hai un sare jagh p dublicate likho  '
# def dublicate(l):
#     new_list=[]
#     for i in l:
#         if i not in new_list:
#             new_list.append(i)
#         else:
#             new_list.append(('dublicate of ',i))
#     return new_list

# user=eval(input("enter your list"))
# result=dublicate(user)
# print(result)






'Agar ek dictionary ke andar doosri '
'dictionary hai, toh use ek single level dictionary mein convert karo.'
# def converted_nested_dict(d):
#     new_dict={}
#     for i in d:
#         value=d[i]
#         if type(value)==dict:
#             res=converted_nested_dict(value)
#             for j in res:
#                 new_dict[j]=res[j]
#         else:
#             new_dict[i]=d[i]
#     return new_dict


# result=converted_nested_dict(d = {"a": {"b": 5}})
# print(result)
                






'Ek circular list mein har element ke liye usse bada agla element dhoondo.'

# def circular_greter(l):
#    new_list=[-1]*len(l)
#    for i in range(len(l)):
#       for j in range(1,len(l)):
#          index=(i+j)%len(l)
#          if l[index]>l[i]:
#           new_list[i]=l[index]
#           break
#    return new_list


# user=eval(input("enter your list"))
# result=circular_greter(user) 
# print(result)   






