'''
Dictionary Filtering & Square Transformation
Aapko ek dictionary di jayegi jismein items aur unki quantities hain. 
Aapko ek aisi nayi dictionary banani hai jismein sirf wahi items hon jinki quantity even ho, 
aur output mein unki quantity ka square ho jana chahiye.
'''

# def transform_even_quantities(d):
#     res={}
#     for i in d:
#         quantity=d[i]
#         if quantity%2==0:
#             res[i]=quantity**2
#     return res

# user=eval(input("enter your dict"))
# result=transform_even_quantities(user)
# print(result)





'''

Question 24: Nested List to Nested Dictionary Mapping
Aapko students ke data ki ek nested list di jayegi: [[Roll, Name, Marks], ...]. 
Aapko ek function banana hai jo is list ko ek nested dictionary mein convert kare, 
jahan Roll Number outer key hogi, aur andar baaki data hoga.

Python
def list_to_nested_dict(student_list):
    # Dictionary comprehension ka next level logic
    pass

# Test Case
students = [
    [1, "Maaz", 95],
    [2, "Rohit", 80],
    [3, "Amit", 45]
]
print(list_to_nested_dict(students))
# Expected Output: {1: {'name': 'Maaz', 'marks': 95}, 2: {'name': 'Rohit', 'marks': 80}, 3: {'nam

'''

# def listed_to_nestted_dict(l):
#     res={}
#     for i in l:
#         key=i[0]
#         res[key]={'name':i[1],'marks':i[2]}
#     return res

# user=eval(input("enter your list"))
# result=listed_to_nestted_dict(user)
# print(result)




'''
Tumhe ek list di jayegi, jaise [0, 1, 0, 3, 12]. Tumhe saare 0 ko uthakar list ke aakhri mein 
fenkna hai, par baaki numbers ka kram (order) 
nahi badalna chahiye. Output aana chahiye: [1, 3, 12, 0, 0].

'''

# def arrange_zero_right_side(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]!=0:
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp

#     return l

# user=eval(input("enter your list"))
# result=arrange_zero_right_side(user)




'''
Target Ka Joda (Two Sum - Sorted Array)
Sawaal: Tumhe ek pehle se sorted list di hai: [2, 7, 11, 15] aur ek target diya hai 9. 
Tumhe un do numbers ka index batana hai jinko jodhkar target 9 ban jaye (jaise yahan 2 + 7 = 9).

'''

# def find_target_number(l,target):
#     d={}
#     for i in range(len(l)):
#         required=target-l[i]
#         if required in d:
#             return d[required],i
#         d[l[i]]=i


# user=eval(input("enter your list"))
# target=int(input("enter your target"))
# result=find_target_number(user,target)
# print(result)





