'''
Socho tum ek Inter-College Hackathon ke liye registration system bana rahe ho. Tumhe ek function banana hai jiska naam hoga validate_hackathon_team.

Ye function team ka data check karega aur do variables (is_approved, rejection_reason) return karega.

📝 Input (Jo tumhare function ke paas jayega):
Tumhara function teen cheezein input mein lega:

team_name (String)

member_count (Integer/Number)

project_domain (String)

⚙️ Validation Ke Rules (Shartein):
Rule 1 (Team Name Check): Team ka naam khali nahi hona chahiye, aur uski length kam se kam 4 characters ki honi chahiye. (Agar galat hai toh message bhejoge: "Bhai, team ka naam kam se kam 4 character ka rakho!")

Rule 2 (Member Count Check): Hackathon ke rule ke mutabik, ek team mein kam se kam 2 members aur zyada se zyada 4 members hone chahiye. Na usse kam, na usse zyada. (Agar galat hai toh message: "Bhai, team mein sirf 2 se 4 members hi ho sakte hain!")

Rule 3 (Domain Check): Project ka domain sirf teen hi allowed hain: 'Web', 'AI', ya 'App'. Agar koi user in teeno ke alawa kuch aur dalta hai (jaise 'Blockchain' ya 'Cyber'), toh wo reject ho jayega. (Agar galat hai toh message: "Bhai, domain sirf Web, AI, ya App hona chahiye!")

'''

# def validate_hackathon_team(team_name,member_count,project_domain):
#    if len(team_name)<4:
#       return False,'Bhai, team ka naam kam se kam 4 character ka rakho!'
#    if  member_count<2 or member_count>4:
#       return False ,"Bhai, team mein sirf 2 se 4 members hi ho sakte hain!"
#    allowed_domains = ['web', 'ai', 'app']
#    if  project_domain in allowed_domains:
#       return False ,"Bhai, domain sirf Web, AI, ya App hona chahiye!"
#    return True ,None

# team_name=input("enter your team name")
# member_count=int(input('how many member'))
# project_domain=input('enter your domain')
# is_approved, rejection_reason=validate_hackathon_team(team_name,member_count,project_domain)
# if rejection_reason:
#    print(f'{rejection_reason}')
# else:
#    print('succes full')





'''
# Bank ke transactions ki list aa rahi hai. Tumhe ek generator banana hai 
# jo sirf un transactions ko yield kare jo suspicious hain. Suspicious ki shart yeh hai:
# Amount 50,000 se zyada hona chahiye
# AUR transaction ka time "Night" (raat) ka hona chahiye.
# '''

# def filter_suspius_transection(l):
#     for i in l:
#       if 'amt' in i and 'time' in i:
#          if i['amt']>50000 and i['time']=='Night':
#             yield i


# user=[
#     {"amt": 60000, "time": "Day"},
#     {"amt": 12000, "time": "Night"},
#     {"amt": 85000, "time": "Night"},  
#     {"amt": 90000, "time": "Night"}   
# ]
# result=filter_suspius_transection(user)
# print(next(result))
# print(next(result))
# print(next(result))

         




'''
Ek list ke har number ke andar jao aur uske ek-ek akshar (digit)
 ko uske position (index) ke hisab se badlo:
Agar digit Even index (0th position, 2nd position...) par baithi hai, toh use 'E' se replace karo.

Agar digit Odd index (1st position, 3rd position...) par baithi hai, toh use 'O' se replace karo.

Phir saare aksharon ko chipka kar string bana do!
'''

# def replac_odd_even(l):
#     for i in range(len(l)):
#         digit=str(l[i])
#         res=''
#         for j in digit:
#             if int(j)%2==0:
#                 res=res+'e'
#             else:
#                 res=res+'o'
#         l[i]=res 
#     return l

# user=eval(input("enter your list"))
# result=replac_odd_even(user)
# print(result)







'''
Ek list ke har number ke andar jao aur har akshar (digit) ko check karo.
Agar koi digit apne aage waale akshar (next digit) se badi hai,
toh un dono ke beech mein ek '-' 
(dash) ghusa do, warna dono ko normal chipka do!
'''
# def replace_greater_with_dash(l):
#     for i in range(len(l)):
#         digit=str(l[i])
#         res=''
#         for j in range(len(digit)-1):
#             if int(digit[j])>int(digit[j+1]):
#                 res=res+digit[j]+'_'
#             else:
#                 res=res+digit[j]
#         res=res+digit[-1]
#         l[i]=res
#     return l


# user=eval(input("enter your list"))
# result=replace_greater_with_dash(user)
# print(result)




