'''
Filter Dictionary by List of Allowed Keys

Task: Ek bade config dictionary se sirf wahi keys filter karni hain jo ek specified list mein di gayi hon.

Input: conf = {"host": "localhost", "port": 8000, "debug": True}, allowed = ["host", "debug"]

Expected Output: {"host": "localhost", "debug": True}

'''

# def filter_keys_by_specified_list(d,l):
#     res={}
#     for i in d:
#         if i in l:
#             res[i]=d[i]
#     return res

# d=eval(input("enter your dict"))
# l=eval(input('enter your list'))
# result=filter_keys_by_specified_list(d,l)
# print(result)
    
        







'''
Create Inverted Index (Word to Index Mapping)

Task: Strings ki list se ek dictionary banani hai jahan key word ho aur value un indices ki list ho jahan wo aaya hai.

Input: data = ["apple", "banana", "apple", "cherry"]

Expected Output: {"apple": [0, 2], "banana": [1], "cherry": [3]}

'''

# def create_invertedz_indexing(l):
#     d={}
#     for i in range(len(l)):
#        if l[i] in d:
#             d[l[i]].append(i)
#        else:
#            d[l[i]]=[i]
#     return d

# user=eval(input("enter your list"))
# result=create_invertedz_indexing(user)
# print(result)      







'''
recursion k flatten diction m '_' add kro 

'''

# def flatten_dict_recursive(d, parent_key=''):
#     res = {}
    
   
#     for key in d:
#         value = d[key]
        
      
#         if parent_key != '':
#             new_key = parent_key + '_' + key
#         else:
#             new_key = key
            

    #     if type(value) == dict:
          
    #         sub_dict = flatten_dict_recursive(value, new_key)
    #         for sub_key in sub_dict:
    #             res[sub_key] = sub_dict[sub_key]
    #     else:
           
    #         res[new_key] = value
            
    # return res

# d_complex = {"user": {"name": "Maaz", "details": {"id": 1, "city": "Delhi"}}}
# print(flatten_dict_recursive(d_complex))



def factorial_any_number(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial

user=int(input("enter your number"))
result=factorial_any_number(user)
print(result)