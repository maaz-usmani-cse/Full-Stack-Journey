'''
API Response Cleaning (Drop Keys with Zero or Negative Values)Task: An analytics API dict se un keys ko hatana hai
 jinki numerical value $0$ ya negative ($<0$) ho.Input: {"views": 1500, "clicks": 0, "bounce_rate": -5, 
"shares": 120}Expected Output: {"views": 1500, "shares": 120}
'''

# def clean_negative_dict(d):
#     res={}
#     for i in d:
#         if d[i]>0:
#             res[i]=d[i]
#     return res


# user=eval(input("enter your list"))
# result=clean_negative_dict(user)
# print(result)









'''

Character Frequency Dictionary (Only Upper Case Letters)

Task: String ke har character ka count nikalna hai, lekin dictionary mein sirf Uppercase letters hi keys banni chahiye.

Input: "Hello MAAZ Usmani 2026"

Expected Output: {'H': 1, 'M': 1, 'A': 2, 'Z': 1, 'U': 1}

'''

# def character_frequency(s):
#     l=s.split()
#     res={}
#     for i in l:
#        for j in i:
#            if j.isupper():
#                if j in res:
#                    res[j]=res[j]+1
#                else:
#                    res[j]=1

#     return res


# user=input('enter your word')
# result=character_frequency(user)
# print(result)









'''
: Product-Price dictionary ki keys aur values ko swap karo, aur nayi values 
(jo pehle keys thin) ko uppercase banao aur prices ko double ($2\times$) kar do.Input:
 {"laptop": 500, "mobile": 200}Expected Output: {1000: "LAPTOP", 400: "MOBILE"}

# '''
# def swap_keys_value(d):
#     res={}
#     for i in d:
#       values =d[i]
#       res[values]=i.upper()
#     return res


# user=eval(input("enter your list"))
# result=swap_keys_value(user)
# print(result)








'''

Mathematical Operation Dispatcher (No if-elif)Problem StatementUser se do numbers ($A$ aur $B$) 
input lo, aur ek option input lo:0 for Addition1 for Subtraction2 for Multiplication3 for Power 
($A^B$)Constraint: Code mein koi bhi if-elif-else statement nahi hona chahiye. 
Choice ke base par correct function ko list se fetch karke execute karna hai.

'''
# def add(a,b):
#     return a+b


# def substract(a,b):
#     return a-b


# def multiply(a,b):
#     return a*b

# def power(a,b):
#     a**b


# operations=[add,substract,multiply,power]

# a=int(input("enter your number"))
# b=int(input('enter your number'))
# choise=int(input("Choose operation (0: Add, 1: Sub, 2: Mul, 3: Power): "))

# selected_func=operations[choise]
# print(selected_func(a,b))










'Find pair whose sum is closest to target '
# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i<pivot:
#             left.append(i)
#         elif i==pivot:
#             middle.append(i)
#         else:
#             right.append(i)
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)



# def find_sum_with_closest_target(l,target):
#     res=quick_sort_pivot(l)
#     left=0
#     right=len(res)-1
#     closest_diff=float('inf')
#     best_pair=()

#     while left<right:
#         current_sum=res[left]+res[right]
#         diff=abs(target-current_sum)

#         if diff<closest_diff:
#             closest_diff=diff
#             best_pair=(res[left],res[right])

#         if current_sum>target:
#             right=right-1
#         else:
#             left=left+1

#     return best_pair


# user=eval(input("enter your list"))
# target=int(input("enter your target number"))
# result=find_sum_with_closest_target(user,target)
# print(result)



    


