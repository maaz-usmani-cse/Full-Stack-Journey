'''
Colors aur Sizes ki lists se saare possible combinations ke pairs generate karo.

Python
colors = ['Red', 'Blue']
sizes = ['S', 'M', 'L']
'''
# def combination_pairs(color,size):
#     return[(i,j)for i in color for j in size]

# color=eval(input('enter your list'))
# size=eval(input("enter your list"))
# result=combination_pairs(color, size)
# print(result)



'''
2 se 30 ke beech ke saare prime numbers list comprehension aur all() function se generate karo.
# '''
# def prime_limit_2_30():
#     return [ i  for i in range(2,31)  if all( i%j!=0 for j in range(2, int(i**0.5) +1 ) )]


# result=prime_limit_2_30()
# print(result)



'''
 Jab bhi do adjacent characters same milein, un dono ko hata do. Yeh tab tak karo jab tak koi adjacent duplicate na bache.
 Input: s = "abbaca"Expected Output: "ca" 
 (Explanation: 'bb' hataan 'aaca' 'aa' hata  'ca'
'''
# def delete_dublicate_adjacent(s):
#     l=[]
#     for i in s:
#         if l and l[-1]==i:
#             l.pop()
#         else:
#             l.append(i)

#     return l


# user=input('enter your word')
# result=delete_dublicate_adjacent(user)
# print(*result)




'''
Template string "Hello {NAME}, your OTP is {OTP}." mein placeholders ko actual values se replace karein.
'''
# def replace_word(s):
#     new_word= s.replace('{NAME}','maaz').replace('{OTP}','5555')
#     return new_word

# user=input('enter your word')
# result=replace_word(user)
# print(result)


