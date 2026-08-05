'''
Find themaximum product of two elements in an array.

'''
# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
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

#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)



# def find_maximum_product(l):
#     res=quick_sort_pivot(l)

#     product1=res[0]*res[1]
#     product2=res[-1]*res[-2]

#     if product1>product2:
#        return f' maximum product is {product1}'

#     else:
#          return f' maximum product is {product2}'

   


# user=eval(input("enter your list"))
# result=find_maximum_product(user)
# print(result)





'Write a program to count the number of zeros in an array.'
# def count_zeroes(l):
#     zero_count=0
#     for i in l:
#         if i==0:
#             zero_count=zero_count+1
#     return zero_count


# user=eval(input('enter your list'))
# result=count_zeroes(user)
# print(result)





'Write a program to shift zeros in the last of the array.'

# def shift_zeroes_end(l):
#     index=0
#     for i in range(len(l)):
#         if l[i]!=0:
#             temp=l[index]
#             l[index]=l[i]
#             l[i]=temp
#             index=index+1







'. Writea function to calculate the factorial of a number.'

# def factorial(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial=factorial*i
#     return factorial


# user=int(input("enter your numbert"))
# result=factorial(user)
# print(result)




'Createa function to check whether a numberis primeornot.'

# def is_prime(n):
#     if n<=1:
#         return 'not prime'

#     elif n==2:
#         return 'prime'

#     elif n%2==0:
#         return 'not prime'

#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return 'not prime'

#     return 'prime'


# user=int(input("enter your numebr"))
# result=is_prime(user)
# print(result)






'Checkif a string is a palindrome.'

# def is_paliindrom(s):
#     if s==s[::-1]:
#         return 'pallindrom'
#     else:
#         return 'not pollindrom'


# user=input("enter your word")
# result=is_paliindrom(user)
# print(result)





'Countthenumberof vowelsand consonantsin a string'
# def count_consonant_vowels(s):
#     d={'a','e','i','o','u','A','E','I','O','U'}
#     vowels=0
#     consonant=0
#     for i in s:
#         if i.isalpha():
#             if i in d:
#                 vowels=vowels+1
#             else:
#                 consonant=consonant+1
#     return f' vowels: {vowels} consonant{consonant}'



# user=input('enter your word')
# result=count_consonant_vowels(user)
# print(result)





'Check if two strings are anagrams.'

# def angram(s1,s2):
#     if len(s1) != len(s2):
#         return 'angram nahi hai'
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

#     if d1 != d2:
#         return 'anagram nahi hai'

  
#     return 'anagram hai'


# s1=input("enter your word")
# s2=input('enter your word')
# result=angram(s1,s2)
# print(result)






'Write a program to find theHCF of two numbers.'
# def find_hcf_two_number(n1,n2):
#     while n2!=0:
#       temp=n1%n2
#       n1=n2
#       n2=temp

#     return n1

# n1=int(input("enter your nmber"))
# n2=int(input("enter your number"))
# result=find_hcf_two_number(n1,n2)
# print(result)





'List me check karo ki kya koi value Float (decimal number) hai.Input: [1, 2, 3.5, 4] $\rightarrow$ Output: True'


# def is_any_float_deciaml(l):
#     return any(isinstance(i,float) for i in l)


# user=eval(input("enter your list"))
# result=is_any_float_deciaml(user)
# print(result)





'''
Check karo ki kya koi word capital 'A' ya small 'a' se shuru hota hai.
Input: ["Cat", "Dog", "apple", "Ball"] $\rightarrow$ Output: True
'''

# def is_start_word_a_or_A(l):
#     return any(i.startswith(('a','A')) for i in l)


# user=eval(input("enter your list"))
# result=is_start_word_a_or_A(user)
# print(result)




