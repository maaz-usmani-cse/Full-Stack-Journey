'''
Ek function extract_domain(email) likho jo ek valid email string parameter le aur uska domain name return kare.

Input: "user.name@gmail.com"

Expected Output: "gmail.com"

'''
# def extract_domain(email):
#     return email.split('@')[-1]


# email=input("enter your email")
# result=extract_domain(email)
# print(result)




'''
Ek function mask_email(email) banao jo sensitive emails ko mask kare. Username ke pehle 2 characters aur
aakhiri character dikhne chahiye,
baaki * se replace ho jayein. Agar username 3 ya usse kam characters ka ho, to bas pehla character dikhao.

Input: "developer@domain.com"

Expected Output: "de*****r@domain.com"

'''

# def mapped_email(email):
#   parts=email.split('@')
#   username=parts[0]
#   domain=parts[-1]
#   if len(username)<=3:
#     masked_user= username[0] + '*' *(len(email)-1)
#     return masked_user + '@' +domain
#   else:
#     masked_user=username[:2] + '*' * (len(username)-3) + username[-1]
#     return masked_user+'@' + domain


# email=input("enter your email")
# result=mapped_email(email)
# print(result)



'''
Ek function group_by_domain(email_list) likho jo emails ki list le aur ek dictionary return
 kare jisme key domain ho aur value un users ke usernames ki list.

Input: ["ali@gmail.com", "rahul@yahoo.com", "sara@gmail.com"]

Expected Output: {"gmail.com": ["ali", "sara"], "yahoo.com": ["rahul"]}
'''
# def group_by_domain(email):
#     d={}
#     for i in email:
#         parts=i.split('@')
#         key=parts[-1]
#         value=parts[0]
#         if key not in d:
#             d[key]=[]
#         d[key].append(value)

#     return d

# email_list=eval(input('enter your list'))
# result=group_by_domain(email_list)
# print(result)


