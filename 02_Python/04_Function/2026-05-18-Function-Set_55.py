'nested dictionary ko list m dalo bhai mere'
# def convert_dict(d):
#     l=[]
#     for i in d:
#       inner_dict=d[i]
#       for j in inner_dict:
#          l.append([j,inner_dict[j]])
#     return l

# d={
#     1: {'name': 'maaz', 'age': 20, 'collage': 'rits'}, 
#     2: {'name': 'amjad'}
# }
# result=convert_dict(d)
# print(result)

         




'''
Maan lo Cybrom Technology ka employee data ek nested dictionary mein hai. 
Har employee ID ke andar unka name, department, aur salary ka data hai.

Tumhe ek aisa program banana hai jo sirf un employees ka naam aur unki salary
ek naye dabba (list) mein append kare jinki Salary 50,000 ya usse zyada hai.
'''

# def refine_data_salary_50000(d):
#     l=[]
#     for i in d:
#         new_dict=d[i]
#         if "name" in new_dict and "salary" in new_dict:
#             if new_dict["salary"]>50000:
#                     l.append([new_dict["name"],new_dict["salary"]])
#     return l

# user={
#     101: {"name": "Maaz", "dept": "IT", "salary": 65000},
#     102: {"name": "Amjad", "dept": "HR", "salary": 45000},
#     103: {"name": "Rohit", "dept": "IT", "salary": 55000},
#     104: {"name": "Saba", "dept": "Marketing", "salary": 30000}
# }
# result=refine_data_salary_50000(user)
# print(result)







'''
Cybrom Technology ke database mein employees ka data department ke sath hai.
Tumhe loop chala kar un employees ka naam ek list mein append karna hai jo "IT" department mein hain AUR jinki salary 60,000 se badi hai.
Kisi bhi missing key (KeyError) se bachne ke liye in ka kavach zaroori hai!
'''

# def inquiry(d):
#     l=[]
#     for i in d:
#         new_dict=d[i]
#         if 'name' in new_dict and 'dept' in new_dict and 'salary' in new_dict:
#            if new_dict['dept']=='IT' and new_dict['salary']>60000:
#                l.append(new_dict['name'])
#     return l


# employees=eval(input("enter your dict"))
# result=inquiry(employees)
# print(result)






'''
Ek list ke har element ko uthao,
us number ke andar ke ek-ek akshar (digit) ko check karo,
aur sirf ODD digits (1, 3, 5, 7, 9) ki ginti (count)
se us element ko replace kar do.
'''

# def replace_odd_digit_count(l):
#     for i in range(len(l)):
#         digit=str(l[i])
#         count=0
#         for j in digit:
#             if int(j)%2!=0:
#                 count=count+1
#         l[i]=count
#     return l
        
# user=eval(input("enter your list"))
# result=replace_odd_digit_count(user)
# print(result)







'1 se lekar 20 tak ke saare numbers ko ek list mein append karna hai,'
' lekin ek shart hai: jo numbers 3 se poore divide hote hain (jaise 3, 6, 9...),'
' unhe continue statement ka use karke skip kar dena hai.'

# def filter_number(n):
#     li=[]
#     for i in range(1,n+1):
#         if i%3==0:
#             continue
#         li.append(i)
#     return li


# user=int(input("enter your range number"))
# result=filter_number(user)
# print(result)






'''
Ek school ke data mein classes hain, unke andar students hain, 
aur unke andar unka result ("Pass" ya "Fail") likha hai.
Tumhe double loop chalakar check karna hai ki kaun-kaun sa student "Fail" hua hai, 
aur unke naam ko alert_list mein daalna hai.
'''

# def filter_result(d):
#     alert_list=[]
#     for i in d:
#         student=d[i]    
#         for j in student:
#             info=student[j]
#             if 'result' in info:
#                 if info['result']=="Fail":
#                     alert_list.append(j)
#     return alert_list

# user={
#     "Class_A": {
#         "Asif": {"result": "Pass"},
#         "Rahul": {"result": "Fail"}
#     },
#     "Class_B": {
#         "Amit": {"result": "Pass"},
#         "Sana": {"result": "Fail"}
#     }
# }
# result=filter_result(user)
# print(result)          







'Ek list ke har element ko uthao aur us number ke saare '
'aksharon ka jod (sum of digits) nikal kar uski jagah par replace kar do.'

# def total_digit_count(l):
#     for i in range(len(l)):
#         digit=str(l[i])
#         count=0
#         for j in digit:
#             count=count+int(j)
#         l[i]=count
#     return l

# user=eval(input("enter your list"))
# result=total_digit_count(user)
# print(result)





'''
Ek list ke har element ko uthao aur us number ke andar ke ek-ek akshar ko check karke sabse bada akshar (maximum digit) dhoodho, aur poore number ko us max digit se replace kar do.
 (Bina max() function ke, loop se bada digit dhoodhna hai!).

'''
# def replace_max_digit(l):
#     for i in range(len(l)):
#         digit=str(l[i])
#         maximum=None
#         for j in digit:
#             if maximum is None or int(j)>maximum:
#                 maximum=int(j)
#         l[i]=maximum
#     return l


# user=eval(input("enter your list"))
# result=replace_max_digit(user)
# print(result)





