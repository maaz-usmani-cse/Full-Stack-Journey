'''
Filter even numbers from a list.
Input: [1, 2, 3, 4, 5, 6] → Output: [2, 4, 6]
'''
# a=[1, 2, 3, 4, 5, 6] 
# result=filter(lambda x: x%2==0 ,a)
# print(list(result))


'''
Filter odd numbers from a list.
Input: [10, 15, 20, 25, 30] → Output: [15, 25]

'''
# a= [10, 15, 20, 25, 30] 
# result=filter(lambda x: x%2!=0 ,a)
# print(list(result))


'''
# Filter numbers greater than 50.
# Input: [10, 60, 45, 70, 30] → Output: [60, 70]
# '''
# a=[10, 60, 45, 70, 30]
# result=filter(lambda x: x>50 , a)
# print(list(result))


'''
Filter strings with length greater than and = 4.
Input: ["apple", "bat", "ball", "hi"] → Output: ["apple", "ball"]

'''
# a= ["apple", "bat", "ball", "hi"]
# result=filter(lambda x: len(x)>=4 , a)
# print(list(result))


'''
Filter positive numbers.
Input: [-2, 0, 5, 9, -7, 3] → Output: [5, 9, 3]
'''
# a= [-2, 0, 5, 9, -7, 3]
# result=filter(lambda x: x>0 , a)
# print(list(result))


'''
Filter words that start with the letter 'a'.
Input: ["apple", "banana", "avocado", "cherry"] → Output: ["apple", "avocado"]

'''
# a= ["apple", "banana", "avocado", "cherry"]
# result=filter(lambda x: x[0]=="a" ,a)
# print(list(result))


'''
Filter palindrome words.
Input: ["madam", "python", "level", "wow", "cat"] → Output: ["madam", "level", "wow"]
'''
# a=["madam", "python", "level", "wow", "cat"] 
# result=filter(lambda x: x[::-1]==x , a)
# print(list(result))



'''
Filter vowels from a list of characters.
Input: ['a', 'b', 'e', 'i', 'o', 'p', 'u'] → Output: ['a', 'e', 'i', 'o', 'u']
'''
# a=['a', 'b', 'e', 'i', 'o', 'p', 'u']
# result=filter(lambda x: x in ["a","e","i","o","u"] ,a)
# print(list(result))


'''
 Filter numbers divisible by both 3 and 5.
Input: [10, 15, 30, 42, 60, 70] → Output: [15, 30, 60]
'''
# a= [10, 15, 30, 42, 60, 70]
# result=filter(lambda x: x%3==0 and x%5==0 ,a)
# print(list(result))



'''
 Filter names that contain the letter 'a' or 'A'.
Input: ["Rahul", "Raj", "Python", "Code"] → Output: ["Rahul", "Raj"]
+
'''
# a=["Rahul", "Raj", "Python", "Code"]
# result=filter(lambda x: "a" in x, a)
# print(list(result))



'''
 Filter numbers whose square is greater than 50.
Input: [2, 4, 6, 8, 10] → Output: [8, 10]
'''
# a=[2, 4, 6, 8, 10]
# result= filter(lambda x: x**2>50 , a)
# print(list(result))



'''
Filter words ending with 'ing'.
Input: ["running", "play", "eating", "dance"] → Output: ["running", "eating"]

'''
# a=["running", "play", "eating", "dance"]
# result=filter(lambda x: x[-3:]=="ing",a)
# print(list(result))



'''
1 Filter elements that are strings from a mixed list.
Input: [1, "apple", 3.5, "banana", True, "cherry"] → Output: ["apple", "banana", "cherry"]
'''
# a=[1, "apple", 3.5, "banana", True, "cherry"] 
# result=filter(lambda x: type(x)==str, a)
# print(list(result))


'''
1 Filter employees older than 25 from a list of tuples (name, age).
Input: [("Rohit", 22), ("Rahul", 26), ("Raj", 30)]
Output: [("Rahul", 26), ("Raj", 30)]
'''

# a=[("Rohit", 22), ("Rahul", 26), ("Raj", 30)]
# result=filter(lambda x: x[1]>25, a)
# print(list(result))
