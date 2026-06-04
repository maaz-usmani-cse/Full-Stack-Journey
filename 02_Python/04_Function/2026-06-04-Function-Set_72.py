'''
User ne shopping cart mein kuch items dale hain aur ek promo code 
lagaya hai. Kuch coupons ke niyam hote hain: "Yeh coupon tabhi chalega 
jab cart ke SAARE items 'Clothing' category ke hon, ya fir kisi BHI EK item ki price 5000 se upar ho."
Sawaal: Ek function banao jo bataye ki kya coupon valid (True) hai ya invalid (False).

'''

# def is_coupon_valid(l):
#     any_cloths=all(i['category']=='Clothing'for i in l )
#     any_price=all(i['category']=='Clothing'for i in l )
#     if any_cloths or any_price:
#         return True
#     return False

# user=eval(input("enter your list"))
# result=is_coupon_valid(user)
# print(result)






'''
Frontend (React/HTML) ko data bhejne se pehle, backend par data saaf karna padta hai. 
Agar API ke response (dictionary) mein koi field None, khali string "", ya khali list [] hai, 
toh use remove kar do taaki network par faltu load na jaye.
Sawaal: Ek dictionary di hai, usme se saare khali/None data ko remove 
karke naya optimized dictionary return karo.
'''

# def clean_data(d):
#     new_dict={}
#     for i in d:
#         if d[i]:
#             new_dict[i]=d[i]
#     return new_dict


# user=eval(input("enter your list"))
# result=clean_data(user)
# print(result)
        






'''
Use Case: Naukri.com ya LinkedIn jaise portals par jab hum resume upload karte hain,
toh backend par ek ATS (Applicant Tracking System) chalta hai. Wo check karta hai ki
kya tumhare resume ke text mein recruiter ke SAARE mandatory keywords (jaise Python, Django) aur 
kam se kam KOI EK optional keyword (jaise AWS, Docker) hai ya nahi.

'''

# def ats_scanner(resume,mandatory,optional):
#     resume=resume.lower
#     mandatory=all(i.lower()in resume for i in mandatory)
#     optional=any(i.lower() in resume for i in optional)
#     if resume and optional:
#         return "Resume Shortlisted for Technical Round!"
#     return "Resume Rejected: Skills mismatch."

# user=input("write your resume")
# mandatory=['Python','Django']
# optional=['AWS', 'Docker']
# result=ats_scanner(user,mandatory,optional)
# print(result)






'''

Aapko $1$ se lekar $n$ tak ke lagatar numbers ki ek list milni chahiye thi,
par usme se ek number missing (gayab) hai. List sorted nahi hai. Aapko wo 
missing number dhoodh kar nikalna hai bina list ko sort kiye.
Real Example: nums = [3, 7, 1, 2, 8, 4, 5], yahan $n = 8$

'''

# def find_missing_value(l):
#     d={}
#     for i in l:
#         d[i]=True
#     for i in range(1,len(l)+1):
#         if i not in d:
#             return f'missing value is {i}'
#     return 'al re availble'


# user=eval(input("enter your list"))
# result=find_missing_value(user)
# print(result)







'''
Ek string di hai jisme akshar lagatar repeat ho rahe hain.
Aapko use compress karke akshar aur uski ginti likhni hai.
Agar compressed string bada ban jaye toh asli string hi de do.
Real Example: "aabcccccaaa" $\rightarrow$ Output: "a2b1c5a3"

'''
 


# def compress_string(s):
#     count=1
#     res=''
#     for i in range(len(s)-1):
#         if s[i]==s[i-1]:
#             count=count+1
#         else:
#             res=res+s[i]+str(count)
#             count=1
#     res=res+s[-1]+str(count)
#     return res

# user=input("enter your word")
# result=compress_string(user)
# print(result)
        
        
    
