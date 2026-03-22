'Ek function likho jo do numbers ka sum return kare.'

# def two_number_sum(n1,n2):
#     return n1+ n2


# user1=int(input("enter your number"))
# user2=int(input('enter your number'))
# result=two_number_sum(user1,user2)
# print(result)


'Ek function jo check kare ki number Even hai ya Odd.'
# def even_odd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"


# user=int(input("enter your number"))
# result=even_odd(user)
# print(result)


'Diye gaye number ka factorial nikalne ka recursive function likho.'
# def facttorial(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial=factorial*i
#     return factorial

# user=int(input('enter your number'))
# result=facttorial(user)
# print(result)


'Check karo ki koi number Prime hai ya nahi.'
# def prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 return "nahi hai"
#         else:
#             return "hai prime"
#     else:
#         return "prime nahi hai"
    
# user=int(input('enter your number'))
# result=prime(user)
# print(result)


'Ek function jo list ke saare numbers ka sum nikal sake.'
# def total_list(n):
#     total=0
#     for i in n:
#         total=total+i
#     return total

# user=eval(input("enter your number"))
# result=total_list(user)
# print(result)




'String ko reverse karne ka function likho (bina slicing ke).'
# def rev_string(n):
#     for i in range(len(n)-1,-1,-1):
#       print(n[i])


# user=input('enter your number')
# rev_string(user)


'Ek function jo check kare string Palindrome hai ya nahi.'
# def pallindrom(n):
#     rev=''
#     for i in n:
#         rev=i+rev
#     if rev==n:
#         return "poollindrom hai"
#     else:
#         return "nahi hai pollindrom"
    
# user=input("enter your number")
# result=pallindrom(user)
# print(result)


'List mein se maximum aur minimum number return karne wala function.'
# def minimum_maximum(n):
#     maximum=None
#     minimum=None
#     for i in n:
#         if maximum is None or i>maximum:
#             maximum=i
#         elif minimum is None or i<minimum:
#             minimum=i
#     return maximum ,minimum
   

# user=eval(input("enter your number"))
# result=minimum_maximum(user)
# print(result)


'Ek function jo count kare ki string mein kitne Vowels aur Consonants hain.'
# def string(n):
#     vowels=0
#     consonant=0
#     for i in n:
#         if i in ["a","e",'i',"o","u"]:
#             vowels=vowels+1
#         else:
#             consonant=consonant+1
#     return "vowels hai",vowels, 'consonant hai',consonant

# user=input("enter your number")
# result=string(user)
# print(result)



'List mein se duplicates hatane wala function likho.'
# def remove_dublicate(n):
#     l=[]
#     for i in n:
#         if i not in l:
#             l.append(i)
#     return l

# user=eval(input('enter your number'))
# result=remove_dublicate(user)
# print(result)



'*args ka use karke ek function banao jo kitne bhi numbers ka product nikal sake.'
# def multiply(*args):
#     result=1
#     for i in args:
#         result=result*i
#     return result
    
# result=multiply(2,2,2,2,2,2,2,2,2)
# print(result)


'List of strings mein se sabse lambi (longest) string dhundne wala function.'
# def string(n):
#     longest=''
#     for i in n:
#         if len(i)>len(longest):
#             longest=i
#     return longest

# a=["maaz","usmani"]
# result=string(a)
# print(result)



