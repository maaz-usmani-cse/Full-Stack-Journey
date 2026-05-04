'''
l = [{'name': 'maaz', 'email': 'maaz@gmail.com'}, {'name': 'ali', 'email': 'ali@yahoo.com'}]
Loop chalao aur emails ko mask kar do, yani sirf pehla letter dikhe aur baki ***.

Expected Output: maaz@gmail.com ban jaye m***@gmail.com
'''
# def mask_email(l):
#     for i in l:
#         if 'email' in i:
#            email= i['email']
#            at_index=email.find('@')
#            masked_email=email[0]+'****'+email[at_index:]
#            i['email']=masked_email
#     return l

# user=eval(input("enter your list"))
# result=mask_email(user)
# print(result)









'''
employees = [{'name': 'A', 'salary': 20000}, {'name': 'B', 'salary': 35000}, {'name': 'C', 'salary': 15000}]
Loop chalao: Agar salary 25000 se kam hai, toh use 10% badha do. Final updated list print karo.
'''


# def update_salary(l):
#     for i in l:
#         if 'salary' in i and i['salary']<25000:
#             increment=i['salary']*0.10
#             i['salary']=i['salary']+increment
#     return l

# user=eval(input("enter your list"))
# result=update_salary(user)
# print(result)










'''
l = [{'color': 'red'}, {'color': 'blue'}, {'color': 'red'}, {'color': 'green'}]
Bina set() ka use kiye, loop se saare unique colors ki ek list banao.

Expected Output: ['red', 'blue', 'green']
'''

# def persnoal_color_list(l):
#     color=[]
#     for i in l:
#         if 'color' in i and i['color'] not in color:
#             color.append(i['color'])
#     return color

# user=eval(input("enter your list"))
# result=persnoal_color_list(user)
# print(result)










'''
students = [{'name': 'maaz', 'score': 85}, {'name': 'rohit', 'score': 92}, {'name': 'ali', 'score': 88}]
Loop chalao aur us student ka Naam print karo jiske sabse zyada marks hain.

'''

# def  greatest_marks_student(l):
#     student=''
#     marks=None
#     for i in l:
#         if 'score' in i:
#             if marks is None or i['score']>marks:
#                 marks=i['score']
#                 student=i['name']
#     return student


# user=eval(input("enter your list"))
# result=greatest_marks_student(user)
# print(result)







'''
s = "name:maaz,age:20,city:bhopal"
Is string ko loop aur split() ka use karke ek real dictionary mein convert karo.

Expected Output: {'name': 'maaz', 'age': '20', 'city': 'bhopal'}
'''


# def convert_string_to_dict(s):
#     d={}
#     items=s.split(',')
#     for i in items:
#         pair=i.split(':')
#         key=pair[0]
#         value=pair[1]
#         d[key]=value

#     return d

# user=input('enter your word')
# result=convert_string_to_dict(user)
# print(result)

