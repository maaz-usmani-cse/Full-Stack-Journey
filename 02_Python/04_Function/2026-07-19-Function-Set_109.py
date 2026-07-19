'''

Matrix Transpose with Single-Line Nested ComprehensionTask: 
Ek $3 \times 2$ matrix ko bina kisi loop block ke, pure nested list 
comprehension se $2 \times 3$ matrix (transpose) mein badalna hai.
Input: matrix = [[1, 2], [3, 4], [5, 6]]Expected Output: [[1, 3, 5], [2, 4, 6]]

'''

# def matrix_transpose(l):
#     res=[[l[row][col]for row  in range(len(l))] for col in range(len(l[0]))]
#     return res


# user=eval(input("enter your list"))
# result=matrix_transpose(user)
# print(result)








'''
Filter Palindrome Strings

Task: Strings ki list se sirf un strings ko filter karna hai jo ulte aur 
seedhe dono taraf se same padhi jaati hain (Palindromes).

Input: words = ["radar", "python", "level", "maaz", "madam"]

Expected Output: ["radar", "level", "madam"]

'''

# def filter_palindrom_word(l):
#     res=[]
#     for i in range(len(l)):
#         if l[i][::-1]==l[i]:
#             res.append(l[i])
#     return res


# user=eval(input("enter yoir list"))
# result=filter_palindrom_word(user)
# print(result)
            








'''
Remove Vowels from Sentences

Task: List comprehension ka use karke sentences ke andar 
se saare vowels (a, e, i, o, u) ko gayab (remove) karna hai.

Input: sentences = ["python is fun", "coding rules"]

Expected Output: ["pythn s fn", "cdng rls"]

'''
# def remove_vowels_clean(l):
#     res = []
#     for sentence in l:
#         sentence = sentence.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
#         sentence = sentence.replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')
#         res.append(sentence)
        
#     return res

# sentences = ["python is fun", "coding rules", "hello maaz"]
# print(remove_vowels_clean(sentences))








'''
Filter Indices of Non-Zero Elements

Task: enumerate() ka use karke list mein se sirf un elements ke indices
 ki list banani hai jo 0 ke barabar nahi hain.

Input: nums = [0, 5, 0, 12, 0, 0, 7]

Expected Output: [1, 3, 6]

'''

# def filter_Indices_of_Non_Zero_Elements(l):
#     res=[]
#     for indx,value in enumerate(l):
#         if value!=0:
#             res.append(indx)

#     return res


# user=eval(input("enter your list"))
# result=filter_Indices_of_Non_Zero_Elements(user)
# print(result)








'''
Extract Valid Email Domains

Task: Email strings ki list se sirf unke domains (jaise gmail.com) nikalne hain, 
lekin condition yeh hai ki email valid hona chahiye (yaani usmein @ hona zaroori hai).

Input: emails = ["maaz@gmail.com", "invalid-email", "rohit@yahoo.com"]

Expected Output: ["gmail.com", "yahoo.com"]

'''
# def extract_valid_email_domains(l):
#     res=[]
#     for i in l:
#         if '@' in i:
#             part=i.split('@')
#             res.append(part[1])
#     return res


# user=eval(input("enter your list"))
# result=extract_valid_email_domains(user)
# print(result)





'''

Tuples ki ek nested list di gayi hai. Har tuple ke andar ke elements ka 
sum (jod) nikal kar ek simple flat list banani hai.

Input: data = [(1, 2), (4, 5, 6), (7,)]

Expected Output: [3, 15, 7]

'''

# def sum_of_nested_tuples_list(l):
#     res=[]
#     for i in l:
#         total=0
#         for j in i:
#             total=total+j
#         res.append(total)
#     return res


# user=eval(input("enter your list"))
# result=sum_of_nested_tuples_list(user)
# print(result)





'''
Task: Agar string ki length odd (visham) hai toh use ulta (reverse) kar do, aur agar even (sam) hai toh waisa hi rehne do.

Input: words = ["abc", "code", "django", "hello"]

Expected Output: ["cba", "code", "django", "olleh"]

'''
# def reverse_odd_string(l):
#     res=[]
#     for i in l:
#         if len(i)%2!=0:

#             res.append(i[::-1])
#         else:
#             res.append(i)
#     return res



# user=eval(input("enter your list"))
# result=reverse_odd_string(user)
# print(result)






'''
Find Substrings of Specific Length

Task: Ek single string se list 
comprehension ka use karke saare possible 3-letter continuous substrings nikalne hain.

Input: s = "python"

Expected Output: ["pyt", "yth", "tho", "hon"]

'''

def substring(s):
    res=[s[i:i+3] for i in range(len(s)-2)]
    return res


user=input("enter your list")
result=substring(user)
print(result)    

