'''Aapko integers ki ek list di hai jisme positive aur negative dono numbers hain. Aapko bina koi nayi list banaye, usi list ke andar elements ko swap karke saare negative numbers ko shuruat (left side) mein lana hai, aur positive numbers ko peeche dhakelna hai.

Real TCS Example: l = [4, -3, 7, -1, -5, 2]

Output: [-3, -1, -5, 4, 7, 2]'''

# def arrange_negative_numbver(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]<0:
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp
#             position=position+1

#     return l


# user=eval(input("enter your list"))
# result=arrange_negative_numbver(user)
# print(result)






'''
Django production database se users ke usernames ki ek list aayi hai. Kuch users ne apna naam dala hai, par kuch fields mein kachra data ya None aur khali strings "" hain. Aapko usi list ke andar loop chalakar saare valid usernames ko uppercase (.upper()) mein badalna hai, aur None ya khali string ko waisa hi chhor dena hai (ya badalna nahi hai).

Real Django Example: usernames = ["maaz", None, "django", "   ", "rits"]

Output: ["MAAZ", None, "DJANGO", "   ", "RITS"]

'''

# def filter_data(l):
#    for i in range(len(l)):
#         if l[i] is not None and isinstance(l[i],str) and l[i].strip():
#               l[i]=l[i].upper()
#    return l



# user=eval(input("enter your list"))
# result=filter_data(user)
# print(result)






'reverse swap list'

# def reverse_list(l):
#     pointer=0
#     length=len(l)-1
#     while pointer<length:
#         temp=l[pointer]
#         l[pointer]=l[length]
#         l[length]=temp
#         pointer=pointer+1
#         length=length-1
#     return l


# user=eval(input("enter your list"))
# result=reverse_list(user)
# print(result)


    
  




'''
Django cart API mein prices ki ek list aayi hai. Agar koi value pure integer (int) hai, toh use waisa hi rkhna hai. Agar koi value string format mein number hai (jaise "250"), toh use int() mein badalna hai. Par agar list mein koi floating number (jaise 99.9), None, ya khali string aa jaye, toh use list se safely delete (filter out) kar dena hai.

Real Django Example: cart = [100, "250", 99.9, None, "   ", 500]

Output: [100, 250, 500]

'''

# def filter_data(l):
#     res=[]
#     for i in l:
#         if i is not None and isinstance(i,str) and i.strip():
#             res.append(int(i))
#         elif isinstance(i,int):
#             res.append(i)
#     return res

# user=eval(input("enter your list"))
# result=filter_data(user)
# print(result)









'''
Aapko mix characters ki ek string S di jayegi. Aapko us string ke andar se sabse lambi 
(longest) aysi continuous string ki length nikaalni hai, jisme koi bhi akshar repeat (dubara) na hua ho.

Yani, aapko string ka wo sabse bada tukda dhoodhna hai jisme saare akshar ekdum unique (alag-alag) hon.

Sample Input 1:

Plaintext
S = "abcabcbb"

'''

def find_longest(s):
    longest=1
    current=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            current=current+1
        else:
            if current>longest:
                longest=current
            current=0
    if current>longest:
        longest=current
    return longest


user=input("enter your word")
result=find_longest(user)
print(result)
