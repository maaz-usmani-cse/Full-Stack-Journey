'''
Cybrom ke students ke placements ka data hai jahan student ka naam 
aur uski company likhi hai. Tumhe loop chala kar ek nayi dictionary banani hai jahan
Company ka naam KEY ho, aur us company mein select hone waale students 
ke naamon ki LIST uski VALUE ho!

'''

# def group_by_company(placement):
#     new_dict={}
#     for i in placement:
#         company=placement[i]
#         if company not in new_dict:
#             new_dict[company]=[]
#         new_dict[company].append(i)
#     return new_dict

# user=placements = {
#     "Maaz": "TCS",
#     "Amjad": "Wipro",
#     "Rohit": "TCS",
#     "Zaid": "Infosys",
#     "Asif": "Wipro"
# }
# result=group_by_company(user)
# print(result)







'''
Ek database mein employees ka data department ke sath hai. Tumhe loop chalakar
sirf un employees ki salary 10% badhani hai (increment karna hai) jo "IT" department
mein hain. Baaki departments ka data same rahega.

Input Data:

Python
employees = {
    1: {"name": "Maaz", "dept": "IT", "salary": 50000},
    2: {"name": "Amjad", "dept": "HR", "salary": 45000},
    3: {"name": "Rohit", "dept": "IT", "salary": 60000}
}
'''

# def salary_increase(d):
#     for i in d:
#         emp_data=d[i]
#         if 'salary' in emp_data and 'dept' in emp_data:
#             if emp_data['dept']=='IT':
#                 current_salary=emp_data['salary']
#                 new_salary=current_salary+(current_salary*0.10)
#                 emp_data['salary']=new_salary
#     return d

# user={
#     1: {"name": "Maaz", "dept": "IT", "salary": 50000},
#     2: {"name": "Amjad", "dept": "HR", "salary": 45000},
#     3: {"name": "Rohit", "dept": "IT", "salary": 60000}
# }
# result=salary_increase(user)
# print(result)