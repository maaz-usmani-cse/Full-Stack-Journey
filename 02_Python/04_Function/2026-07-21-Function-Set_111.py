'''
Filter Words with Repeating Characters

Task: List comprehension ka use karke sirf un words ko filter karna hai jinke andar kam se kam ek character repeat ho raha ho.

Input: words = ["code", "hello", "python", "maaz", "world"]

Expected Output: ["hello", "maaz"] (Kyunki 'hello' mein 'l' aur 'maaz' mein 'a' repeat hai)

'''

# def filter_words_with_repeating_character(l):
#     res=[word for word in l if len(word)!=len(set(word))]
#     return res


# user=eval(input("entwr your list"))
# result=filter_words_with_repeating_character(user)
# print(result)
                   
        




'''
Run-Length Encoding Helper (Consecutive Same Elements Count)

Task: String ke har character ko uske consecutive count ke saath
 tuple ke roop mein nikalna hai (Bina internal loop ke standard list comprehension se).

Input: s = "aaabbc"

Expected Output: [('a', 3), ('b', 2), ('c', 1)]

'''


# def run_length_encoding(s):
#     current_char=s[0]
#     count=1
#     res=[]
#     for i in range(1,len(s)):
#         if s[i]==current_char:
#             count=count+1
#         else:
#             res.append((current_char,count))
#             current_char=s[i]
#             count=1
#     res.append((current_char,count))
#     return res


# user=input("enter your result")
# result=run_length_encoding(user)
# print(result)







'''

Task: Teen alag-alag same length ki lists ke parallel elements ko zip() 
karke unka addition (sum) nikal kar ek nayi list banani hai.

Input: a = [1, 2], b = [10, 20], c = [100, 200]

Expected Output: [111, 222]
'''

# def three_list_parellel_sum(l1,l2,l3):
#     res=[]
#     for i in range(len(l1)):
#         total=l1[i]+l2[i]+l3[i]
#         res.append(total)
#     return res


# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# l3=eval(input("enter your list"))
# result=three_list_parellel_sum(l1,l2,l3)
# print(result)









'''
Extract Multiples of Index Value

Task: enumerate() ka use karke sirf un elements ko filter karna hai jo apne 
Index Number se pura divide (divisible) ho jayein (Index 0 ko ignore kar dena).

Input: nums = [10, 5, 9, 11, 16]  (Indices: 0, 1, 2, 3, 4)

Expected Output: [5, 16] (Kyunki 5/1=5 aur 16/4=4)

'''
# def extract_multiples_of_index_value(l):
#    res=[]
#    for index,value in enumerate(l):
#       if index!=0:
#         if value%index==0:
#            res.append(value)
#    return res


# user=eval(input("enter your list"))
# result=extract_multiples_of_index_value(user)
# print(result)





'''
Flatten a 3D Matrix into 1D List

Task: Ek 3-level nested list ($3D$ matrix) ko pure single list comprehension se $1D$ flat list mein convert karna hai.

Input: matrix3d = [[[1, 2]], [[3, 4]], [[5, 6]]]

Expected Output: [1, 2, 3, 4, 5, 6]

'''

def flatten_a_3d_matrix_into_1D_list(matrix3d):
    flat_list = [val for level1 in matrix3d for level2 in level1 for val in level2]
    return flat_list


user=eval(input("enter your list"))
result=flatten_a_3d_matrix_into_1D_list(user)
print(result)