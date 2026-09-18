'''
Ek username string di gayi hai. Check karo kya us username me kam se kam ek digit (0-9) hai ya nahi.
Input: "rahul_kumar"  Output: FalseInput: "rahul_99" Output: True

'''
# def is_digit(s):
#     res= any(i.isdigit() for i in s)
#     return res

# username=input("enter your name")
# result=is_digit(username)
# print(result)


'''
Ek mixed list di gayi hai. Check karo ki kya list ke saare elements string type ke hain
Input: ["python", "code", "dev"] Output: True Input: ["python", 101, "dev"] Output: False
'''
# def is_all_string(l):
#     res=all(isinstance(i,str) for i in l)
#     return res

# user=eval(input("enter your list"))
# result=is_all_string(user)
# print(result)




'''
Ek filename string di gayi hai (jaise "resume.pdf"). 
Check karo kya file ka extension inme se koi ek hai: ['.pdf', '.docx', '.txt']
Input: "profile.png"  Output: False Input: "document.pdf" Output: True
'''
# def is_valid_file_extenshions(file):
#     allowed_extensions = ('.pdf', '.docx', '.txt')
#     return file.endswith(allowed_extensions)

# user=input("enter your file")
# result=is_valid_file_extenshions(user)
# print(result)




'''
Ek numbers ki list di gayi hai. 
Check karo kya list me kam se kam ek prime number hai.
Input: [4, 6, 8, 9, 11] 
Output: True (11 prime hai)Input: [4, 6, 8, 9, 10] 
Output: False

'''
# def is_prime(n):
#         if n<2:
#             return False

#         elif n==2:
#             return True

#         elif n%2==0:
#             return False
        
#         for i in range(3,int(n**0.5)+1,2):
#              if n%i==0:
#                   return False

        
#         return True

# def is_list_prime(l):
#      return any(is_prime(i) for i in l  )
   


# user=eval(input("enter your list"))
# result=is_list_prime(user)
# print(result)
    



'''
Check karo ki kya ek list ke saare numbers ascending order (chote se bada) me hain.
Input: [2, 5, 8, 19, 25]  Output: True Input: [2, 5, 3, 19, 25] Output: False

'''
# def is_element_assending(l):
#     res=all(l[i]<l[i+1] for i in range(len(l)-1))
#     return res

# user=eval(input("enter your list"))
# result=is_element_assending(user)
# print(result)
        



'''
Sentence me check karo kya koi word capital letter se start ho raha hai
'''

# def is_word_start_capital_letter(word):
#     res=any(i.istitle()for i in word)
#     return res

# word=input("enter your word")
# result=is_word_start_capital_letter(word)
# print(result)


