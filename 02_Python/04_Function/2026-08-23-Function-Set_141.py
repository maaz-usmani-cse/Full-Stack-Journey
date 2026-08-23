'''
Ek binary string mein koi bhi do adjacent character same nahi hone chahiye (e.g. "010101..."). Aisa banane ke liye minimum kitne characters badalne padenge?

Input: s = "111000"

Expected Output: 2 (Isse "101010" banaya ja sakta hai 2 flips mein)

'''

# def min_flip(s):
#     flips_even=0
#     flips_odd=0
#     for i in range(len(s)):
#         expected_even='0' if i%2==0 else '1'
#         if s[i]!=expected_even:
#             flips_even+=1

#         expected_odd='1' if i%2==0 else '0'
#         if s[i]!=expected_odd:
#             flips_odd+=1

#     if flips_even<flips_odd:
#         return f'minimum character channge{flips_even}'
#     else:
#         return f'minimum character change {flips_odd}'


# user=input("enter your word")
# result=min_flip(user)
# print(result) 




'''
List mein un sabhi numbers ko dhundho jo apne pichle aur agle dono padosi elements se strictly bade hain.

Input: nums = [1, 3, 2, 5, 4, 7, 1]

Expected Output: [3, 5, 7]
'''

# def find_leaders(l):
#     leader=[]
#     for i in range(1,len(l)-1):
#         if l[i]>l[i+1] and l[i]>l[i-1]:
#             leader.append(l[i])
#     return leader

# user=eval(input("enter your list"))
# result=find_leaders(user)
# print(result)





'''
String ke har consecutive duplicate character ke beech ek dash '-' lagao.

Input: s = "balloon"

Expected Output: "bal-lo-on"
'''
# def dashed_betwene_consecutive_dublicate(s):
#     res=''
#     for i in range(len(s)-1):
#         if s[i+1]==s[i]:
#             res = res+  s[i]+'-' 
#         else:
#             res+=s[i]
#     res+=s[-1]
#     return res


# user=input('enter your word')
# result=dashed_betwene_consecutive_dublicate(user)
# print(result)








'''
String mein total kitne alag-alag continuous groups hain unki count return karo.

Input: s = "aaabbcaadd"

Expected Output: 5 (Groups: 'aaa', 'bb', 'c', 'aa', 'dd')

'''

# def total_consecutive_continuous_group(s):
#     d={}
#     count=1
#     for i in range(1,len(s)):
#         if s[i]!=s[i-1]:
#             count+=1

#     return count

# user=input("enter your word")
# result=total_consecutive_continuous_group(user)
# print(result)





'''
Ek sentence mein se sirf wahi words filter karo jinme koi letter continuous repeat ho raha ho (jaise 'oo', 'll', 'ee').

Input: sentence = "the little book is on the green floor"

Expected Output: ['little', 'book', 'green', 'floor']

'''

# def filter_word_in_repeated_continuous_letter(s):
#     s=s.split()
#     res=[]
#     for word in s:
#         for j in range(1,len(word)):
#             if word[j]==word[j-1]:
#                 res.append(word)
#                 break
#     return res

# user=input("enter your word")
# result=filter_word_in_repeated_continuous_letter(user)
# print(result)

        



