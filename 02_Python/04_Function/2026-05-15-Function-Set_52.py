'''
Ek list di hai numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Ek aisi nayi list banao jisme sirf un numbers ka Square ho jo Odd hain, aur wo square 50 se chota hona chahiye.
'''
# def filtr_list(l):
#     result=[i**2 for i in l if i%2!=0 and i**2<50]
#     return result

# user=eval(input("enter your list"))
# result=filtr_list(user)
# print(result)




'''
Tumhare paas ek 2D list hai: data = [["apple", "banana"], ["cherry", "date"], ["eggfruit"]].
Isko ek single flat list mein badlo lekin shart ye hai ki har fruit ka sirf pehla akshar (first letter) hi list mein aana chahiye.

Expected Output: ['a', 'b', 'c', 'd', 'e']

Concept Check: Nested list comprehension + string indexing.

'''

# def change_single_element_list(l):
#     li=[]
#     for i in l:
#        for j in i:
#             li.append(j[0])
#             break
#     return li




# user=eval(input("enter your list"))
# result=change_single_element_list(user)
# print(result)






'use of list '
# def change_single_element_list(l):
#     result=[j[0] for i in l for j in i]
#     return result

# user=eval(input("enter your list"))
# result=change_single_element_list(user)
# print(result)




'logical question'
# t = (1, 2, [3, 4])
# try:
#     t[2] += [5, 6]
# except TypeError:
#     print("Error aaya!")

# print(t)







# name = ("Maaz", "CSE") # Tuple
# print(hash(name)) # Ye ek bada sa number print karega (Jaise: 45321897...)

# # Ab list ke saath try karo
# skills = ["Python", "Django"] 
# print(hash(skills))
# # print(hash(skills)) # Ye line error degi: "TypeError: unhashable type: 'list'"






'logic test'
# x=(1,2,3,[1,2,3])
# x[3].append(5)
# print(x)








'date time k sath print karao aj konsa date aur time ho rha hai'
# from datetime import datetime
# def date_time():
#     from datetime import datetime
#     abhi = datetime.now()

#     tarikh = abhi.strftime("%d-%m-%Y") 
#     samay = abhi.strftime("%H:%M:%S") 

#     print(f"Aaj ki Date hai: {tarikh}")
#     print(f"Abhi ka Time ho raha hai: {samay}")




# print(date_time())
    




'konsa din hai konsa mahina hai konsa day hai sb print kro '
# def time_table_print():
    
#     from datetime import datetime
#     abhi = datetime.now()

#     din_ka_naam = abhi.strftime("%A")
#     mahina = abhi.strftime("%B")      
#     tarikh = abhi.strftime("%d")      
#     saal = abhi.strftime("%Y")        
#     samay = abhi.strftime("%I:%M %p") 

#     print(f"Bhai, aaj {din_ka_naam} hai.")
#     print(f"Abhi {mahina} ka mahina chal rha hai, date {tarikh} hai aur saal {saal}.")
#     print(f"Aur time ho rha hai: {samay}")



# print(time_table_print())










'''
Ek function banao jo student ke subjects aur marks le (kwargs),
aur unka Average nikal kar de. Par shart ye hai ki tum len() ya sum() use nahi kar sakte.
'''
# def calculate_average(**kwargs):
#     marks=0
#     subject=0
#     for i in kwargs:
#         marks=marks+kwargs[i]
#         subject=subject+1
#     if subject==0:
#         return 0
    
#     average=marks/subject
#     return average


# d={}
# user=int(input("how many subject??"))
# for i in range(user):
#     sub=input("enetr your subject")
#     marks=int(input("enter your marks"))
#     d[sub]=marks

# result=calculate_average(**d)
# print(result)


