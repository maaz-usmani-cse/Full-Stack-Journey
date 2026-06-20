'''
Bilkul Next Greater jaisa hai, bas is baar aapko har element ke liye uske theek aage (right side) waala 
sabse pehla chota (smaller) number dhoodhna hai. Agar koi chota na mile, toh -1.

Desi Logic: Shuruat me res = [-1] * len(l) banao. Reverse loop chalao. if l[i+1] < l[i]: ho toh answer 
padosi ho gaya. elif res[i+1] < l[i]: ho toh answer padosi ka jodidaar ho gaya! (Bas sign badal jayega).

Input: [4, 5, 2, 10]

Output: [2, 2, -1, -1] (Kyunki 4 ke aage sabse pehla chota 2 hai, 5 ke aage 2 hai, aur 2 aur 10 ke aage koi 
chota nahi hai).

'''
# def replace_next_smallest(l):
#     res=[-1]*len(l)
#     for i in range(len(l)-2,-1,-1):
#         if l[i+1]<l[i]:
#             res[i]=l[i+1]
#         elif res[i+1]<l[i]:
#             res[i]=res[i+1]
#     return res

# user=eval(input("enter your list"))
# result=replace_next_smallest(user)
# print(result)




'''
Next Greater Element II (Circular Array)
Sawaal: Sawaal bilkul wahi hai, bas is baar list khatam hone par aap dobara shuruat se check kar sakte ho 
(circular fashion mein).

Desi Logic: Agar koi element aakhri mein hai, toh wo dobara index 0 se check karna shuru karega. Isko karne ke 
liye hum input list ko do baar jod dete hain (l = l + l) aur fir wahi purana Next Greater wala logic chala dete 
hain!

Input: [1, 2, 1]

Output: [2, -1, 2] (Pehle 1 ka next greater 2 hai. 2 ke aage koi nahi hai aur ghoom kar bhi koi bada nahi 
mila toh -1.

'''

# def replace_next_greater_circular(l):
#     res=[-1]*len(l)
#     for i in range(len(l*2)-1,-1,-1):
#         current_index=(i%len(l))
#         next_index=((i+1)%len(l))
#         if l[next_index]> l[current_index]:
#             res[current_index]=l[next_index]
#         elif res[next_index]>l[current_index] and res[next_index] != -1:
#             res[current_index]=res[next_index]
#     return res




# user=eval(input("enter your list"))
# result=replace_next_greater_circular(user)
# print(result)
        





'''
. Check for Negative NumbersSawaal: Aapko ek numbers ki list di hai. 
Pata karo ki kya list ke andar ek bhi number negative (< 0) hai?Input: 
[3, 5, -1, 8, 12] $\rightarrow$ Output: True (Kyunki -1 negative hai).Input: 
[1, 2, 3] $\rightarrow$ Output: False

'''

# def is_negative_number(l):
#     res=any(i<0 for i in l)
#     return res


# user=eval(input("enter your list"))
# result=is_negative_number(user)
# print(result)




'''


Target Element Matcher
Sawaal: Ek nested list (list ke andar list) di hai. Pata karo ki kya poori nested 
list mein kahin bhi hamara target number baitha hai?

Input: l = [[1, 2], [3, 4], [5, 6]], target = 4


'''

# def is_targtet_number(l,target):
#     res=any(target in i for i in l )
#     return res


# user=eval(input("enter your list"))
# target=int(input("enter your target number"))
# result=is_targtet_number(user,target)
# print(result)






'''
Check for None or Empty ValuesSawaal: Ek database se aayi hui data list hai. 
Pata karo ki kya list mein koi value None ya khali string "" hai, taaki humein 
pata chal sake data corrupt hai ya nahi.Input: ["Bhopal", "Bihar", "", "Delhi"] $\rightarrow$ Output: True 
(Kyunki beech mein ek khali string "" hai).
'''

def is_clean_data(l):
    res=any(isinstance ,str) and i.strip() for i in l if i is not None)
    return res


user=eval(input("enter your list"))
result=is_clean_data(user)
print(result)