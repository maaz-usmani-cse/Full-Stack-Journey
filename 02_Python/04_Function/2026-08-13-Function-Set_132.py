'''
Encoded string se original string wapas generate karo.

Input: s = "a3b2c1a2"

Expected Output: "aaabbca"

'''
# def decompress_string(s):
#     res=''
#     for i in range(0,len(s),2):
#         char=s[i]
#         count=int(s[i+1])
#         res=res+char*count
#     return res


# user=input("enter your word")
# result=decompress_string(user)
# print(result)




'''
Agar koi character lagaataar (consecutive) repeat ho raha hai, toh use single character mein convert kar do.

Input: s = "aaabbcddda"

Expected Output: "abcda"

'''

# def remove_consecutive_char(s):
#     res=''
#     res=s[0]
#     for i in range(1,len(s)):
#         if s[i]!=s[i-1]:
#             res=res+s[i]
#     return res

# user=input("enter your word")
# result=remove_consecutive_char(user)
# print(result)








'''
Reverse Words Without Built-in Shortcuts
Task: Sentence ke har word ko reverse karo, lekin word order same rehna chahiye (bina split() ya [::-1] use kiye).

Input: s = "hello world python"

Expected Output: "olleh dlrow nohtyp"
'''

# def reverse_word_without_built_in(s):
#     res=''
#     current_word=''
#     for i in s:
#         if i!=' ':
#             current_word=i+current_word

#         else:
#             res=res+current_word+' '
#             current_word=''
#     res=res+current_word
#     return res



# user=input("enter your word")
# result=reverse_word_without_built_in(user)
# print(result)










'check number is pallindrom or not'

# def is_number_pallindrom(n):
#     n=str(n)
#     rev=''
#     for i in n:
#         rev=i+rev
#     if rev==n:
#         return True
#     return False

# user=int(input("enter your number"))
# result=is_number_pallindrom(user)
# print(result)






'harshad number check kro'

# def is_harshad_number(n):
#     n=str(n)
#     total=0
#     for i in n:
#         total=total+int(i)
#     if int(n)%total==0:
#         return 'harsdah number hai'

#     return 'harshad number nahi hai'


# user=int(input("enter your number"))
# result=is_harshad_number(user)
# print(result)






