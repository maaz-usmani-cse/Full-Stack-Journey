'''
Django ke contact form se users ne inputs bheje hain. Kuch logon ne phone number ya email ki 
jagah galti se sirf khali spaces "   " bhej diye hain ya field khali chhor di hai.
Agar tumne ye data database mein save kiya toh models crash ho jayenge.

Test Input: form_inputs = ["   maaz@gmail.com ", "", "bhopal_rits", None, "   "]

Expected Output: ['maaz@gmail.com', 'bhopal_rits']
'''
 

# def filter_data(l):
#     res=[i.strip()for i in l if i is not None and i.strip()!='']
#     return res

# user=eval(input("enter your list"))
# result=filter_data(user)
# print(result)












'list ka kon aysa number hai jo apne aagey wale s sbse bda ho '
# def check_greater(l):
#     li=[]
#     for i in range(len(l)):
#         for j in range(1,len(l)):
#             index=(i+j)%len(l)
#             if l[index]>l[i]:
#                 break
#         else:
#             li.append(l[i])
#     return li



# user=eval(input("enter your list"))
# result=check_greater(user)
# print(result)










'''
Django e-commerce views mein tumhe products ka price calculate karna hai.
Agar product ki category "Luxury" hai, toh uspar $18\%$ tax lagega (price * 1.18). 
Agar category "Essential" hai, toh price same rahega (no tax).
'''

# def product_price_filter(l):
#     for i in l:
#         if  'category'in i and 'price' in i:
#             if i['category']=='Luxury':
#                 i['price']=i['price'] * 1.18
#     return l




# user=eval(input("enter your list"))
# result=product_price_filter(user)
# print(result)








'''
Tumhe active users ko filter bhi karna hai, aur frontend par bhejne ke liye unke naam ko Upper Case 
(.upper()) mein badalna bhi hai!

1. List Comprehension se (Ekdam Makkhan Line):
Python
users = [
    {"username": "maaz", "active": True},
    {"username": "amjad", "active": False},
    {"username": "rohit", "active": True}
]

'''

# def filter_data(l):
#     res=[i['username'].upper() for i in l if i['active']==True]
#     return res


# user=eval(input("enter your list"))
# result=filter_data(user)
# print(result)


