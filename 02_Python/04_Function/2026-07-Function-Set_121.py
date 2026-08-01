'Find the Kth largest element in an array.'
# def find_kth_largest(l,k):
#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i>pivot:
#             left.append(i)
#         elif i==pivot:
#             middle.append(i)
#         else:
#             right.append(i)
#     if k<=len(left):
#         return find_kth_largest(left,k)

#     elif k<=len(left)+len(middle):
#         return pivot

#     else:
#         return find_kth_largest(right,k-(len(left) + len(middle)))



# user=eval(input("enter your list"))
# target=int(input("enter your target"))
# result=find_kth_largest(user,target)
# print(result)  







'Removeduplicates from an array.'
# def remove_dublicate(l):
#    res=[]
#    for i in l:
#       if i not in res:
#          res.append(i)
#    return res


# user=eval(input("enter your list"))
# result=remove_dublicate(user)
# print(result)









'Write a program to reverse an array dont useextra varibale.'

# def reverse_list(l):
#     for i in range(len(l)//2):
#         temp=l[i]
#         l[i]=l[len(l)-1-i]
#         l[len(l)-1-i]=temp
#     return l


# user=eval(input("enter your list"))
# result=reverse_list(user)
# print(result)





'. Write a program to find theintersection of two arrays.'

# def intersection_of_2(l1,l2):
#     d={}
#     res=[]
#     for i in l1:
#         d[i]=True
#     for j in l2:
#         if j in d:
#             res.append(j)
#             del d[j]

#     return res


# l1=eval(input("enter your list"))
# l2=eval(input("enter your list"))
# result=intersection_of_2(l1,l2)
# print(result)






'''
: 1 से 10 तक की संख्याओं की लिस्ट बनाएं, जिसमें Even संख्याएँ वैसी ही रहें लेकिन Odd संख्याओं की जगह "Odd" लिखा आए। 
Expected Output: ['Odd', 2, 'Odd', 4, 'Odd', 6, 'Odd', 8, 'Odd', 10]

'''

# def create_even_odd_list():
#     return[i if i%2==0 else "ODD" for i in range(1,11)]



# result=create_even_odd_list()
# print(result)






'''
Matrix Transpose
Task: 3x3 मैट्रिक्स का ट्रांसपोज (Rows को Columns में बदलना) निकालें।

Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Expected Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

'''

# def transpose_matrix(l):
#     return[[row[j] for row in l] for j in range(len(l[0])) ]


# user=eval(input("enter your list"))
# result=transpose_matrix(user)
# print(result)






'''
Prime Numbers in a Range
Task: List Comprehension (और inner all/any logic) की मदद से 2 से 50 के बीच की (Prime) संख्याएँ निकालें।

Expected Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

'''






'''
Word Length Pair
Task: एक वाक्य के सभी शब्दों और उनकी लंबाई का tuple जोड़ा (word, length) बनाएं।

Input: "Code in Python"

Expected Output: [('Code', 4), ('in', 2), ('Python', 6)]


'''

# def lenth_word_in_tule(s):
#     return [(i,len(i)) for i in s.split()]


# user=input("enter your list")
# result=lenth_word_in_tule(user)
# print(result)