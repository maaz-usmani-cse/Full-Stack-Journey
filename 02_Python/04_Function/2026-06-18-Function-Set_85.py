'''
Ek list mein se un saare numbers ko dhoodhna hai jo apne aage 
(right side) waale saare numbers se bade hon.
Ise piche se check karte hue aana hai.

[16, 17, 4, 3, 5, 2]

Output: [2, 5, 17]
'''

# def leader_element(l):
#     leader=l[-1]
#     res=[leader]
#     for i in range(len(l)-2,-1,-1):
#         if l[i]>leader:
#             leader=l[i]
#             res.append(l[i])
#     return res


# user=eval(input("enter your list"))
# result=leader_element(user)
# print(result)







'''
Find Peak Element (Neighbor Check)
Sawaal: List mein aisa number dhoodho jo apne aage waale aur apne piche waale... 
dono padosiyon se bada ho (if dono se bada ho).

Desi Matlab: Is baar loop index 1 se shuru hoga aur len(l)-1 tak jayega 
(yani beech waale numbers). Check karna hai: if l[i] > l[i-1] and l[i] > l[i+1].

Input: [1, 3, 20, 4, 1, 0]

'''

# def find_peak_element(l):
#     res=[]
#     for i in range(1,len(l)-1):
#         if l[i]>l[i+1] and l[i]>l[i-1]:
#             res.append(l[i])
#     return res


# user=eval(input("enetr your list"))
# result=find_peak_element(user)
# print(result)









'''
Har ek number ke liye check karo ki uske theek aage (right side) 
wala number usse chota hai ya nahi. 
Agar chota hai toh count badhao.

[12, 1, 2, 3, 0, 11]

Output Count: 2 (Kyunki 12 bada hai 1 se, aur 3 bada hai 0 se).
'''

# def is_right_side_greater(l):
#     count=0
#     for i in range(len(l)-1):
#         if l[i+1]<l[i]:
#             count=count+1
#     return count

# user=eval(input("enter your list"))
# result=is_right_side_greater(user)
# print(result)










'''
Replace with Absolute Difference
Sawaal: Har element ko uske theek aage waale element ke difference 
(bade mein se chota
ghata kar) se replace kar do. Aakhri element ke aage koi nahi hai, toh wahan 0 rakhna
hai.

Desi Matlab: res list pehle se 0 ki bana lo. Loop chalao aur if lagakar l[i] 
aur l[i+1] ka difference nikal kar res[i] mein daalte jao.

Input: [5, 3, 8, 10]

Output: [2, 5, 2, 0] (Kyunki 5-3=2, 8-3=5, 10-8=2, aur aakhri wala 0).

'''

# def replace_absoloute_diff(l):
#     for i in range(len(l)-1):
#         diffrence=None
#         if l[i]>l[i+1]:
#             diffrence=l[i]-l[i+1]
#             l[i]=diffrence
#         else:
#             diffrence=l[i+1]-l[i]
#             l[i]=diffrence
#     l[-1]=0
#     return l


# user=eval(input("enter your list"))
# result=replace_absoloute_diff(user)
# print(result)








'''
 Count Elements Greater Than All Previous Elements (Infosys Round)Sawaal: 
 List mein shuruat se aage badhte hue un numbers ko gino (count karo) jo 
 apne piche aane waale saare numbers se bade hon.Desi Matlab: Pehle element ko 
 sabse bada maan lo (max_so_far = l[0]). Aage badhte hue if l[i] > max_so_far ho, 
 toh count = count + 1 karo aur max_so_far ko update kar do.Input: [10, 20, 30, 40, 
 50] $\rightarrow$ Output: 5 (Kyunki har number piche waale se bada hai).Input: 
 [10, 5, 8, 20, 15] $\rightarrow$ Output: 2 
 (Sirf 10 aur 20 hi apne piche waalon se bade hain).
'''

# def count_greater_previous_element(l):
#     count=0
#     max_so_far=l[0]
#     for i in range(len(l)-1):
#         if l[i+1]>max_so_far:
#             count=count+1
#             max_so_far=l[i]
#     return count

# user=eval(input("enter your list"))
# result=count_greater_previous_element(user)
# print(result)
        










'Move All Zeros to End'
# def move_all_zero(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]!=0:
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp
#             position=position+1
#     return l

# user=eval(input("enter your list"))
# result=move_all_zero(user)
# print(result)
