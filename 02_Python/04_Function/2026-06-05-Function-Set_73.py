''''
Ek string di hai. Agar usme lagatar (consecutive) ek jaise akshar aayein, 
toh unhe hata kar sirf ek akshar chhodna hai.
Real Example: "aaabbccba" $\rightarrow$ Output: "abcba"

'''
# def del_dublicate(s):
#     res=''
#     for i in range(len(s)-1):
#         if s[i]!=s[i+1]:
#             res=res+s[i] 
#     res= res+s[-1] 
#     return  res


# user=input("enter your word")
# result=del_dublicate(user)
# print(result)










'''
Aapko batana hai ki kya di gayi list Monotonic hai ya nahi? Monotonic ka
matlab hota hai ki list ya toh lagatar badh rahi ho (Increasing) ya fir 
ghat rahi ho (Decreasing). Beech mein sequence tootna nahi chahiye.
Real Example 1: [1, 2, 2, 3] $\rightarrow$ Output: True (Badh rahi hai)
Real Example 2: [6, 5, 4, 4] $\rightarrow$ Output: True (Ghat rahi hai)
Real Example 3: [1, 3, 2, 4] $\rightarrow$ Output: False

'''


# def is_monotonic(l):
#     increase=True
#     decrease=True
#     for i in range(len(l)-1):
#         if l[i]>l[i+1]:
#             increase=False
#         if l[i]<l[i+1]:
#             decrease=False
#     if increase or decrease:
#         return True
#     else:
#         return False
    

# user=eval(input("enter your list"))
# result=is_monotonic(user)
# print(result)
    




            




'''
Aapko do choti strings di hain, s1 aur s2. Aapko batana hai ki kya dono strings 
mein ekdum same akshar use hue hain, bhale hi unka aage-piche ka sequence alag ho? 
(Isi ko coding mein Anagram kehte hain).
Real Example 1: s1 = "listen", s2 = "silent" $\rightarrow$ Output: True
Real Example 2: s1 = "rat", s2 = "car" $\rightarrow$ Output: False

'''

def is_anagram(s1,s2):
    d={}
    d2={}
    for i in s1:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    for j in s2:
        if j in d2:
            d2[j]=d[j]+1
        else:
            d2[j]=1
    if d==d2:
        return f'yes anagram hai'
    else:
        return f'anagram nahi hai'


s1=input("eter your word")
s2=input("eter your word")
result=is_anagram(s1,s2)
print(result)

