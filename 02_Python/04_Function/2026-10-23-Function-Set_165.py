'''
Palindrome Check
Question: Ek string ya number palindrome hai ya nahi, yeh check karne ke liye function likho.
'''
# def is_pallindrom(s):
#     res=''
#     for i in range(len(s)):
#         res=s[i]+res
#     if res==s:
#         return 'palindrom'
#     return 'not pallindrom'

# user=input("enter your text")
# result=is_pallindrom(user)
# print(result)


'factorial'

# def factorial(n):
#     res=1
#     for i in range(1,n+1):
#         res=res*i
#     return res

# user=int(input("enter your number"))
# result=factorial(user)
# print(result)

'n terms tak Fibonacci sequence generate karne ke liye function likho.'
# def fibonacci_series(n):
#     n1=01
#     n2=1
#     for i in range(n):
#         add=n1+n2
#         print(n1,end=' ')

#         n1=n2
#         n2=add


# fibonacci_series(5)


'Find the Largest/Smallest Element in a List'
# def is_largest_and_smallest(l):
#     largest=None
#     smallest=None
#     for i in l:
#         if largest is None or i>largest:
#             largest=i
#         if smallest is None or i<smallest:
#             smallest=i
#     return f"larget is {largest} and smalles is {smallest}"

# user=eval(input("enter your list"))
# result=is_largest_and_smallest(user)
# print(result)


'''
Count Vowels in a String
Question: Ek string mein total vowels (a, e, i, o, u) kitne hain, yeh count karne ka function likho.
'''
# def count_vowels(s):
#     total_vowels=0
#     vowels={"a":True,"e":True,'i':True,'o':True,'u':True,'A':True,'E':True,'I':True,'O':True,'U':True}
#     for i in s:
#         if i in vowels:
#             total_vowels+=1
#     return f'total vowels are {total_vowels}'

# user=input("enter your word")
# result=count_vowels(user)
# print(result)


'''
Remove Duplicates from a List
Question: Ek list se duplicate elements hata kar unique elements ki list return karo.
'''
# def remove_dublicate(l):
#     res=[]
#     for i in l:
#         if i not in res:
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# result=remove_dublicate(user)
# print(result)


'Check for Prime Number'
# def is_prime(n):
#     if n==0 or n==1:
#         return False
#     elif n==2:
#         return True

#     elif n%2==0:
#        return  False

#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return False
#     return True



# user = int(input('enter your number: '))
# result = is_prime(user)
# print('Result:', result)  # Yahan 'Result:' likh dega toh dikhega
# print('-' * 20)  # Ek line aa jayegi beech mein


'''
List ya string mein har element kitni baar aaya hai (frequency count), uska function likho.
'''
# def check_frequency_count(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d

# user=input("enter your word")
# result=check_frequency_count(user)
# print(result)


'''
Do strings anagram hain ya nahi (matlab same characters se bani hain), yeh check karo.
Python
'''
# def is_anagram(s1,s2):
#     s1=s1.replace(' ','').lower()
#     s2=s2.replace(' ','').lower()
#     if len(s1)!=len(s2):
#         return False
#     d1={}
#     d2={}
#     for i in s1:
#         if i in d1:
#             d1[i]=d1[i]+1
#         else:
#             d1[i]=1
        
#     for i in s2:
#         if i in d2:
#             d2[i]=d2[i]+1
#         else:
#             d2[i]=1

#     if d1==d2:
#         return True
#     return False

        

# s1=input("enter your word")
# s2=input("enter your word")
# result=is_anagram(s1,s2)
# print(result)