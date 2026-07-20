'''

Filter Even Squares in a Range

Task: range(1, 11) tak ke numbers mein se pehle unka square karna hai, aur fir sirf un squares ko rakhna hai jo Even hain.

Expected Output: [4, 16, 36, 64, 100]

'''

# def even_square():
#     res=[i**2 for i in range(1,11) if i%2==0]
#     return res




# result=even_square()
# print(result)







'''
Grouped Consecutive Differences

Task: Ek list ke aaju-baaju wale (consecutive) elements ka absolute difference nikalna hai.

Input: nums = [10, 14, 20, 25]

Expected Output: [4, 6, 5] (Kyunki |14-10|=4, |20-14|=6, |25-20|=5)

'''

# def absoulute_diff(l):
#     res=[]
#     for i in range(len(l)-1):
#         diff=abs(l[i]-l[i+1])
#         res.append(diff)
#     return res



# user=eval(input("enter your list"))
# result=absoulute_diff(user)
# print(result)







'''
Convert List of Key-Value Pairs into Grouped Dictionary

Task: Ek pairs ki list ko dictionary mein convert karna hai, lekin agar koi key repeat 
ho rahi hai toh uski maximum value save honi chahiye.

Input: pairs = [('a', 10), ('b', 20), ('a', 50), ('b', 15)]

Expected Output: {'a': 50, 'b': 20}

'''

# def convert_list_of_key_value_pairs_into_grouped(l):
#    res={}
#    for key,value in l:
#       if key in res:
#          if value>res[key]:
#             res[key]=value
#       else:
#          res[key]=value

#    return res


# user=eval(input("enter your list"))
# result=convert_list_of_key_value_pairs_into_grouped(user)
# print(result)








'''
Filter Dictionary by Value Datatype

Task: Ek mixed data wali dictionary se sirf wahi keys aur values filter
 karni hain jinki value strictly ek Integer hai.

Input: d = {"name": "Maaz", "age": 21, "city": "Bhopal", "roll": 105}

Expected Output: {"age": 21, "roll": 105}

'''

# def filter_int_value(d):
#     res={ i:d[i] for i in d if type(d[i])==int}
#     return res


# user=eval(input("enter your list"))
# result=filter_int_value(user)
# print(result)








'''

ASCII Value Mapping

Task: Ek string ke unique characters ko key banana hai aur unki ASCII 
value (Python ka ord() function use karke) ko value banana hai.

Input: s = "abc"

Expected Output: {'a': 97, 'b': 98, 'c': 99}
'''

# def ascii_value_mapping(s):
#     res={}
#     for i in s:
#         ascii_value=ord(i)
#         res[i]=ascii_value
#     return res


# user=input("enter your word")
# result=ascii_value_mapping(user)
# print(result)








'''
Nested Dict to Flat Dict with Custom Separator

Task: 2-level nested dictionary ko flat dictionary mein 
convert karna hai jahan new key dono keys ko hyphen (-) se jod kar bane.

Input: d = {"rits": {"cse": 120, "it": 60}}

Expected Output: {"rits-cse": 120, "rits-it": 60}

'''

# def nested_dict_to_flateen(d,parent_key=''):
#     res={}
#     for i in d:
#         value=d[i]
#         if parent_key!='':
#             new_key=parent_key+'-'+i
#         else:
#             new_key=i
#         if type(value)==dict:
#             subdict=nested_dict_to_flateen(value,new_key)
#             for key in subdict:
#                 res[key]=subdict[key]
#         else:
#             res[new_key]=value
#     return res


# user=eval(input("enter your dict"))
# result=nested_dict_to_flateen(user)
# print(result)







'''
Invert Dictionary with List Values (Explode Logic)

Task: Agar kisi key ki value ek list hai, toh use explode karke ulta
 karna hai taaki list ka har element alag key ban jaye.

Input: d = {"fruits": ["apple", "banana"]}

Expected Output: {"apple": "fruits", "banana": "fruits"}

'''

# def explode_list_element_with_key(d):
#     res={}
#     for i in d:
#         value=d[i]
#         if type(value)==list:
#             for j in value:
#                 res[j]=i
#     return res


# user=eval(input("enter your list"))
# result=explode_list_element_with_key(user)
# print(result)






'''
Sentence Word-Length Dictionary

Task: Ek sentence ko tod kar (split karke) uske
 har word ko key banana hai aur us word ki string length ko value.

Input: text = "Django is awesome"

Expected Output: {"Django": 6, "is": 2, "awesome": 7}

'''
# def sentence_word_length_dictionary(s):
#     word=s.split()
#     res={}
#     for i in word:
#         res[i]=len(i)
#     return res



# user=input("enter your word")
# result=sentence_word_length_dictionary(user)
# print(result)







'''
Filter Dictionary items with Keys containing specific Character

Task: Dict se un entries ko filter karo jinki key ke andar letter 'a' aata ho.

Input: d = {"maaz": 95, "rohit": 80, "amit": 85, "vikas": 70}

Expected Output: {"maaz": 95, "amit": 85, "vikas": 70}

'''

# def filter_key_with_a(d):
#     res={ key:d[key] for key in d if 'a' in key}
#     return res


# user=eval(input("enter your dict"))
# result=filter_key_with_a(user)
# print(result)







'''
Reverse Both Keys and String Values

Task: Ek dictionary ki keys aur string values dono ko ulta (reverse) karke nayi dict banani hai.

Input: d = {"py": "code", "dj": "web"}

Expected Output: {"yp": "edoc", "jd": "bew"}

'''


# def reverse_key_value(d):
#     res={}
#     for i in d:
#         key=i[::-1]
#         value=d[i][::-1]
#         res[key]=value

#     return res

# user=eval(input("enter your dict"))
# result=reverse_key_value(user)
# print(result)






'''

Categorize Numbers into Even/Odd Keys

Task: Ek numbers ki list se ek dictionary banani hai jahan numbers khud keys hon 
aur value mein "Even" ya "Odd" string likhi ho.

Input: nums = [4, 7, 10]

Expected Output: {4: "Even", 7: "Odd", 10: "Even"}

'''

# def categrorize_even_odd_value_dict(l):
#     res={}
#     for i in l:
#        if i%2==0:
#            res[i]='Even'
#        else:
#            res[i]='Odd'
#     return res


# user=eval(input("enter your list"))
# result=categrorize_even_odd_value_dict(user)
# print(result)







'''
Clean Dictionary from Empty Strings and None

Task: Ek dictionary ko sanitize karna hai—yaani agar kisi key ki value None ho ya 
khaali string "" ho, toh use remove kar dena hai.

Input: data = {"user": "Maaz", "email": "", "phone": None, "status": "active"}

Expected Output: {"user": "Maaz", "status": "active"}

'''
# def filter_dict(d):
#     res = {}
#     for i in d:
#         # 1. Pehle check kiya None na ho
#         if d[i] is not None:
#             # 2. Agar string hai, toh khali/spaces wali string filter karo
#             if isinstance(d[i], str):
#                 if d[i].strip():  # Khali string "" ya spaces "  " par False dega
#                     res[i] = d[i]
#             # 3. Agar string ke ilawa kuch aur hai (int, bool, etc.), toh direct include kar lo
#             else:
#                 res[i] = d[i]
                
#     return res

# user = {"user": "Maaz", "age": 21, "email": "  ", "phone": None}
# result = filter_dict(user)
# print(result)
