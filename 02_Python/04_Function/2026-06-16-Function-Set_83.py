'''
Django authentication ko secure banane ke liye ek rule lagaya gaya hai: 
User ka password kabhi bhi uske username jaisa nahi hona chahiye, aur na hi 
username password ke andar chhupa hona chahiye (substring). Aapko check lagana 
hai ki agar username password ke andar baitha hai, toh use block karo.Hint: Python 
ka in keyword use hoga yahan.Username: "maaz", Password: "123maaz789" $\rightarrow$ Output: 
Error Block Executed! (Kyunki password me 'maaz' chhupa hai)Username: "maaz", Password: 
"bhopal1234" $\rightarrow$ Output: Success

'''

# def is_same_password(username,password):
#     if username in password:
#         return False
    
#     return True

# username=input("enter your username")
# password=input("enter your password")
# result=is_same_password(username,password)
# print(result)








'''
Django comment system mein agar koi user bad words (jaise "fraud", "spam", "fake") 
likhta hai, toh humein use block nahi karna, balki un shabdon ko "****" se replace kar dena hai. 
Aapko ek function banana hai jo comment saaf kare.

'''
# def clean_comment(word):
#     clean_text=word.lower().strip()
#     spam_word=["fraud", "spam", "fake"]
#     for i in spam_word:
#         if i in clean_text:
#             clean_text=clean_text.replace(i,'****')
#     return clean_text



# word=input("enter your word")
# result=clean_comment(word)
# print(result)

            
        



'''
Ek middleware dashboard ke liye user ka password mask karna hai. Rule yeh hai ki password 
ka sirf pehla akshar aur aakhri akshar dikhna chahiye, aur beech ke jitne bhi akshars 
hain, unki jagah dynamic * lagne chahiye (jaise tumne email wale code mein (skip - 1) ka '
dimaag lagaya tha). Agar password ki total length 6 se kam hai, toh if not lagakar invalid 
bol do.Hint: String slicing [0] aur [-1] ka khel hai.Input: "python123" $\rightarrow$ Total 
length 9 hai.
 Pehla 'p', aakhri '3', beech me 7 stars $\rightarrow$ Output: "p*******3"
   (Success)Input: 
 "abcd"
   $\rightarrow$ 
 Length 4 hai $\rightarrow$ Output: Error Block Executed! 
(Password too short to mask)

'''

# def password_mask(password):
#     first=password[0]
#     midd=password[1:-1]
#     domain=len(midd)*'*'
#     last=password[-1]
#     result=first+domain+last
#     return result

# password=input("enter your password")
# result=password_mask(password)
# print(result)







'''
Django mein ek web-scraper view bana rahe ho jahan poora URL aata hai 
(jaise "https://google.com" ya "https://github.com"). Aapko slicing aur 
.find() ya .replace() ka use karke sirf beech ka domain name (jaise "google" ya "github") 
baahar nikalna hai. Agar URL "https://" se shuru nahi hota, toh use if not se block 
karo.Hint: "https://" ki length 8 hoti hai, wahan se slice shuru kar sakte ho!Input: 
"https://youtube.com" $\rightarrow$ Output: "youtube" (Success)Input: "http://xyz.com" 
$\rightarrow$ "https://" nahi hai $\rightarrow$ Output: Error Block Executed!

'''
# def is_domain_name(url):
#     clean_url = url.lower().strip()
#     if not clean_url.startswith('https://'):
#         return '❌ galat urls hai'
#     check = clean_url.find('.', 8)
#     domain_name = clean_url[8:check]
    
#     return f'✅ succes {domain_name}'




# url = input("enter your url: ")
# result = is_domain_name(url)
# print(result)