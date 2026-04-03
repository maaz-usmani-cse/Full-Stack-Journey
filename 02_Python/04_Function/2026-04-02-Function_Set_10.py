'Ek function likho jo do dictionaries ko merge kare.'
# def merge_dict(dict1,dict2):
#     return dict1 | dict2


# d1=eval(input("enter your number"))
# d2=eval(input("enter your number"))
# result=merge_dict(d1,d2)
# print(result)



'Function banayein jo check kare ki koi key dictionary mein exist karti hai ya nahi.'
# def check_key(d,key):
#     if key in d:
#         return True
#     else:
#         return False
    
# dictnories=eval(input("enter your Dictionaries"))
# key=input("enter your Key")
# result=check_key(dictnories,key)
# print(result)




'Ek dictionary ke saare values ka sum nikalne ka function.'
# def sum_of_value_in_dict(d):
#     total=0
#     for i in d:
#         total=total+d[i]
#     return total


# user=eval(input('enter your dict'))
# result=sum_of_value_in_dict(user)
# print(result)




'Dictionary mein se maximum aur minimum value find karne ka code.'
# def find_minimum_maximum_in_dict(d):
#     minimum=None
#     maximum=None
#     for i in d:
#         if minimum is None or d[i]<minimum:
#             minimum=d[i]
#         elif maximum is None or d[i]>maximum:
#             maximum=d[i]
#     return "minimum :",minimum, "maximum :", maximum

# user=eval(input("enter your dict"))
# result=find_minimum_maximum_in_dict(user)
# print(result)





'Ek function jo user se input lekar dictionary create kare.'

# def build_dict(mydict,key,value):
#     mydict[key]=value
#     return mydict




# dict={}
# while True:
#     k=input("enter key").strip()
#     if k=="stop":
#         break
#     if not k or k=="'" or k=='"':
#         print("key dalna zrori hai")
#         continue


#     v=input("enter value").strip()
#     if not v or v=="'" or v=='"':
#         print("value dena zroori hai")
#         continue
    
#     result=build_dict(dict,k,v)
#     print(result)




