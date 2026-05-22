'''
Ek list ke har number ke andar jao aur uske ek-ek akshar (digit) ko check karo:
Agar wo digit ek Prime Number ($2, 3, 5, 7$) hai, toh use 'P' se replace karo.Agar wo digit prime
nahi hai, toh use 'N' (Non-Prime) se replace karo.Phir saare aksharon ko chipka kar string bana 
!Test Input: l = [543, 29]Hint: * 543 $\rightarrow$ 5 (Prime) $\rightarrow$ 'P', 4 (Not Prime)
$\rightarrow$ 'N', 3 (Prime) $\rightarrow$ 'P'. Ban gaya: "PNP".29 $\rightarrow$ 2 (Prime) 
$\rightarrow$ 'P', 9 (Not Prime) $\rightarrow$ 'N'.
 Ban gaya: "PN".Expected Output: ["PNP", "PN"]
'''

# def replace_digit_prime(l):
#     prime_digit=[2,3,5,7]
#     for i in range(len(l)):
#         digit=str(l[i])
#         res=''
#         for j in digit:
#             if int(j)>1:
#                  if int(j) in prime_digit:
#                      res=res+'P'
#                  else:
#                    res=res+'N'
#             else:
#                 res=res+'j'
#         l[i]=res
#     return l

# user=eval(input("enter your list"))
# result=replace_digit_prime(user)
# print(result)           



            




'''
Question 2: Left-Right Neighbor Max Flusher (Adjacent Comparison)Ek list ke har number
 ke andar jao aur har akshar (digit) ko check karo. Agar koi digit apne ekdam piche waale
(left) aur apne ekdam aage waale (right) DONO aksharon se badi hai, toh use 'X' se replace kar 
do, warna use normal rehne do!(Note: Shuruat aur aakhiri digit ke dono taraf padosi nahi hote,
toh unhe normal chhor dena).Test Input: l = [182, 35461]Hint: * 182 $\rightarrow$ 8 ko dekho,
wo 1 se bhi bada hai aur 2 se bhi. Toh 8 ban gaya 'X'. Output: "1X2".35461 $\rightarrow$ 5 
apne padosiyon (3, 4) se bada hai $\rightarrow$ 'X'. 6 apne padosiyon (4, 1) se bada hai 
$\rightarrow$ 'X'. 
Output: "3X4X1".Expected Output: ["1X2", "3X4X1"]

'''

# def replace_X(l):
#     for i in range(len(l)):
#         digit=str(l[i])
#         res=digit[0]
#         for j in range(1,len(digit)-1):
#             current=int(digit[j])
#             right=int(digit[j+1])
#             left=int(digit[j-1])
#             if current>right and current>left:
#                 res=res+'X'
#             else:
#                 res=res+str(digit[j])
#         res=res+digit[-1]
#         l[i]=res
#     return l


# user=eval(input("enter your list"))
# result=replace_X(user)
# print(result)







'''
Ek list ke andar jao aur check karo ki kya us list mein koi Equilibrium Index hai?
Agar list mein wo index mil jaye, toh us index par jo number baitha hai use mita kar 'EQ' likh do,
 warna baaki saare numbers ko normal rehne do!
'''
# def replace_iqulibrium_index(l):
#     for i in range(1,len(l)-1):
#         left_sum=0
#         right_sum=0
#         for j in range(0,i):
#             left_sum=left_sum+l[j]
#         for k in range(i+1,len(l)):
#             right_sum=right_sum+l[k]
#         if left_sum==right_sum:
#             l[i]='Iq'
#             break
#     return l


# user=eval(input('enter your list'))
# result=replace_iqulibrium_index(user)
# print(result)








'''
Ek list ke har element par jao. Har index par khade hokar check karo:

Agar us index ke Left side ka poora sum aur Right side ka poora sum barabar hai, 
toh us element ko 0 se replace kar do.
'''
# def replace_0_with_iqulibrium(l):
#     for i in range(len(l)):
#         left_sum=0
#         right_sum=0
#         for j in range(0,i):
#             left_sum=left_sum+l[j]
#         for k in range(i+1,len(l)):
#             right_sum=right_sum+l[k]
#         if left_sum==right_sum:
#             l[i]=0  
#     return l


# user=eval(input("enter your list"))
# result=replace_0_with_iqulibrium(user)
# print(result)            




'''

User tumhe ek string dega jisme sirf numbers honge (jaise "12312"). 
Tumhe check karna hai ki string ka kaunsa akshar equilibrium position par hai.
Jahan equilibrium mile,
us akshar ko 'X' se replace kar do!
'''
def check_iqulibrium_digit(n):
    res=''
    for i in range(len(n)):
        iquilibrium_index=''
        left_sum=0
        right_sum=0
        for j in range(0,i):
            left_sum=left_sum+int(n[j])
        for k in range(i+1,len(n)):
            right_sum=right_sum+int(n[k])
        if left_sum==right_sum:
            iquilibrium_index=i
            res=res+'X'
            res=res+n[i+1:]
            break
        else:
            res=res+n[i]
    return f'index no{iquilibrium_index},{res} '

user=input("enter your number")
result=check_iqulibrium_digit(user)
print(result)




   

            
