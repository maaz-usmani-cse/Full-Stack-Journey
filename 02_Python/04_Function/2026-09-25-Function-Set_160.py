'teen list me se common element find fro'

# def common_in_three_list(l1,l2,l3):
#     d1={}
#     d2={}
#     res=[]
#     for i in l1:
#         d1[i]=True
#     for j in l2:
#         if j in d1:
#             d2[j]=True
#     for k in l3:
#         if k in d2:
#             res.append(k)
#             del d2[k]
#     return res

# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# l3=eval(input("enter your list"))
# res=common_in_three_list(l1,l2,l3)
# print(res)
        


'har word ka position bdaho per out of character anhi jana chaiye'

# def change_position_every_char(word,position):
#     res=''
#     for i in word:
#         if i.islower():
#             old_position=ord(i)-ord('a')
#             new_position=(old_position+position)%26
#             res=res+chr(ord('a')+new_position)
#         elif i.isupper():
#             old_position=ord(i)-ord('A')
#             new_position=(old_position+position)%26
#             res=res+chr(ord('A')+new_position)
#     return res

# user=input("enetr your word")
# position=int(input("enter your number"))
# res=change_position_every_char(user,position)
# print(res)






        