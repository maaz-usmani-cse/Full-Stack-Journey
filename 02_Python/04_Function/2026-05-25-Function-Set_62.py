'''
: Django Rest Framework mein tumhaare paas active orders ka data aaya hai. Tumhe frontend par dropdown dikhane ke liye sirf un orders ka data bhejna hai jo "delivered" ho chuke hain. Lekin frontend developer ne bola hai ki mujhe puri dictionary mat bhejo, mujhe sirf un orders ki IDs ko String format mein badal kar ek nayi list bana kar do!

Task: Ek single-line list comprehension chalao jo orders ko filter bhi kare aur unki IDs ko string (str()) mein transform bhi kare.

Test Input:

Python
orders = [
    {"order_id": 1001, "status": "pending"},
    {"order_id": 1002, "status": "delivered"},
    {"order_id": 1003, "status": "delivered"},
    {"order_id": 1004, "status": "cancelled"}
]

'''
# def filter_data(l):
#      res=[str(i['order_id'])for i in l if 'status' in i if i['status']=='delivered']
#      return res


# user=eval(input("enter your list"))
# result=filter_data(user)
# print(result)



# orders = [
#     {"order_id": 1001, "status": "pending"},
#     {"order_id": 1002, "status": "delivered"},
#     {"order_id": 1003, "status": "delivered"},
#     {"order_id": 1004, "status": "cancelled"}
# ]
# res=list(filter(lambda x: "status" in x  and x["status"]=='delivered',orders))
# print(res)



'''
Database se tumhare paas 4 users ka data aaya hai. Kuch users ka account is_active: True hai 
aur kuch ka is_active: False.

Frontend developer ne bola: "Bhai Maaz, mujhe un users ka data chahiye jo active (True) hain."

# '''
# def filter_user_data(l):
#     res = [i["username"] for i in l if 'is_active' in i if i["is_active"] == True]
#     return res


# user = [
#     {"username": "maaz_rits", "is_active": True},
#     {"username": "asif_99", "is_active": False},
#     {"username": "rohit_dev", "is_active": True},
#     {"username": "amjad_hr", "is_active": False}
# ]
# result=filter_user_data(user)
# print(result)







'longest aassending sequence'
# def longest_sequence(l):
#     current=1
#     longest=1
#     for i in range(len(l)-1):
#         if l[i+1]>l[i]:
#             current=current+1
#         else:
#             if current>longest:
#                longest=current
#             current=1
        
#     if current>longest:
#         longest=current
      
#     return longest


        
# user=eval(input("enter your list"))
# result=longest_sequence(user)
# print(result)



