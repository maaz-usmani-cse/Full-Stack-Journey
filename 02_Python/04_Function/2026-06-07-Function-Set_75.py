'check kro ki even date p jiske last m even digit ho usi ka gadi chalega btao nahi to fine bhao'

# def calculate_total_fine(l,date,fine):
#     violating_vehicles=0
#     is_date_even=(date%2==0)
#     for i in l:
#         if is_date_even and i%2!=0:
#             violating_vehicles=violating_vehicles+1
#         elif not is_date_even and i%2==0:
#             violating_vehicles=violating_vehicles+1
#     return violating_vehicles*fine

# l=eval(input("enter your list"))
# date=int(input("enter your date"))
# fine=int(input("enter your fine amount"))
# result=calculate_total_fine(l,date,fine)
# print(result)        










'''
Ek cybersecurity company ne ek niyam banaya hai ki unka password hamesha ek
unique string hona chahiye jisme koi bhi akshar repeat na ho. Aapko ek string di hai, 
aapko batana hai ki kya ye password valid hai? (Niyam: in keyword use nahi karna hai!).
Real Example 1: s = "bhopal" $\rightarrow$ Output: True (Saare akshar alag hain).Real 
Example 2: s = 
"apple" $\rightarrow$ Output: False ('p' repeat ho gaya).
'''

# def is_uniques_string(s):
#     d={}
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             return 'repeat ho rha hai'
#     return True


# user=input("enter your word")
# result=is_uniques_string(user)
# print(result)









'''
apko ek list di hai. Aapko us list ka ek element chhod kar agla element 
(alternate elements) print karna hai, yani index 0, fir index 2, fir index 4... aise.
Real Example: l = [10, 20, 30, 40, 50, 60] $\rightarrow$ Output: [10, 30, 50]
'''

# def print_alternative_element(l):
#     alternative=[]
#     for i in range(0,len(l),2):
#         alternative.append(l[i])
#     return alternative

# user=eval(input("enter your list"))
# result=print_alternative_element(user)
# print(result)






'''
Aapko users ke status ki ek list di hai (True matlab active, False matlab inactive). 
Django dashboard ke liye aapko batana hai ki kya list mein kam se kam ek user active hai?
Real Example 1: users = [False, False, True, False] $\rightarrow$ Output: True
Real Example 2: users = [False, False, False] $\rightarrow$ Output: False

'''
# def filter_data(l):
#     return any(l)




'''
Aapko ek list di hai jisme user ke 4 documents ka verification status hai 
(True matlab verify ho gaya, False matlab pending hai).
Aapko all() ka use karke batana hai ki kya saare ke saare documents verify 
ho chuke hain taaki profile approve ki ja sake?
Real Example 1: docs = [True, True, True, True] $\rightarrow$ Output: True
Real Example 2: docs = [True, False, True, True] $\rightarrow$ Output: False 
(Kyunki ek document abhi bacha hai).

'''

# def is_verify_document(l):
#     return all(l)


# user=eval(input("enter your list"))
# result=is_verify_document(user)
# print(result)





'''
Aapko ek dictionary di hai jisme bachon ke naam aur unke exam ke marks hain. 
Aapko ginti karke batana hai ki kitne bache exam mein paas 
hue hain (Paas hone ke liye marks 40 ya 40 se zyada hone chahiye)?
Real Example: marksheet = {"Maaz": 85, "Rahul": 35, "Amit": 42, "Rohit": 28}
$\rightarrow$ Output: 2 (Kyunki sirf Maaz aur Amit ke marks 40 se upar hain).

'''
# def is_passing_student(d):
#     pass_student=0
#     for i in d:
#         if d[i]>40:
#             pass_student=pass_student+1
#     return pass_student

# user=eval(input("enter your list"))
# result=is_passing_student(user)
# print(result)






'''
Ek bohot badi E-commerce website (jaise Amazon) par customers alag-alag products 
ko 1 se 5 tak ki star rating dete hain. Website ka manager 
chahta hai ki un saare products ki list baahar nikali jaye jinki rating lagatar 
(continuously) badhti chali gayi ho,
 kyunki un products ko top page par promote karna hai.
'''

# def check_rating(l):
#     for i in range(len(l)-1):
#         if l[i]>=l[i+1]:
#             return False
        
#     return True


# def filter_top_product(l):
#     selected_product=[]
#     for j in l:
#         product_id=j[0]
#         rating_only=j[1:]
#         if check_rating(rating_only)==True:
#             selected_product.append(product_id)
#     return selected_product


# user=eval(input("enter your list"))
# result=filter_top_product(user)
# print(result)







'''
Aapko numbers ki ek list di hai. Aapko ek naya code likhna hai jo list 
ke har ek number ka count (frequency) nikaal kar ek Dictionary banaaye. 
Par niyam yeh hai ki aakhri output mein sirf wahi numbers dikhne chahiye jo 
list mein 1 se zyada baar (Duplicate) aaye hain! Jo sirf 1 baar aaya hai, use nikaal dena hai.

Real Example: l = [1, 2, 3, 2, 1, 4, 1]

Output:  {1: 3, 2: 2}

'''

# def check(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     repeated={}
#     for j in d:
#         if d[j]>1:
#             repeated[j]=d[j]
#     return repeated


# user=eval(input("enter your list"))
# result=check(user)
# print(result)





