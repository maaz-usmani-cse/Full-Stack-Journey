'Dictionary se kisi specific key ko remove karne ka function.'

# def remove_key_in_dict(originial_dict,target_key):
#     d={}
#     for i in originial_dict:
#       if i!=target_key:  
#             value=originial_dict[i]
#             d[i]=value
#     return d

# user=eval(input("enter your dict"))
# key=input("enter your remove key")
# result=remove_key_in_dict(user,key)
# print(result)




'Ek function jo dictionary ko values ke basis par sort kare.'

# def dict_sort_valuebase(d):
#     l=[]
#     mydict={}
#     for i in d:
#         l.append([i,d[i]])

#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i][1]>l[j][1]:
#               temp=l[i]
#               l[i]=l[j]
#               l[j]=temp
#     for i in l:
#        mydict[i[0]]=i[1]
#     return mydict


# user=eval(input("enter your dict"))
# result=dict_sort_valuebase(user)
# print(result)
    




