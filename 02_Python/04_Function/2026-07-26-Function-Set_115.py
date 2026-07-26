'''
Dictionary Filtering using External Set (Fast Lookup)

Task: Large dictionary se un keys ko filter karo jo ek allowed_set mein maujood hon.

Input: data = {"a": 1, "b": 2, "c": 3, "d": 4}, allowed = {"a", "c"}

Expected Output: {"a": 1, "c": 3}


'''

# def filter_dictionary(d):
#     allowed = {"a", "c"}
#     res={}
#     for i in d:
#         if i in allowed:
#             res[i]=d[i]
#     return res


# user=eval(input("enter your list"))
# result=filter_dictionary(user)
# print(result)
        





'''
Reverse Key String only if Value is Prime

Task: Dict mein agar value prime number hai toh key string ko reverse kar do, warna key waisi hi rehne do.

Input: d = {"code": 7, "data": 4, "user": 11}

Expected Output: {"edoc": 7, "data": 4, "resu": 11}

'''


# def is_prime(n):
#     if n<=1:
#         return False
#     elif n==2:
#         return True

#     elif n%2==0:
#         return False

#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return False
#     return True


# def is_value_prime_reverse_key(d):
#     res={}
#     for i in d:
#         if is_prime(d[i]):
#             res[i[::-1]]=d[i]
#         else:
#             res[i]=d[i]
#     return res

# user=eval(input("enter your list"))
# result=is_value_prime_reverse_key(user)
# print(result)










'''
xtract Duplicate Elements and their Frequency

Task: Ek numbers list se  un numbers ki frequency nikalni hai jo 1 se zyada baar repeat huye hain.

Input: nums = [1, 2, 2, 3, 4, 4, 4, 5]

Expected Output: {2: 2, 4: 3}
'''

# def dublicate_frequency(l):
#     d={}
#     res={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1

#     for j in d:
#         if d[j]>1:
#             res[j]=d[j]
#     return res


# user=eval(input("enter your list"))
# result=dublicate_frequency(user)
# print(result)
        





'''
Sentence ke har unique word ko Key banana hai aur us word ka sentence mein pehla index position Value banana hai.

Input: text = "python is fun and python is easy"

Expected Output: {"python": 0, "is": 1, "fun": 2, "and": 3, "easy": 6}

'''

# def unique_word_key(s):
#     res={}
#     l=s.split()
#     for i in range(len(l)):
#         if l[i] not in res:
#              res[l[i]]=i
#     return res

# user=input('enter your word')
# Result=unique_word_key(user)
# print(Result)










'''

Filter Nested Dict by Inner Key Condition

Task: Employees nested dict se sirf un employees ko filter karo jinki experience 2 saal se zyada ho.

Input: emps = {"E1": {"exp": 3}, "E2": {"exp": 1}, "E3": {"exp": 5}}

Expected Output: {"E1": {"exp": 3}, "E3": {"exp": 5}}

'''

# def filter_2plus_experience(d):
#     res={}
#     for i in d:
#         if d[i]['exp']>2:
#             res[i]=d[i]
#     return res

# user=eval(input("enter your dict"))
# result=filter_2plus_experience(user)
# print(result)    











'''

Key-Length Comparison Filter

Task: Dict se un entries ko filter karo jahan Key ki length Value (integer) se badi ho.

Input: d = {"python": 4, "django": 10, "html": 2}

Expected Output: {"python": 4, "html": 2}

'''


# def filter_dict_length_grater_value(d):
#     res={}
#     for i in d:
#         if len(i)>d[i]:
#             res[i]=d[i]
#     return res

# user=eval(input("enter your dict"))
# result=filter_dict_length_grater_value(user)
# print(result)









'''
'Group numbers by sum of digits --done'??


Aapko numbers ki ek list di jayegi, aur aapko un numbers ke digits (aank) ka sum 
(jod) nikalna hai. Phir jin numbers ke digits ka sum aapas me BARABAR (same) aayega, unhe ek 
saath group (cluster) karke ek jagah rakhna hai.Python me is kaam ke liye Dictionary (HashMap) 
sabse best aur fast tool hota hai.Step-by-Step ExampleMaan lijiye aapke paas yeh list hai:arr = 
[12, 21, 30, 41, 14, 50]Step 1: Har number ke digits ka sum nikalein12 $\rightarrow 1 + 2 =$ 321 
$\rightarrow 2 + 1 =$ 330 $\rightarrow 3 + 0 =$ 341 $\rightarrow 4 + 1 =$ 514 $\rightarrow 1 + 4 =$ 
550 $\rightarrow 5 + 0 =$ 5Step 2: Same sum wale numbers ko ek group (List) me daaleinSum = 3 wale: 
[12, 21, 30]Sum = 5 wale: [41, 14, 50]Final Output:{3: [12, 21, 30], 5: [41, 14, 50]}\
(Ya phir in sub-lists ko ek sath output kar sakte ho: [[12, 21, 30], [41, 14, 50]])

'''



# def digit_sum(n):
#     total=0
#     n=abs(n)
#     while n>0:
#         total=total+(n%10)
#         n=n//10
#     return total   


# def group_by_digit(l):
#     res={}
#     for num in l:
#         if num==0:
#             total=0
#         else:
#             total=digit_sum(num)

#         if total not in res:
#             res[total]=[]

#         res[total].append(num)

#     return res


# user=eval(input("enter your dict"))
# result=group_by_digit(user)
# print(result)





'''
.Move all elements whose digit sum is prime to front ??


Aapko numbers ki ek list di jayegi. Aapko har number ke digits ka sum (jod) nikalna hai, aur check karna hai ki wo sum ek Prime Number (2, 3, 5, 7, 11...) hai ya nahi.

Jin numbers ke digits ka sum Prime aaye, un sabhi numbers ko array ke AAGE (front me) shift kar do.

Baaki bache huye numbers (jin ka digit sum Non-Prime ho) unhe PEECHE (back me) rehne do.


'''

# def is_prime(n):
#     if n<=1:
#         return False
#     elif n==2:
#         return True
    
#     elif n%2==0:
#         return False

#     for i in range(3,int(n**0.5)+1,2):
#         if n%i==0:
#             return False
#     return True


# def is_sum_digit_prime_then_shift_front(l):
#     for i in range(len(l)):
#         total=0
#         for j in range(len(i))
        



        

        


d={'name':'maaz','age':10}
d['age']=20
print(d)