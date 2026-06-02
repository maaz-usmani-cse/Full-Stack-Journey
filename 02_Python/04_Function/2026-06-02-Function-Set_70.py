'''
 Ek numbers ki list di hai. Aapko unko Even (Sam) aur Odd (Visham) ke group mein
baantkar ek dictionary mein return karna hai. Dictionary ki keys hongi 'Even' 
aur 'Odd', aur unke andar un numbers ki list hogi.
Example: [1, 2, 3, 4, 5] $\rightarrow$ Output: {'Even': [2, 4], 'Odd': [1, 3, 5]

'''
# def group_even(l):
#     result={
#         'even':[],
#         'odd':[]
#     }
#     for i in l:
#         if i%2==0:
#             result['even'].append(i)
#         else:
#             result['odd'].append(i)
#     return result


# user=eval(input("enter your list"))
# result=group_even(user)
# print(result)






'''
Aapko wo pehla akshar dhoodhna hai jo string mein dobara (repeat) aaya ho. Jaise hi koi akshar pehli baar se zyada dikhe, turant wahi answer return kar do. Agar koi bhi repeat nahi ho raha, toh "" return karo.
Real Example: "codingchallenge" $\rightarrow$ Output: "c"
'''
# def first_repeating_char(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in d:
#         if d[i]>1:
#             return f'first repeating charcter:{j}'
#     return d


# user=(input("enetr your list"))
# result=first_repeating_char(user)
# print(result)








'''
Ek list di hai aur ek target sum diya hai. Aapko batana hai ki kya 
list ke andar koi bhi do aise numbers hain jinko jodne par target mile? Agar hain, 
toh True return karo, nahi toh False.
'''
# def summ_of_target(l,target):
#     d={}
#     for i in l:
#         required=target-i
#         if required in d:
#             return True
#         d[i]=True
#     return False


# user=eval(input("enter your list"))
# target=int(input("enter yur target number"))
# result=summ_of_target(user,target)
# print(result)






'''
Ek list di hai numbers ki. Aapko un saare numbers ko dhoodh kar
nikalna hai jo list mein Odd number of times 
(jaise 1 baar, 3 baar, 5 baar) aaye hain.
Real Example: [1, 2, 3, 2, 1, 3, 3] $\rightarrow$ Output: [3]
(Yahan 1 do baar aaya hai (even), 
'''

# def find_odd_occurenece(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     l=[]
#     for j in d:
#         if d[j]%2!=0:
#             l.append(j)
#     return l

# user=eval(input("enter your list"))
# result=find_odd_occurenece(user)
# print(result)






'''

Sawaal: Aapko ek dictionary di hai jisme employees ke naam aur unki [Age, Salary]
ki list save hai. Aapko ek nayi dictionary banani hai jo employees ko 3 groups—'Junior_High',
'Senior_High', aur 'Others' mein baante.

If-Else Ki Conditions (Niyam):

Junior_High: Agar employee ki Age 30 ya 30 se kam hai AND uski Salary 50,000 se zyada hai.

Senior_High: Agar employee ki Age 30 se zyada hai AND uski Salary 80,000 se zyada hai.

Others: Baaki bache hue saare employees is group mein jayenge.

employees = {
    "Maaz": [23, 85000],
    "Amit": [45, 90000],
    "Rahul": [28, 40000],
    "Rohit": [35, 60000]
}
'''


# def categroies_employees(l):
#     d={ 'senior':[],
#         'junior':[],
#         'others':[]
#           }
    
#     for i in l:
#         age=l[i][0]
#         salary=l[i][1]
#         if age>30 and salary>80000:
#             d['senior'].append(i)
#         elif age<=30 and salary>50000:
#                 d['junior'].append(i)
#         else:
#              d['others'].append(i)

#     return d

# user=eval(input("enter your list"))
# result=categroies_employees(user)
# print(result)    

