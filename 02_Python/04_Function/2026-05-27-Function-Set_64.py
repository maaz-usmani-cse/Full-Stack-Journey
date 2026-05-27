'''
Is list mein se sirf wahi Composite numbers dhoond kar bahar nikaalo
jo 3 se poore-poore divide hote hon!
'''
# def is_composite_and_divisible_by_3(n):
#     if n%3!=0:
#         return False
#     if n<=3:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return True
#     return False
    

# user=eval(input("enter your list"))
# result=list(filter(is_composite_and_divisible_by_3,user))
# print(result)





'with the help of list comprehenshion '
# user=[2, 4, 7, 9, 12, 15, 17, 18, 20, 23, 25]
# res=[i for i in user if i%3==0 and any(i%j==0 for j in range(2,i))]








'''
"Maaz, agar kisi username mein @, #, ya $ aa gaya, toh wo illegal hai.
Mujhe un usernames ki list nikaal kar do
jo Illegal (Khatarnak) hain!"
'usernames = ["maaz_usmani", "rohit@123", "amit_rits", "suresh#bhopal", "code_journey"]'
'''

# def check_username(l):
#     illegal_chars = ['@', '#', '$']
#     has_illegal=[i for i in l if any(j in illegal_chars for j in i)]
#     return has_illegal
    


# user=eval(input("enter your list"))
# reuslt=check_username(user)
# print(reuslt)






'''
Mujhe sirf un students ke marks ki list chahiye jo saare subjects mein
70 se upar (> 70) score kiye hon!
Agar ek bhi subject mein 70 ya usse kam hua, toh wo bahar!
'''

# def find_marks(l):
#     res=[i for i in l if all(j>70 for j in i)]
#     return res


# user=eval(input("enter your list"))
# result=find_marks(user)
# print(result)







'''
Rearrange array such that positives and negatives alternate (stable)

is question ka matlab ekdam simple aur dhasu hai. Interviewer tumse bol raha 
hai ki ek list mein positive numbers (+ve) aur negative numbers (-ve) gich-pich
(mix) hokar pade hain. Tumhe unhe is tarah set karna hai ki wo ek ke baad ek
alternate aayein—yaani
pehle positive, phir negative, phir positive, phir negative
'''


# def alternate_rearrange(l):
#     pos=[]
#     neg=[]
#     for i in l:
#         if i>=0:
#             pos.append(i)
#         else:
#             neg.append(i)
#     final_reult=[]
#     i=0
#     j=0
#     while i<len(pos) and j<len(neg):
#         final_reult.append(pos[i])
#         final_reult.append(neg[j])
#         i=i+1
#         j=j+1
#     while i<len(pos):
#         final_reult.append(pos[i])
#         i=i+1
#     while i<len(neg):
#        final_reult.append(neg[j])
#     return final_reult



# user=eval(input("enter your list"))
# result=alternate_rearrange(user)
# print(result)







'Move all elements divisible by 3 to middle, others on sides'
# def ararnge_miid_divisible_by_3(l):
#     others=[]
#     div_3=[]
#     for i in l:
#         if i%3==0:
#             div_3.append(i)
#         else:
#             others.append(i)
#     mid=len(others)//2
#     left=others[:mid]
#     right=others[mid:]
#     final_result=left+div_3+right
#     return final_result


# user=eval(input("enter your list"))
# result=ararnge_miid_divisible_by_3(user)
# print(result)







'secret to send email '

# def mask_email(l):
#     for i in l:
#         if 'email' in i:
#             email=i['email']
#             address=email.find('@')
#             mask=email[:2] + '*' * (address-2) + email[address:]
#             i['email']=mask
#     return l
        
# user=eval(input("enter your list"))
# result=mask_email(user)
# print(result)







'''
Mujhe sirf un users ki list chahiye jinka role ekdam "admin" hai, AUR unka jo "token" hai wo security 
ke liye badal kar ekdam khaali ("")
ho jana chahiye, baaki name aur role waisa ka waisa copy hona chahiye!
users = [
    {"name": "Maaz", "role": "admin", "token": "SEC#1234"},
    {"name": "Rohit", "role": "student", "token": "STU@9988"},
    {"name": "Amit", "role": "admin", "token": "SEC#8877"},
    {"name": "Suresh", "role": "student", "token": "STU@1122"}
]

'''


# def filter_list(l):
#     res=[]
#     for i in l:
#         if 'role' in i and i['role']=='admin':
#             res.append({**i,'token':''})
#     return res


# user=eval(input("enter your list"))
# result=filter_list(user)
# print(result)










'''
Ek password tabhi valid mana jayega jab uske andar kam se kam ek special character (@, #, $) maujood ho.
Mujhe un passwords ki list nikaal kar do jo Invalid (Unsafe) hain
(yaani jisme inme se ek bhi character nahi hai!).
passwords = 
# '''
# def is_password_valid(l):
#     invalid_password=[]
#     for i in l:
#       has_special_char=False
#       for j in i:
#          if not j.isalnum():
#             has_special_char=True
#             break
#       if not has_special_char:
#          invalid_password.append(i)
#     return invalid_password



# user=eval(input("enter your list"))
# result=is_password_valid(user)
# print(result)