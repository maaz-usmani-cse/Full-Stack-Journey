'''
String ko consecutive count format (jaise "a3b2") mein compress karo, lekin compressed string tabhi 
return karo agar uski length original string se choti ho. Agar choti na ho, toh original string hi return karo.Input 1: s = "aabcccccaaa" $\rightarrow$ Output: "a2b1c5a3" (Compressed choti hai)Input 2: 
s = "abc" $\rightarrow$ Output: "abc" (Kyunki compressed "a1b1c1" lambi hai)

'''
# def  consecutice_count_compress(s):
#     res=''
#     count=1
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             count=count+1
#         else:
#             res=res+s[i]+str(count)
#             count=1
#     res=res+s[i]+str(count)

#     if len(res)<len(s):
#         return res
    
#     return s

# user=input("entet your word")
# result=consecutice_count_compress(user)
# print(result)
    




'''
String mein agar do same characters bagal-bagal aate hain toh dono ko delete kar do. Yeh process tab tak repeat karo jab tak koi pair na bache.

Input: s = "baab"
Expected Output: "" (Explanation: 'aa' delete hua $\implies$ bacha 'bb', phir 'bb' delete hua $\implies$ empty)
'''
# def remove_consecutive_char(s):
#     l=[]
#     for i in l:
#         if l and i==[-1]:
#             l.pop()
#         else:
#             l.append(i)
#     return ''.join(l)

# user=input("enter your word")
# result=remove_consecutive_char(user)
# print(result)