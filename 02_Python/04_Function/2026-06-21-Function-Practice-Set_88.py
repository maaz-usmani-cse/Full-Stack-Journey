'''
Unique ID Detector (System Design Round)Interviewer Bola: 
"Maaz, humare paas user IDs ki ek database list hai. System mein ek bug ki 
wajah se kuch Duplicate IDs generate ho rahi hain. Mujhe poori list scan nahi 
karni, bas jaldi se short-circuit karke batao ki kya list mein ek bhi aisi ID 
hai jo duplicate hai?"Input: l = [101, 102, 103, 101] $\rightarrow$ 
Output: True (Kyunki 101 do baar aaya hai, yaani .count(i) > 1 hai).Input: 
l = [1, 2, 3] $\rightarrow$ Output: False

'''

# def uniques_id_detector(l):
#      d={}
#      res=any(i in d or d.update({i:True}) for i in l)
#      return res


# user=eval(input("enter your list"))
# result=uniques_id_detector(user)
# print(result)







'''
. Restricted Domain Blocker (Security Round)
Interviewer Bola: "Humare platform par kuch hackers temporary emails 
use kar rahe hain. Mujhe ek emails ki list di gayi hai. Pata karo ki kya 
list mein koi bhi email aisa hai jo restricted domains (jaise '@xyz.com' ya 
'@hack.com') se belong karta hai?"

Hint: Check karo ki kya kisi bhi email ke aakhri mein .endswith() se restricted domain match ho raha hai.

Input: emails = ["user1@gmail.com", "attacker@hack.com", "user2@yahoo.com"]

Output: True (Kyunki bad domain mil gaya).
'''

# def restrictted_domain_block(l):
#     restricted=('@xyz.com', '@hack.com')
#     res=any(i.endswith(restricted) for i in l)
#     return res


# user=eval(input("enter your list"))
# result=restrictted_domain_block(user)
# print(result)








'''
"Hum ek chat app bana rahe hain jahan abusive words allowed nahi hain. 
User ne ek message (string) bheja hai. Humare paas banned words ki ek list hai
banned = ["spam", "fake"]. Pata karo ki kya user ke message mein koi bhi 
banned word maujood hai?"

Input: message = "This product is totally fake and waste"

Output: True (Kyunki "fake" word message ke andar baitha hai).

'''

# def is_spam_word(s):
#     spam_word= ["spam", "fake"]
#     res=any(i in s for i in spam_word)
#     return res


# user=input("enter your message")
# result=is_spam_word(user)
# print(result)








'	Replace element with previous smaller element '
# def replace_previous_smallest_element(l):
#     n = len(l)
#     res = [-1] * n
    
#     for i in range(1, n):
#         if l[i-1] < l[i]:
#             res[i] = l[i-1]
            
       
#         elif res[i-1] < l[i] and res[i-1] != -1:
#             res[i] = res[i-1]
            

            
#     return res

# user = [2, 6, 4, 8]
# result = replace_previous_smallest_element(user)
# print(result)

