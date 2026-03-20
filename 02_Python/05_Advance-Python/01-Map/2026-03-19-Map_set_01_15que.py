'''
1. Convert a list of integers into their squares using map().
Input: [1, 2, 3, 4] → Output: [1, 4, 9, 16]
'''
# a=[1, 2, 3, 4]
# result=map(lambda x: x**2 ,a)
# print(list(result))



'''
2. Convert all strings in a list to uppercase using map().
Input: ["python", "map", "function"] → Output: ["PYTHON", "MAP", "FUNCTION"]

'''
# a=["python", "map", "function"]
# result=map(lambda x: x.upper(),a)
# print(list(result))



'''
3. Convert a list of integers to strings using map().
Input: [1, 2, 3] → Output: ["1", "2", "3"]
'''
# a= [1, 2, 3] 
# result=map(lambda x: str(x) ,a)
# print(list(result))




'''
4. Find the length of each word in a list using map().
Input: ["apple", "banana", "kiwi"] → Output: [5, 6, 4]
'''


# a=["apple", "banana", "kiwi"]
# result=map(lambda x: len(x) ,a)
# print(list(result))




'''
5. Double all numbers in a list using map().
Input: [3, 6, 9] → Output: [6, 12, 18]
'''
# a=[3, 6, 9] 
# result=map(lambda x: x*2 ,a)
# print(list(result))



'''
6. Add 10 to every number in a list using map().
Input: [1, 2, 3] → Output: [11, 12, 13]
'''
# a=[1, 2, 3]
# result=map(lambda x: x+10,a )
# print(list(result))


'''
8.Extract the first character of each word using map().
Input: ["apple", "banana", "cherry"] → Output: ["a", "b", "c"]

'''

# a= ["apple", "banana", "cherry"]
# result=map(lambda x: x[0] ,a)
# print(list(result))



'''
9. Check if each number in a list is even or odd using map().
Input: [1, 2, 3, 4] → Output: ["Odd", "Even", "Odd", "Even"]


'''

# a=[1, 2, 3, 4] 
# result=map(lambda x: "even" if x%2==0 else "odd"  ,a)
# print(list(result))


'''
# 10. Convert a list of binary strings to integers using map().
# Input: ["101", "111", "1001"] → Output: [5, 7, 9]


# '''

# a=["101", "111", "1001"]





'''
11. Combine two lists element-wise by summing them using map().
Input: [1, 2, 3], [4, 5, 6] → Output: [5, 7, 9]


'''

# a=[1, 2, 3]
# b=[4,5,6]
# c=[7,8,9]
# result=map(lambda x1,x2,x3: x1+x2+x3 ,a,b,c)
# print(list(result))



'''
12. Capitalize the first letter of each name in a list using map().
Input: ["raj", "wohit", "python"] → Output: ["Mahesh", "Soni", "Python"]
'''


# a=["maaz", "usmnai", "python"]
# result=map(lambda x: x.capitalize() , a)
# print(list(result))


'''
13. Remove spaces from each string using map().
Input: ["a p p l e", "b a n a n a"] → Output: ["apple", "banana"]

'''

# a=["a p p l e", "b a n a n a"] 
# result=map(lambda x: x.replace(" ",''),a)
# print(list(result))



'''

Given a list of numbers, return their cubes if they are even, else square them using map().
Input: [1, 2, 3, 4] → Output: [1, 8, 9, 64]
'''

# a=[1, 2, 3, 4] 
# result=map(lambda x: x**3 ,a)
# print(list(result))


'''
15. Convert a list of tuples (name, age) into formatted strings using map().
Input: [("Raj", 22), ("rahul", 21)]
Output: ["Raj is 22 years old", " rahul is 21 years old"]

'''

# a=[("Raj", 22), ("rahul", 21)]
# result=map(lambda x: x[0] + ' '+"is"+' ' +str(x[1])+" "+"years old",a)
# print(list(result))


