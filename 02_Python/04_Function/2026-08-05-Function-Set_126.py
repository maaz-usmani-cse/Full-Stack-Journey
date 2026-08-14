'''
Check karo ki kya koi word number par khatam ho raha hai.
Input: ["apple", "banana1", "cherry"] $\rightarrow$ Output: True

'''

# def is_end_digit(l):
#     return any(i[-1].isdigit() for i in l)


# user=eval(input("enter your list"))
# result=is_end_digit(user)
# print(result)





'''
Sentence me check karo ki kya isme koi space (" ") hai.Input: "HelloWorld" $\rightarrow$ Output: False
'''

# def is_space(s):
#     return any(i==' ' for i in s)


# user=input('enter your word')
# result=is_space(user)
# print(result)







'''

List me check karo ki kya koi value Float (decimal number) hai.Input: [1, 2, 3.5, 4] $\rightarrow$ Output: True
'''

# def is_float(l):
#     return any(isinstance(i,float) for i in l)


# user=eval(input("enter your list"))
# result=is_float(user)
# print(result)







# 'zigzag patter'
# def zigzag_pattern(l):
#     for i in range(len(l) - 1):

#         if i % 2 == 0:
#             if l[i] > l[i+1]: 
#                 temp = l[i]
#                 l[i] = l[i+1]
#                 l[i+1] = temp

       
#         else:
#             if l[i] < l[i+1]: 
#                 temp = l[i]
#                 l[i] = l[i+1]
#                 l[i+1] = temp

#     return l


# user = eval(input("enter your list: "))
# result = zigzag_pattern(user)
# print(result)









'''
Words ki list se ek dictionary banao jisme Key word ka pehla character ho aur Value un words ki list ho.

Input: words = ["apple", "banana", "avocado", "cat", "bat"]

Expected Output: {'a': ['apple', 'avocado'], 'b': ['banana', 'bat'], 'c': ['cat']}

'''
# def fisrt_word_key(l):
#     d={}
#     for i in l:
#        fisrt=i[0]
#        if fisrt not in d:
#            d[fisrt]=[]
#        d[fisrt].append(i)

#     return d


# user=eval(input('enter your list'))
# result=fisrt_word_key(user)
# print(result)

