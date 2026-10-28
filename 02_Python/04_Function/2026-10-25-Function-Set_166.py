'Find the Second Largest Element'
# def second_larget(l):
#     first=None
#     second=None
#     for i in l:
#         if first is None or i>first:
#             second=first
#             first=i
#         elif i!=first and (second is None or i>second):
#             second=i

#     return f"second largest is {second}"

# user=eval(input("enter your list"))
# result=second_larget(user)
# print(result)


'Find Missing Number in 1 to N'
# def is_missing_number(l):
#     for i in range(1,len(l)+1):
#         if i not in l:
#             return f"misiing number is {i}"

# user=eval(input("enter your list"))
# result=is_missing_number(user)
# print(result)



'''
latten a Nested List
 Ek list ke andar doosri list di gayi hai (nested list), usko ek single flat list mein convert karo.
'''
# def flatteen_list(l):
#     res=[]
#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatteen_list(i))

#         else:
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# result=flatteen_list(user)
# print(result)



'reverse without extra variable'
# def reverse(s):
#     s=list(s)
#     for i in range(len(s)//2):
#         temp=s[i]
#         s[i]=s[~i]
#         s[~i]=temp
#     return ''.join(s)

# user=input("enter your word")
# result=reverse(user)
# print(result)
    



'Find the Longest Word in a Sentence'
# def find_largest_word(s):
#     s=s.split()
#     first=None
#     for i in s:
#         if first is None or i>first:
#             first=i

#     return f"longest word is {first}"

# user=input("enter your word")
# resut=find_largest_word(user)
# print(resut)
            

'Ek list di gayi hai numbers ki, recursion ka use karke uske saare elements ka total sum nikalna hai.'
# def total_sum(l):
#     if not l:
#         return 0
#     return l[0]+total_sum(l[1:])


# user=eval(input("enter your list"))
# result=total_sum(user)
# print(result)