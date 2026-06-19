'''
Replace Element with its Square if it's Even
Sawaal: List ke har element par ghoomo. Agar number even (sam) hai, toh use uske square (usko khud se multiply) 
se badal do, aur agar odd (visham) hai, toh use waise hi chhor do.

Desi Matlab: Ek single for i in range(len(l)) ka loop chalao. if l[i] % 2 == 0 ho toh use change karo, 
else mein kuch mat karo.

Input: [2, 3, 4, 5]

Output: [4, 3, 16, 5]

'''

# def replace_even_its_square(l):
#     for i in range(len(l)):
#         if l[i]%2==0:
#             l[i]=l[i]**2
#     return l


# user=eval(input("enter your list"))
# result=replace_even_its_square(user)
# print(result)







'Find the Element that Appears Once'
# def find_appears_once(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in d:
#         if d[j]==1:
#             return f'apears once is {j}'


# user=eval(input("enter your list"))
# result=find_appears_once(user)
# print(result)






'''
Check Equality of Neighbors (Padosi Check)
Sawaal: Humein list ke un elements ko nikalna hai jinke theek piche wala padosi aur theek aage wala padosi 
ekdum barabar (equal) hon.

Desi Matlab: Wahi Peak Element waala loop range range(1, len(l)-1) chalao. Is baar check karo: 
if l[i-1] == l[i+1].

Input: [1, 2, 1, 3, 1, 4]

Output: [2, 3] (Kyunki 2 ke dono taraf 1 hai, aur 3 ke dono taraf भी 1 hai).
'''

# def check_equality_negihbour(l):
#     res=[]
#     for i in range(1,len(l)-1):
#         if l[i+1]==l[i-1]:
#             res.append(l[i])
#     return res

# user=eval(input("enter your list"))
# result=check_equality_negihbour(user)
# print(result)









'''
 Alternate Positive and Negative ElementsSawaal: List mein se positive ($>0$) 
 aur negative ($<0$) numbers ko chanti karke ek naye list mein alternate (ek positive, 
 ek negative, fir ek positive...) bithana hai.Desi Matlab: Do khali list banao pos = [] aur neg = 
 []. Loop chalao: if i >= 0 toh pos mein daalo, else neg mein daalo. Aakhri mein dono ko alternate jod do.
 Input: 
 [9, -2, 4, -1, 5, -5]Output: [9, -2, 4, -1, 5, -5]

'''

# def alternative_possitive_negative(l):
#     pos=[]
#     neg=[]
#     res=[]
#     for i in l:
#         if i>0:
#             pos.append(i)
#         else:
#             neg.append(i)
#     if len(pos)>len(neg):
#         limit=len(pos)
#     else:
#         limit=len(neg)
#     for i in range(limit):
#         res.append(pos[i])
#         res.append(neg[i])
#     return res



# user=eval(input("enter your list"))
# result=alternative_possitive_negative(user)
# print(result)




'''
Find the First Repeating Element (TCS Round)
Sawaal: List mein shuruat se aage badhte hue aisa pehla number dhoodhna hai jo list mein aage dobara repeat hua ho (duplicate ho).

Desi Matlab: Ek dictionary use karo. Loop chalao: if i in d ho toh turant wahi number return kar do (kyunki wo pehle aa chuka hai), else mein d[i] = True karo.

Input: [10, 5, 3, 4, 3, 5, 6]

Output: 5 (Kyunki shuruat se chalne par 5 sabse pehle repeat hone waala element milta hai).

'''

# def find_first_repeated_element(l):
#     d={}
#     for i in l:
#         if i in d:
#            d[i]=d[i]+1
#         else:
#             d[i]=1
#     for j in d:
#         if d[j]>1:
#             return j
        



# user=eval(input("enter your list"))
# result=find_first_repeated_element(user)
# print(result)






'''
Count Elements with Even Number of Digits
Sawaal: List mein un numbers ko gino jinki total digits (ank) even hain. Jaise 12 mein 2 digits hain (even), par 345 mein 3 digits hain (odd).

Desi Matlab: Loop chalao, har number ko string mein badlo str(i) aur if len(str(i)) % 2 == 0 ho, toh count = count + 1 kar do.

Input: [55, 2, 634, 1234, 9]

Output Count: 2 (Kyunki 55 mein 2 digits hain aur 1234 mein 4 digits hain).

'''
# def count_even_digit(l):
#     count=0
#     for i in l:
#        if len(str(i))%2==0:
#            count=count+1
#     return count

# user=eval(input("enter your list"))
# result=count_even_digit(user)
# print(result)






'''
Replace Every Element with the Sum of its Neighbors
Sawaal: List ke beech waale elements ko badalna hai. Har element ki jagah uske theek piche waale aur theek aage waale padosi ka sum (jod) likhna hai.

Desi Matlab: Peak element waala loop range(1, len(l)-1) chalao. res list pehle se hi input list ke barabar copy kar lo. Fir loop ke andar res[i] = l[i-1] + l[i+1] kar do.

Input: [1, 2, 3, 4, 5]

Output: [1, 4, 6, 8, 5] (Kyunki 2 ki jagah 1+3=4, 3 ki jagah 2+4=6, aur 4 ki jagah 3+5=8).

'''

# def replace_sum_of_neighbour(l):
#     res=list(l)
#     for i in range(1,len(l)-1):
#         replace_sum=l[i-1]+l[i+1]
#         res[i]=replace_sum
#     return res

# user=eval(input("enter your list"))
# result=replace_sum_of_neighbour(user)
# print(result)





'''
Group Elements by their Remainder (Modulus 2)
Sawaal: Dictionary ke andar do keys banani hain: 'even' aur 'odd'. Unke aage un numbers ki list honi 
chahiye jo even ya odd hain.

Desi Matlab: Shuruat me dictionary fixed kar lo: d = {'even': [], 'odd': []}. Loop chalao: if i % 2 == 0 
ho toh d['even'].append(i) karo, else d['odd'].append(i) karo.

Input: [1, 2, 3, 4, 5]

Output: {'even': [2, 4], 'odd': [1, 3, 5]}

'''

# def group_element(l):
#     d={'even':[],'odd':[]}
#     for i in l:
#         if i%2==0:
#             d['even'].append(i)
#         else:
#             d['odd'].append(i)
#     return d

# user=eval(input("enter your list"))
# result=group_element(user)
# print(result)








'''
Map Names to Name-Lengths (Basic Key-Value)
Sawaal: Aapko doston ke naam ki ek list di hai. Ek dictionary banani hai jahan Key dost ka 
naam hoga, aur Value uske naam ki length (letters ki ginti) hogi.

Desi Matlab: d = {} banao. Loop chalao: d[naam] = len(naam) bithate jao.

Input: ["Maaz", "Ali", "Zubair"]

Output: {"Maaz": 4, "Ali": 3, "Zubair": 6}

'''

# def name_key_length_value(l):
#     d={}
#     for i in l:
#         d[i]=len(i)
#     return d


# user=eval(input("enter your list"))
# result=name_key_length_value(user)
# print(result)








'''
Create Index-Mapping of Elements
Sawaal: List mein jo number jis index (position) par baitha hai, uski ek dictionary banani hai, 
jahan Key wo number hoga aur Value uska index hoga.

Desi Matlab: Is baar loop range(len(l)) chalega. d[l[i]] = i bithate jao.

Input: [10, 20, 30]

Output: {10: 0, 20: 1, 30: 2}

'''

# def create_index_mapping(l):
#     d={}
#     for i in range(len(l)):
#         d[l[i]]=i
#     return d


# user=eval(input("enter your list"))
# result=create_index_mapping(user)
# print(result)





'''
Count Votes for Candidates
Sawaal: Ek list mein alag-alag logon ne netaon ko vote diye hain. Kis neta ko kitne vote mile, 
uski ek Key-Value dictionary banani hai (Neta = Key, Votes = Value).

Desi Matlab: d = {} banao. Loop chalao: if neta in d: toh d[neta] = d[neta] + 1, else: d[neta] = 1.

Input: ["Rahul", "Modi", "Rahul", "Rahul"]

Output: {"Rahul": 3, "Modi": 1}


'''


# def count_vote(l):
#     d={}
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     return d


# user=eval(input("enter your list"))
# result=count_vote(user)
# print(result)
