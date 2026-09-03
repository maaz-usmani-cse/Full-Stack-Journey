'''
Ek function banao is_email_okay(email) jo check kare:
Email me @ hona chahiye ANDEmail ke end me .com ya .in ya .org me
 se kam se kam koi ek hona chahiye (hint: email.endswith(...))
.Input: "test@gmail.com" $\rightarrow$ Expected Output: TrueInput: "test@gmail.xyz" $\rightarrow$ Expected Output: False

'''
# def is_email_okay(email):
#     required_symbol='@' in email
#     required=email.endswith((".com", ".in", ".org"))
#     if not(required_symbol and required):
#         return False 
#     return True


# email=input("enter your email")
# result=is_email_okay(email)
# print(result)


'''

Python me neeche diye gaye code snippet ka output kya aayega?

Python
'''
# text = "hello"
# result = any('@' for ch in text)
# print(result)





'''
Ek function likho is_valid_username(username) jo check kare:Username me space (' ') nahi honi
chahiye.Username kam se kam 5 characters lamba hona chahiye (len >= 5).Agar dono condition sahi hain toh 
True, warna False.Example:is_valid_username("rahul12")
Trueis_valid_username("rahul 12")  False
'''
# def is_valid_username(username):
#     if ' ' in username:
#         return False
#     elif len(username)<5:
#         return False

#     return True

# username=input("enter your username")
# result=is_valid_username(username)
# print(result)
    


'''
Ek function likho is_image_file(filename) jo check kare:

Kya file ka extension .jpg, .jpeg, ya .png me se koi ek hai?

Dhyaan rahe: Check case-insensitive hona chahiye (matlab agar file "photo.JPG" ya "photo.png" ho, dono valid maane jayein).
'''

# def is_valid_image_extenshion(image):
#    return image.lower().endswith((".jpg", ".jpeg", ".png"))
    
# user=input('enter your field')
# result=is_valid_image_extenshion(user)
# print(result)



'''
Ek function likho is_valid_phone(phone) jo check kare:
Phone number ki total length exactly 10 honi chahiye.Phone number sirf digits (0-9) se bana hona chahiye
(koi letter ya symbol nahi).Phone number '0' se shuru nahi hona chahiye.
Example:is_valid_phone("9876543210") $\rightarrow$ Trueis_valid_phone("0876543210") 
$\rightarrow$ False (0 se start ho raha hai)is_valid_phone("98765abc10") $\rightarrow$ False
(letters hain)Question 2: Passw
'''

# def is_phone_number_valid(phone):
#     if len(phone)<10 or not phone.isdigit() or not phone[0]!='0':
#         return False
#     return True

# phone=input("enter your phone")
# result=is_phone_number_valid(phone)
# print(result)





'''
Ek function likho has_vowel(text) jo check kare:Kya diye gaye text ke andar kam se kam ek vowel
 (a, e, i, o, u) maujood hai?Case-insensitive hona chahiye (matlab 'A' ya 'a' dono chalenge).
 Hint: Yahan loop ya any(...) ka use karo.
Example:has_vowel("sky") $\rightarrow$ Falsehas_vowel("strOng") $\rightarrow$ True
'''
# def is_vowel(word):
#    word=word.lower()
#    vowel='aeiou'
#    for i in vowel:
#       if i in word:
#          return True
#    return False

# user=input('enter your word')
# result=is_vowel(user)
# print(result)
   



'''
Social media ke liye ek function likho is_valid_hashtag(tag) jo check kare:

Tag hamesha '#' se start hona chahiye.

Tag ke andar koi space (' ') nahi honi chahiye.

Sirf '#' nahi hona chahiye, '#' ke baad kam se kam ek character hona zaroori hai (len > 1).
'''
# def is_valid_tag(tag):
#     if tag[0] !='#':
#         return f'tag ka start # se kro'

#     elif ' ' in tag:
#         return f'{tag} k andr aap sapce na do yrr'

#     elif len(tag)==1:
#         return f'{tag} yr ek character nahi hoga do ya usse zadh dalo'

#     return True


# user=input("enter your tag")
# result=is_valid_tag(user)
# print(result)