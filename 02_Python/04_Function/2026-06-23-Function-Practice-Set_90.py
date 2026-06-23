'''
Remove Target Element (LeetCode Classic)
Interviewer Bola: "Maaz, aapko ek list di hai aur ek target number diya hai. Mujhe us list mein se saare target 
waale numbers ko hata dena hai, aur baaki bache numbers ko aage khiska dena hai. Koi extra space nahi chahiye, jo 
badlav hoga usi list mein hoga!"

Hint: Ek pointer i (deewar) rakho jo sirf un elements ko jagah dega jo target ke barabar nahi hain, 
aur j se poori list scan karo.

Input: l = [3, 2, 2, 3], target = 3

Output: [2, 2] (Dono 3 gayab aur bache hue 2 aage aa gaye).
'''

# def remove_target_element(l,target):
#     j=0
#     for i in range(len(l)):
#        if l[i]!=target:
#            l[j]=l[i]
#            j=j+1
#     return l[:j]


# user=eval(input("enter your list"))
# target=int(input("enter your target"))
# result=remove_target_element(user,target)
# print(result)







'Move All Zeroes to the End'
# def move_allzeroes(l):
#     position=0
#     for i in range(len(l)):
#         if l[i]!=0:
#             temp=l[position]
#             l[position]=l[i]
#             l[i]=temp
#             position=position+1
#     return l

# user=eval(input("enter your list"))
# result=move_allzeroes(user)
# print(result)







'remove dublicate item'
# def remove_dublicate(l):
#     j=0
#     for i in range(len(l)-1):
#         if l[i]!=l[i+1]:
#             l[j]=l[i]
#             j=j+1
#     return l[:j]



# user=eval(input("enter your list"))
# result=remove_dublicate(user)
# print(result)




'Reverse the Array In-Place'

# def reverse_list(l):
#     for i in range(len(l)//2):
#         piche_ka_index=len(l)-1-i
#         temp=l[piche_ka_index]
#         l[i]=piche_ka_index
#         l[piche_ka_index]=temp
#     return l

# user=eval(input("enter your list"))
# result=reverse_list(user)
# print(result)




