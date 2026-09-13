'''
Ek string di gayi hai. Generator expression use karke check karo kya string me koi vowel (a, e, i, o, u) hai ya nahi (case-insensitive hona chahiye).

'''
# def is_vowel(s):
#     s=s.lower()
#     vowel='aeiou'
#     v=any(i in s for i in vowel)
#     return v

# user=input("enter your word")
# result=is_vowel(user)
# print(result)



'''
Ek password string di gayi hai. Check karo ki kya usme kam se kam 
ek special character maujood hai inme se: "!@#$%^&*"
'''
# def is_special_char(s):
#     speacial="!@#$%^&*"
#     res=any(i in s for i in speacial)
#     return res

# password=input("ENTER your password")
# result=is_special_char(password)
# print(result)




'''
Ek sentence ke words ki list di gayi hai. Check karo ki kya har
ek word Title Case me hai (matlab pehla letter capital ho,

["Hello", "World", "Python"],
["Hello", "world", "Python"]
'''
# def is_word_title_case(l):
#     res=all(i.istitle() for i in l)
#     return res

# user=eval(input("enter your list"))
# result=is_word_title_case(user)
# print(result)




'''
Form submission se strings ki list aayi hai. Check karo ki kya saari strings non-empty hain (kisi ki bhi length 0 ya sirf spaces nahi honi chahiye).
["admin", "user1", ""]
["admin", "user1", "guest"]
'''
# def is_valid_details(l):
#     res=all(i and i.strip() for i in l)
#     return res

# user=eval(input("enter your list"))
# result=is_valid_details(user)
# print(result)



'''
Ek student ke 5 subjects ke marks diye gaye hain: 
marks = [65, 78, 38, 90, 55]. Passing mark 40 hai.
Function banao jo True return kare agar student saare subjects me pass hai.
Input: [65, 78, 38, 90, 55]  Output: False (38 par fail hai)
'''
# def is_pass_student(marks):
#     res=all(i>=40 for i in marks)
#     return res

# user=eval(input("enter your list"))
# result=is_pass_student(user)
# print(result)


'''
Ek list di gayi hai words ki. Check karo kya list me kam se kam ek word Palindrome hai (jo aage-peeche se same ho).
["car", "code", "level", "tech"]
'''
# def is_pallindrom(l):
#     res=any(i==i[::-1] for i in l)
#     return res


# user=eval(input("enter your list"))
# result=is_pallindrom(user)
# print(result)