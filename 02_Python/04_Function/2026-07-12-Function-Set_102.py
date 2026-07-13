
'late winding concept'
# funcs = [lambda x: x * i for i in range(3)]
# print(funcs[0](5))



'''
Ek words ki list di gayi hai. Har word mein kitne vowels (a, e, i, o, u) hain, 
unka count nikal kar nayi list banani hai.

Input: words = ["apple", "banana", "sky"]

Expected Output: [2, 3, 0]

# '''
# def count_vowels_in_word(l):
#    d={'a':True,'e':True,'i':True,'o':True,'u':True}
#    res=[]
#    for i in l:
#       count=0
#       for j in i:
#          if j in d:
#             count=count+1
#       if count>0:
#          res.append(count)
#    return res


# user=eval(input('enter your list'))
# res=count_vowels_in_word(user)
# print(res)         




'''
Flattening a 2D Matrix (List)

Task: Ek 2D matrix ko single flat list mein convert karna hai.

Input: matrix = [[1, 2], [3, 4], [5, 6]]

Expected Output: [1, 2, 3, 4, 5, 6]
'''

# def convert_single_flat_matrix(l):
#     res=[j for i in l for j in i]
#     return res


# user=eval(input("enter your list"))
# result=convert_single_flat_matrix(user)
# print(result)





'''
Common Elements between Three Lists

Task: Teen lists mein se common elements nikalne hain. (Dhyan rahe, lookup fast hona chahiye!).

Input: l1 = [1, 2, 3], l2 = [2, 3, 4], l3 = [3, 4, 5]

Expected Output: [3]

'''

# def find_common_element(l1,l2,l3):
#     res=[]
#     d1={}
#     d2={}
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
# result=find_common_element(l1,l2,l3)
# print(result)





'''
enumrate() k sath sirf Even Indices par baithe numbers ko unke index se multiply karna hai, aur baaki ko ignore karna hai.

Input: nums = [10, 20, 30, 40, 50]

Expected Output: [0, 60, 200] (Kyunki index 010=0, index 230=60, index 450=200)*
'''


# def multiply_even_indices(l):
#     res=[]
#     for index,value in enumerate(l):
#         if index%2==0:
#             res.append(value*index)
#     return res

# user=eval(input("enter your list"))
# result=multiply_even_indices(user)
# print(result)

  

'''

Filter Strings by Length

Task: Sirf un strings ko filter karna hai jinki length 4 se badi ho.

Input: items = ["hi", "maaz", "python", "code"]

Expected Output: ["python"]
'''

# def filter_string(l):
#     res=[i for i in l if len(i)>4]
#     return res

# user=eval(input("enter your list"))
# result=filter_string(user)
# print(result)






'''
Ek numbers ki list se sirf Prime Numbers (abhibhajya sankhya) ko filter karna hai.

Input: nums = [2, 4, 7, 9, 11, 15]

Expected Output: [2, 7, 11]
'''

# def is_prime(n):
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     if n%2==0:
#         return False
#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return False
        
#     return True

# def filter_prime_numbers(l):
#     res=[]
#     for i in l:
#         if is_prime(i):
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# result=filter_prime_numbers(user)
# print(result)









'''
Square of Evens, Cube of Odds

Task: if-else ka combo lagakar Even number ka square aur Odd number ka cube karna hai.

Input: arr = [1, 2, 3, 4]

Expected Output: [1, 4, 27, 16]

'''
# def even_square_odd_cube(l):
#     res=[i**2 if i%2==0 else i**3 for i in l]
#     return res

# user=eval(input("enter your list"))
# result=even_square_odd_cube(user)
# print(result)







'''
Extract Extensions from File Names

Task: Files ki list se unki formats/extensions (.py, .txt etc.) nikalni hain.

Input: files = ["main.py", "resume.pdf", "notes.txt"]

Expected Output: ["py", "pdf", "txt"]

'''
# def extract_extenshion_from_file(l):
#    res=[]
#    for i in l:
#       extenshion=i.split('.')
#       res.append(extenshion[1])
#    return res

# user=eval(input("enter yoour list"))
# result=extract_extenshion_from_file(user)
# print(result)






'''
Drop Negative Numbers with Condition

Task: Agar number negative hai toh use drop kar do, aur positive hai toh double kar do.

Input: data = [-1, 2, -3, 4]

Expected Output: [4, 8]

'''
# def drop_negative_multiply_possitive(l):
#     res=[]
#     for i in l:
#         if i>0:
#             res.append(i**2)
#     return res

# user=eval(input("enter your list"))
# result=drop_negative_multiply_possitive(user)
# print(result)






'''
Create Tuples of Index and Value

Task: Ek list se (index, value) ke tuples ki nayi list banani hai.

Input: chars = ['a', 'b', 'c']

Expected Output: [(0, 'a'), (1, 'b'), (2, 'c')]
'''

# def Create_Tuple_of_index_value(l):
#     res=[(i,l[i])for i in range(len(l))]
#     return res

# user=eval(input("enter your list"))
# result=Create_Tuple_of_index_value(user)
# print(result)
    






'''
Dictionary Comprehension Elite (Questions 11 to 20)
Q11. Length-Based Word Mapping

Task: List ke words ko key banana hai aur unki length ko value.

Input: words = ["django", "html", "css"]

Expected Output: {"django": 6, "html": 4, "css": 3}

'''
# def word_key_length_value(l):
#     res={i:len(i) for i in l}
#     return res

# user=eval(input("enter your list"))
# result=word_key_length_value(user)
# print(result)







'''
Dictionary mein se sirf un students ko filter karna hai jinke marks 50 ya 50 se zyada hain.

Input: scores = {"Maaz": 95, "Amit": 45, "Rohit": 82}

Expected Output: {"Maaz": 95, "Rohit": 82}

'''

# def filter_basis_of_marks(d):
#     res={i:d[i] for i in d if d[i]>=50}
#     return res

# user=eval(input("enter your list"))
# result=filter_basis_of_marks(user)
# print(result)





'''
Invert a Dictionary (Unique Values)

Task: Ek dictionary ke keys aur values ko aapas mein swap (ulta) karna hai.

Input: d = {"a": 1, "b": 2, "c": 3}

Expected Output: {1: "a", 2: "b", 3: "c"}
'''

# def swap_keys_values(d):
#     res={}
#     for i in d:
#         value=d[i]
#         res[value]=i
#     return res

# user=eval(input("enter your dict"))
# result=swap_keys_values(user)
# print(result)




