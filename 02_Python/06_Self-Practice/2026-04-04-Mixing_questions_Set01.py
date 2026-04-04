'''
Convert a list of integers into their squares using map().
Input: [1, 2, 3, 4] → Output: [1, 4, 9, 16]


'''

# a=[1, 2, 3, 4]
# result=map(lambda x: x**2 ,a)
# print(list(result))






'''
Convert all strings in a list to uppercase using map().
Input: ["python", "map", "function"] → Output: ["PYTHON", "MAP", "FUNCTION"]

'''


# a=["python", "map", "function"]
# result=map(lambda x: x.upper() , a)
# print(list(result))




'''

Convert a list of integers to strings using map().
Input: [1, 2, 3] → Output: ["1", "2", "3"]

'''


# a=[1, 2, 3]

# result=map(lambda x: str(x) ,a)
# print(list(result))




'''
Find the length of each word in a list using map().
Input: ["apple", "banana", "kiwi"] → Output: [5, 6, 4]


'''
# a= ["apple", "banana", "kiwi"] 
# result=map(lambda x: len(x), a)
# print(list(result))




'''
Double all numbers in a list using map().
Input: [3, 6, 9] → Output: [6, 12, 18]

'''
# a=[3, 6, 9]
# result=map(lambda x: x*2 , a)
# print(list(result))




'''
Add 10 to every number in a list using map().
Input: [1, 2, 3] → Output: [11, 12, 13]

'''

# a=[1, 2, 3]
# result=map(lambda x: x+10, a)
# print(list(result))




'''
Extract the first character of each word using map().
Input: ["apple", "banana", "cherry"] → Output: ["a", "b", "c"]

'''
# a=["apple", "banana", "cherry"]
# result=map(lambda x: x[0] , a)
# print(list(result))



'''
Check if each number in a list is even or odd using map().
Input: [1, 2, 3, 4] → Output: ["Odd", "Even", "Odd", "Even"]

# '''
# a=[1, 2, 3, 4]
# result=map(lambda x: "even" if x%2==0 else "odd" ,a)
# print(list(result))



'''

Combine two lists element-wise by summing them using map().
Input: [1, 2, 3], [4, 5, 6] → Output: [5, 7, 9]

'''
# a= [1, 2, 3]
# b= [4, 5, 6] 
# result=map(lambda x,y: x+y ,a,b)
# print(list(result))



'''

Capitalize the first letter of each name in a list using map().
Input: ["maaz", "wohit", "python"] → Output: ["Maaz", "Wohit", "Python"]

'''

# a=["maaz", "wohit", "python"]
# result=map(lambda x: x[0].upper()+x[1:],a)
# print(list(result))


'''    

Remove spaces from each string using map().
Input: ["a p p l e", "b a n a n a"] → Output: ["apple", "banana"]
'''
# def remove_space(n):
#     word=''
#     for i in n:
#         if i!=' ':
#             word=word+i
#     return word

# a=["a p p l e", "b a n a n a"] 
# result=map(remove_space,a)
# print(list(result))



'''

14. Given a list of numbers, return their cubes if they are even, else square them using map().
Input: [1, 2, 3, 4] → Output: [1, 8, 9, 64]

'''

# a=[1, 2, 3, 4]
# result=map(lambda x: x**3 if x%2==0 else x*2 ,a)
# print(list(result))




'''

Convert a list of tuples (name, age) into formatted strings using map().
Input: [("Raj", 22), ("rahul", 21)]
Output: ["Raj is 22 years old", " rahul is 21 years old"]

'''

# a=[("Raj", 22), ("rahul", 21)]
# result=map(lambda x: x[0]+' '+"is"+' '+str(x[1])+' '+"years"+' '+"old",a)
# print(list(result))





'''
Find the sum of all numbers in a list using reduce().
Input: [1, 2, 3, 4, 5] → Output: 15 

'''
# from functools import reduce
# a=[1, 2, 3, 4, 5]
# result=reduce(lambda x,y:x+y , a)
# print(result)


'''

Find the product of all numbers in a list.
Input: [1, 2, 3, 4] → Output: 24
'''

# from functools import reduce
# a= [1, 2, 3, 4] 
# result=reduce(lambda x,y: x*y , a)
# print(result)


# a=[1,0,1,0,2,0,3]
# zero=list(filter(lambda x: x==0 ,a))
# nonzero=list(filter(lambda x: x!=0 ,a))
# result=zero+nonzero
# print(result)







