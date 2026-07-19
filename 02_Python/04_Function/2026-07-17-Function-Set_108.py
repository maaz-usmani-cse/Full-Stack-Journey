'''
Character frequency dict banani hai lekin output mein sirf wahi characters aane chahiye 
jo 1 se zyada baar repeat huye hain.

Input: s = "success"

Expected Output: {'s': 3, 'c': 2}

'''

# def repeates_character_freq_dict(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     res={}
#     for i in d:
#         if d[i]>>1:
#             res[i]=d[i]
#     return res

# user=input("enter your character")
# result=repeates_character_freq_dict(user)
# print(result)



'''
Filter Dictionary Keys with Even Length and Truthy Values

Task: Dict se un keys ko filter karo jinki string length even ho aur value None ya False na ho.

Input: d = {"data": "ok", "test": None, "py": True, "code": False}

Expected Output: {"data": "ok", "py": True}

'''

# def filter_even_length_keys(d):
#     res={}
#     for i in d:
#         if len(i)%2==0 and (d[i] is not None and d[i] is not False):
#             res[i]=d[i]
#     return res

# user=eval(input("enter your list"))
# result=filter_even_length_keys(user)
# print(result)





'''
Item tuples ki list [(brand, price), ...] se brand ko key aur unki maximum price ko value banao.

Input: items = [("Nike", 2000), ("Adidas", 3000), ("Nike", 2500)]

Expected Output: {"Nike": 2500, "Adidas": 3000}

'''
# def max_price_by_brand(l):
#     d={}
#     for brand,price in l:
#         if brand in d:
#             if price>d[brand]:
#                 d[brand]=price
#         else:
#             d[brand]=price

#     return d

# user=eval(input("enter your list"))
# result=max_price_by_brand(user)
# print(result)




'''
Convert String Query to Dictionary

Task: URL query parameters jaisi string ko parse karke dictionary banani hai.

Input: query = "name=maaz&dept=cse&year=4"

Expected Output: {"name": "maaz", "dept": "cse", "year": "4"}
'''

  
# def convert_string_query_to_dict(s):
#     res={}
#     part=s.split('&')
#     for i in part:
#         key_value=i.split('=')
#         key=key_value[0]
#         value=key_value[1]
#         res[key]=value
#     return res

# user=input("enter your list")
# result=convert_string_query_to_dict(user)
# print(result)   




'''
Task: Dict keys agar digit string hain (jaise '5'), toh unka integer square karke value banao, baaki keys ignore karo.

Input: d = {"2": 10, "abc": 20, "5": 4}

Expected Output: {2: 4, 5: 25}

'''

def string_digit_key_value_square(d):
    res={}
    for i in d:
     if i.isdigit() and type(i)==str:
        key=int(i)
        res[key]=key**2
    return res

user=eval(input("enter your dict"))
result=string_digit_key_value_square(user)
print(result)
