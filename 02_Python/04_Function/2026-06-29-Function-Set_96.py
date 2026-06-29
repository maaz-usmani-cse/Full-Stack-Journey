'''

String ke Substrings check karna
Aapko sentences ki ek list di gayi hai:

sentences = ["Python is awesome", "Java is old", "I love Python programming", "C++ is fast"]

Task: List comprehension ka use karke sirf un sentences ko filter karna hai jismein 
"Python" shabd aata ho.

Expected Output: ["Python is awesome", "I love Python programming"]

'''

# def filter_python_word(l):
#     res=[i for i in l if 'python' in i.lower()]
#     return res

# user=eval(input("enter your list"))
# result=filter_python_word(user)
# print(result)







'''
Numbers ko unke Signs ke hisab se modify karna
Aapko ek list di gayi hai: numbers = [-5, 3, -2, 8, 0, -1, 4]

Task: List comprehension ka use karke ek nayi list banani hai. 
Agar number negative hai toh uski jagah 0 aana chahiye, aur agar positive 
ya zero hai toh number waisa ka waisa hi rehna chahiye.

Expected Output: [0, 3, 0, 8, 0, 0, 4]


'''

# def replace_zero(l):
#     res=[0 if i<0 else i for i in l]
#     return res

# user=eval(input("enter your list"))
# result=replace_zero(user)
# print(result)









'''
 Matrix ke Diagonal Elements nikalnaAapke paas ek $3 \times 3$ ki square matrix 
 (2D list) hai:Pythonmatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Task: range() aur list comprehension ka use karke is matrix ke primary diagonal elements 
(yaani 1, 5, 9) ko nikal kar ek nayi list banani hai.Expected Output: [1, 5, 9]

'''

# def primary_diaogonaly(l):
#     res=[l[i][i] for i in range(len(l))]
#     return res


# user=eval(input("enter your list"))
# result=primary_diaogonaly(user)
# print(result)
