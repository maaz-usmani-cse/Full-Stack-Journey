'''
Aapko do strings di hain, s1 aur s2. Aapko batana hai ki kya s2 ko thoda ghumane (rotate karne) par s1 ban sakti hai?
Real Example 1: s1 = "amazon", s2 = "azonam" $\rightarrow$ Output: True (Kyunki 'amazon' ke shuruat ke 'am' ko piche bhej dein toh 'azonam' ban jata hai).
Real Example 2: s1 = "amazon", s2 = "azonma" 


'''


# def is_rotation(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     lambistring=s1+s1
#     if s2 in lambistring:
#         return True
#     else:
#         return False
    

# s1=input("enter your word")
# s2=input("enteryour word")
# result=is_rotation(s1,s2)
# print(result)





'''
Aapko do strings di hain, badi_string aur choti_string. Aapko batana hai ki kya choti_string is badi_string ke andar lagatar 
(continuous) baithi hai ya nahi? Niyam: Python ka in keyword ya .find() 
function use NAHI karna hai! Poora manual loop chalana hai.
Real Example 1: badi_string = "bhopal", choti_string = "hop" $\rightarrow$ Output: True
Real Example 2: badi_string = "bhopal", choti_string = "hpl" $\rightarrow$ Output: False (Kyunki 'h', 'p', 'l' alag-alag hain, lagatar nahi hain).
'''

# def is_smallstring_continously_repeat(s1,s2):
#     for i in range(len(s1)-len(s2)+1):
#         tukda=s1[i:i+len(s2)]
#         if tukda==s2:
#             return True
#         else:
#             return False
        
    
# s1=input("enter your word")
# s2=input("enetr your word")
# result=is_smallstring_continously_repeat(s1,s2)
# print(result)








'''

Aapko numbers ki ek list di hai. Agar koi number us list mein 2 baar se ZYADA 
(yani 3 ya 3 se zyada baar) aaya hai, toh us number ki saari jagahon par
aapko badal kar string "REPEATED" likhna hai. Aur jo numbers 2 ya 2 se kam baar aaye hain,
unhe waise ka waise hi chhod dena hai.

'''

# def replace_repeat_greater2(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for i in range(len(l)):
#         element=l[i]
#         if d[element]>2:
#             l[i]='repeated'
#     return l


# user=eval(input("enter your list"))
# result=replace_repeat_greater2(user)
# print(result)
    




'''
Aapko ek list di hai. Jo number list mein sirf ek hi baar (exactly 1 time) aaya hai, 
use badal kar uski jagah 0 likh do. Aur jo repeat hue hain, unhe waise hi chhod do.
Real Example: l = [4, 5, 4, 6, 7, 5] $\rightarrow$ Output: [4, 5, 4, 0, 0, 5]

'''

# def replace_only_onetime(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for i in range(len(l)):
#         element=l[i]
#         if d[element]==1:
#             l[i]=0
#     return l

# user=eval(input("enter your list"))
# result=replace_only_onetime(user)
# print(result)






'''
Aapko ek list di hai. Agar koi number list mein Odd number of times 
(jaise 1 baar, 3 baar, या 5 baar) aaya hai, toh use badal kar string "ODD" likh do. 
Jo Even baar (2, 4 baar) aaye hain, unhe mat chhedo.
Real Example: l = [1, 1, 1, 2, 2, 3] $\rightarrow$ Output:
["ODD", "ODD", "ODD", 2, 2, "ODD"]
'''

# def replace_odd_items(l):
#     for i in range(len(l)):
#         if l[i]%2!=0:
#             l[i]='odd'
#     return l


# user=eval(input("enter your list"))
# result=replace_odd_items(user)
# print(result)




'''
Move All Zeros to the End
 '''


# def move_zero(l):
#     pointer=0
#     for i in range(len(l)):
#         if l[i]!=0:
#             temp=l[pointer]
#             l[pointer]=l[i]
#             l[i]=temp
#             pointer=pointer+1
#     return l

# user=eval(input("enter your list"))
# result=move_zero(user)
# print(result)







'''
Ek list mein kisi element ko "Leader" tab kehte hain, jab wo apne daayein 
(right) taraf ke saare elements se bada ho. Sabse aakhri wala element hamesha 
leader hota hai kyunki uske right mein koi nahi hota. Aapko list ke saare leader elements
dhoodh kar batane hain.
Real Example: l = [16, 17, 4, 3, 5, 2] $\rightarrow$ Output: [17, 5, 2]

'''

# def find_leader(l):
#     leader=[]
#     max_digit=l[-1]
#     leader.append(max_digit)
#     for i in range(len(l)-2,-1,-1):
#         if l[i]>max_digit:
#             leader.insert(0,l[i])
#             max_digit=l[i]
#     return leader

# user=eval(input("enter your list"))
# result=find_leader(user)
# print(result)








'''
Aapko ek list di hai. Aapko ek nayi list banani hai jahan har index par baki
saare numbers ka guna (product/multiplication) baitha ho, par us index wale khud ke
number ko chhod kar.
Real Example: l = [1, 2, 3, 4] $\rightarrow$ Output: [24, 12, 8, 6]

'''

# def product_except_self(l):
#     final_res=[1]*len(l)
#     left_multiply=1
#     for i in range(len(l)):
#         final_res[i]=left_multiply
#         left_multiply=left_multiply*l[i]

#     right_multiply=1
#     for j in range(len(l)-1,-1,-1):
#         final_res[j]=final_res[j]*right_multiply
#         right_multiply=right_multiply*l[j]
#     return final_res

# user=eval(input("enter your list"))
# result=product_except_self(user)
# print(result)






'''
Ek string di hai. Aapko batana hai ki poori string mein sabse pehla aisa kaun sa akshar hai 
jo repeat nahi hua
(uski frequency exactly 1 hai). Agar aisa koi akshar nahi hai toh -1 return karo.
Real Example: s = "apple" $\rightarrow$ Output: 'a' (Kyunki 'a' ek hi baar aaya hai
aur sabse pehle hai. 'p' toh repeat ho gaya).

'''
# def non_repeated_element(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in d:
#         if d[j]==1:
#             return j
        

# user=input("enter your word")
# result=non_repeated_element(user)
# print(result)





'''

Aapko ek string di hai. Aapko batana hai ki usme kitne Vowels (a, e, i, o, u)
hain aur kitne Consonants (baki bache akshar) hain? Space aur special characters
ko chhod dena hai.Real Example: s = "tcs digital" 
$\rightarrow$ Output: Vowels: 3, Consonants: 7💡 Hint:

'''
# def vowel_consonant_count(s):
#     vowel=0
#     consonant=0
#     for i in s:
#         if i.isalpha():
#             if i in ['a','i','e','i','o','u']:
#                 vowel=vowel+1
#             else:
#                 consonant=consonant+1
#     return vowel,consonant

# user=input("enter your word")
# result=vowel_consonant_count(user)
# print(result)




# def find_missing(l):
#     d={}
#     for i in l:
#         d[i]=True

#     for j in range(1,len(l)+1):
#         if i not in d:
#             return f'missing value is {i}'
    
# user=eval(input("enter your list"))
# result=find_missing(user)
# print(result)




