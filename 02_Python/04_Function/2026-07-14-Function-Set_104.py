'''
Matrix Transpose (Row to Column Swap)Task: List comprehension ka use karke ek
 $2 \times 3$ matrix ko transpose ($3 \times 2$) mein badalna hai 
(rows ko columns banana hai).Input: matrix = [[1, 2, 3], [4, 5, 6]]Expected Output:
 [[1, 4], [2, 5], [3, 6]]

'''
# def create_matrix(l):
#     res=[[l[i][j]for i in range(len(l))]  for j in range(len(l[0]))]
#     return res


# user=eval(input("enter your list"))
# result=create_matrix(user)
# print((result))









'''
Filter Anagrams of a Word

Task: Words ki list se sirf un words ko filter karna hai jo string "abc" ke anagrams hain 
(yaani akshar aage-piche ho sakte hain par exactly wahi hone chahiye).

Input: words = ["cab", "bca", "xyz", "bac", "apple"]

Expected Output: ["cab", "bca", "bac"]

'''


# def anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     d1={}
#     d2={}
#     for i in s1:
#         if i in d1:
#             d1[i]=d1[i]+1
#         else:
#             d1[i]=1
#     for j in s2:
#         if j in d2:
#             d2[j]=d2[j]+1
#         else:
#             d2[j]=1
#     if d1!=d2:
#         return False
#     return True


# def filter_angram_word(l,target_word):
#     res=[]
#     for i in l:
#         if anagram(target_word,i):
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# target_word=input("enter your word")
# result=filter_angram_word(user,target_word)
# print(result)









'check anagram'

# def anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return 'anagram nahi ho skta'
#     d1={}
#     d2={}
#     for i in s1:
#         if i in d1:
#             d1[i]=d1[i]+1
#         else:
#             d1[i]=1
#     for j in s2:
#         if j in d2:
#             d2[j]=d2[j]+1
#         else:
#             d2[j]=1
#     if d1!=d2:
#         return False
#     return True

# s1=input('enter your word')
# s2=input("enter your word")  
# result=anagram(s1,s2)  
# print(result)









'''
Extract Digits from Alpha-Numeric Strings

Task: Mix character aur numbers wali list ke har element se sirf digits (numbers) nikal kar unhe integers banana hai.

Input: data = ["m44z", "p3th0n", "cs101"]

Expected Output: [44, 30, 101] (Hint: .isdigit() ya .join() che

'''

# def extract_digit_from_alphanumberic(l):
#     res=[]
#     has_digit=False
#     for i in l:
#         has_digit=False
#         num=0
#         for j in i:
#             if j.isdigit():
#                 num=num*10+int(j)
#                 has_digit=True
#         if has_digit:
#             res.append(num)
#     return res


# user=eval(input('enter your list'))
# result=extract_digit_from_alphanumberic(user)
# print(result)

        
    



'''
Running Difference / Cumulative Subtraction

Task: enumerate() ka use karke ek nayi list banani hai jahan har element apne pichle element se subtract ho (index 0 ko chhor kar).

Input: nums = [10, 25, 40, 55]

Expected Output: [15, 15, 15] (Kyunki 25-10=15, 40-25=15...)
'''

# def running_diffrence(l):
#     res=[]
#     for i ,value in enumerate(l):
#         if i>0:
#             diff=value-l[i-1]
#             res.append(diff)
#     return res

# user=eval(input("enter your list"))
# result=running_diffrence(user)
# print(result)