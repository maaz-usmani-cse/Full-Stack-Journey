'''

Django blog project mein jab koi user title likhta hai (jaise "Python aur Django Seekhein!"),
 toh use website ka URL (slug) banana padta hai. Aapko ek logic banana hai jo string mein se saare spaces " " ko dash "-" se badal de, saare exclamation marks ! ko gayab (khali "") kar de, aur poori string ko lowercase mein badal de.

Real Django Example: title = "Learn Python And Django!"

Output: "learn-python-and-django"

'''


# def replace_dased(l):
#     res=''
#     for i in l:
#         if i!='!':
#             replce=i.replace(" ",'_').lower()
#             res=res+replce
#     return res



# user=input("enter your word")
# result=replace_dased(user)
# print(result)






'''

Security round mein ek string ko encode karne ke liye bola gaya hai. Aapko string ke andar ke kuch specific aksharon ko numbers se replace karna hai:

'a' ya 'A' ko badal kar '4' karna hai.

'e' ya 'E' ko badal kar '3' karna hai.

'i' ya 'I' ko badal kar '1' karna hai.

'o' ya 'O' ko badal kar '0' karna hai.

Real TCS Example: S = "Bhopal is Awesome"

Output: "Bh0p4l 1s 4w3s0m3"

'''


# def encode_string(s):
   
#     s = s.replace('a', '4').replace('A', '4')
#     s = s.replace('e', '3').replace('E', '3')
#     s = s.replace('i', '1').replace('I', '1') 
#     s = s.replace('o', '0').replace('O', '0')
    
#     return s

# user = input("enter your word: ") 
# result = encode_string(user)








'''
Django signup API mein data ka ek list/dictionary aaya hai. 
Aapko ek generator expression ka use karke yeh check karna hai ki kya saare incoming fields non-empty
 strings hain? Agar ek bhi field None, khali string "", ya sirf spaces "   " hua, toh turant False aana 
 chahiye, nahi toh True.Real Django Example: payload = ["Maaz", "Bhopal", "Django", "Python"] $\rightarrow$ 
 Output: TrueBad Payload: payload = 
["Maaz", "   ", "Django", None] $\rightarrow$ Output: False

'''

# def check_empty_string(l):
#    res=all(isinstance(i,str) for i in l)
#    return res

# user=eval(input("enter your list"))
# result=check_empty_string(user)
# print(result)









'''
Django login form mein do fields hain—email aur phone. Django ka niyam hai ki user dono me se koi bhi 
ek field bhar dega toh kaam chal jayega (dono khali nahi hone chahiye). Aapko any() ka use karke validation 
lagana hai.Inputs: email = "", phone = "98765XXXXX" $\rightarrow$ Output: True (Login allowed)Inputs: email = "",
 phone = "" 
$\rightarrow$ Output: False (Error: Dono khali hain!)

'''

# def check_field(email,phone):
#     res=any([email,phone])
#     return res


# email=input("enter ypur word")
# phone=input("enter your phone")
# result=check_field(email,phone)
# print(result)






'''
Django signup par ek naya password check lagana hai. Password tabhi strong mana jayega jab uski 
length 8 se badi ho AND usme kam se kam ek number (0-9) zaroori ho. Aapko all() ka use karke validation 
lagana hai.Inputs: password = "MaazBhopal7" $\rightarrow$ Output: True (Strong password)Inputs: password =
 "Maaz" $\rightarrow$ Output: False (Too short)Inputs: password = "MaazBhopal" $\rightarrow$ Output: 
False (Number missing)


'''
# def password_check(password):
#    length=len(password)>8
#    has_digit=any(i.isdigit() for i in password)
#    if not (length and has_digit):
#       return False
   
#    return True

# user=input("enter your password")
# result=password_check(user)
# print(result)








'''
Django e-commerce portal par vendor product ki images upload kar raha hai. 
Ek list mein 4 files ke extensions aaye hain: extensions = ['.jpg', '.png', '.jpeg', '.png']. 
Aapko generator expression aur all() ka use karke validation lagana hai ki 
kya saare extensions strictly image ke hain? (Maan lo image extensions sirf
.jpg, .jpeg, aur .png hain). Agar ek bhi .exe ya .pdf mila, toh if not block 
chalna chahiye.Payload 1: ['.jpg', '.png', '.jpeg'] $\rightarrow$ Output: Success 
(Database me save karo)Payload 2: ['.jpg', '.pdf', '.png'] $\rightarrow$ Output: 
Error Block Executed! (Kyunki .pdf aa gaya)

'''

# def image_extenshion_check(l):
#    allowed_extenshions=['.jpg', '.png', '.jpeg']
#    res=all(i in allowed_extenshions for i in l)
#    if not res:
#       return 'Error Block Executed! (Kyunki .pdf aa gaya)'
#    return True


# user=eval(input("enter your list"))
# result=image_extenshion_check(user)
# print(result)








'''
Ek wholesale order form aaya hai jisme 3 items ki quantities hain: items_qty = [15, 20, 8].
 Wholesaler ka niyam hai ki har ek item ki quantity kam se kam 10 honi chahiye tabhi order accept hoga.
   Aapko all() aur if not ka combination lagakar validation lagana hai.Inputs: [15, 20, 30] $\rightarrow$ 
   
   Output: Success (Order Placed)Inputs: [15, 20, 8] $\rightarrow$ Output:
 Error Block Executed! (Kyunki 8, 10 se chota hai)

'''

# def quantity_check(l):
#     res=all(i>=10 for i in l)
#     if not res:
#         return 'Error Block Executed! (Kyunki 8, 10 se chota hai)'
#     return True



# user=eval(input("enter your list"))
# result=quantity_check(user)
# print(result)
        


'''
User profile update karte waqt teen fields ka data aaya: [bio, github_url,
linkedin_url]. Hamein check karna hai ki kya koi bhi ek field khali string "" 
ya None hai? Is baar tumhein not any() ka dimaag lagana hai. if not (not any(...))
 ka logic bithaao—yani agar ek bhi gaddbad mili toh error block chale, nahi toh data seedhe
.save() ho jaye.Inputs: ["Dev", "github.com", "linkedin.com"] $\rightarrow$ Output: Success 
(Saved to DB)Inputs: ["Dev", "", "linkedin.com"] $\rightarrow$ Output: 
Error Block Executed! (Khali field mil gaya)

'''

def check_data(l):
    res=all(isinstance(i,str) and i.strip()for i in l)
    if not res:
        return 'Error Block Executed! (Khali field mil gaya)'
    return True

user=eval(input("enter your list"))
result=check_data(user)
print(result)