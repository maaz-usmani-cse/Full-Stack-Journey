'''
Aapko ek names (naam) ki list di hai. Aapko ek aisi dictionary banani hai 
jisme saare naam unke pehla akshar (first letter) ke hisab se group ho jayein.
Real Example: ["Maaz", "Amit", "Mohit", "Rahul", "Ankit"]
Output: {'M': ['Maaz', 'Mohit'], 'A': ['Amit', 'Ankit'], 'R': ['Rahul']}

'''

# def group_by_first_letter(l):
#     d={}
#     for i in l:
#         if i[0] in d:
#             d[i[0]].append(i)
#         else:
#             d[i[0]]=[i]
#     return d

# user=eval(input("enter your list"))
# result=group_by_first_letter(user)
# print(result)







'''

 Ek numbers ki list di hai aur ek diff (difference) diya hai. Aapko batana hai 
 ki kya list mein koi bhi aisi do numbers ki jodi hai jinka aapas ka antar
(subtraction) diff ke barabar ho? Agar hai, toh True return karo, nahi toh False.
Real Example: nums = [1, 5, 3, 4, 2], diff = 3 $\rightarrow$ Output: True (Kyunki $5 - 2 = 3$ ya $4 - 1 = 3$).


'''

# def has_pair_of_diff(l,diff):
#     d={}
#     for i in l:
#         d[i]=True
#     for j in d:
#         required=j-diff
#         if required in d:
#             return True
#     return False

# user=eval(input("enter your list"))
# diff=int(input("enter your number"))
# result=has_pair_of_diff(user,diff)
# print(result)






'''
Ek string di hai. Aapko uske har ek akshar (character) 
ko is cheez se replace karna hai ki wo poore string mein 
kitni baar aaya hai. Output string hi hona chahiye.
Real Example: "apple" $\rightarrow$ Output: "12211"
(Kyunki 'a' 1 baar hai, 'p' 2 baar hai, 'l' 1 baar, 'e' 1 baar).

'''

# def replace_with_frequency(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     res=''
#     for j in s:
#        res=res+str(d[j])
#     return res 

# user=input("enter your word")
# result=replace_with_frequency(user)
# print(result)

  




'''
Replace Elements with Next Greater
Element using Map (TCS Elite / Infosys SP)
'''

# def next_greater(l):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[j]>l[i]:
#                 temp=l[i]
#                 l[i]=l[j]
#                 l[j]=temp
#                 break

#     return l


# user=eval(input("enter your list"))
# result=next_greater(user)
# print(result)





'''
Ek list di hai jisme ek special number -1 bhara hai kai jagah 
(matlab data missing hai). Aapko is -1 ko us number se replace karna hai 
jo list mein sabse zyada baar (maximum times) aaya hai.
Real Example: [1, 3, -1, 2, 3, -1, 3] $\rightarrow$ Output: 
[1, 3, 3, 2, 3, 3, 3]
'''

# def replace_mostfrequent_element(l):
#      d={}
#      for i in l:
#           if i in d:
#                d[i]=d[i]+1
#           else:
#                d[i]=1
#      max_value=None
#      max_elemnt=None
#      for j in d:
#           if max_value is None or d[j]>max_value:
#                max_value=d[j]
#                max_elemnt=j
#      for i in range(len(l)):
#           if l[i]==-1:
#                l[i]=max_elemnt
#      return l


# user=eval(input("entr your list"))
# result=replace_mostfrequent_element(user)
# print(result)
          
          





'''
Aapko validate karna hai ki kya koi ek bhi file aisi hai jo
.exe ya .bat (dangerous extension) ki hai? Agar hai, toh form ko reject
karna hai.
Real Input: ['resume.pdf', 'photo.jpg', 'virus.exe', 'marksheet.pdf']

'''


# def validate_data(l):
#     res=any(i.endswith('.exe')for i in l )
#     if res:
#         return 'dangerous file'
#     else:
#         return 'not dangerous'
    
# user=eval(input("enter your list"))
# result=validate_data(user)
# print(result)








