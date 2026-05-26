'k target pair'
# def k_target(l,k):
#     pair=[]
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[i]+l[j]==k:
#                 pair.append((l[i],l[j]))
#     return pair


# user=eval(input("enter your list"))
# target=int(input("entr your number"))
# result=k_target(user,target)
# print(result)








'''
Maan lo tumhaare paas ek list hai numbers ki. Interviewer ne bola: 
"Maaz, mujhe aisi sequence ki lambai (length) nikaalni hai jo ek baar badhe (+),
fir ek baar ghate (-), fir badhe (+), fir ghate (-). Yaani consecutive elements 
badhte-ghatate rehne chahiye (Zig-Zag pattern)!"
numbers = [1, 5, 2, 8, 3, 1, 9, 4]
'''
# def check_zigzag_pattern(l):
#     if len(l) < 2:
#         return len(l)
        
#     longest = 1
#     current = 1
#     expecting_up = None 
#     for i in range(len(l) - 1):
#         if expecting_up is None:
#             if l[i+1] > l[i]:
#                 expecting_up = False 
#                 current += 1
#             elif l[i+1] < l[i]:
#                 expecting_up = True 
#                 current += 1
#             continue


#         if expecting_up and l[i+1] > l[i]:
#             current += 1
#             expecting_up = False
#         elif not expecting_up and l[i+1] < l[i]:
#             current += 1
#             expecting_up = True  
    
#         else:
          
#             if current > longest:
#                 longest = current
                
           
#             if l[i+1] != l[i]:
#                 current = 2
#                 expecting_up = False if l[i+1] > l[i] else True
#             else:
#                 current = 1
#                 expecting_up = None
#     if current > longest:
#         longest = current
        
#     return longest




# numbers = [1, 5, 2, 8, 3, 1, 9, 4]
# result=check_zigzag_pattern(numbers)
# print(result)










'''
Tumhe ek list di jayegi numbers ki. Tumhe loop chala kar ek aisa element dhoondhna hai jo apne bagal
waale dono elements se bada ho (yaani l[i] > l[i-1] AND l[i] > l[i+1]). Ise "Peak Element" kehte hain.

Challenge: Agar list mein aise 2-3 peak elements hain, toh mujhe un sabhi peaks ka index aur value 
chahiye.

Test Input: l = [1, 3, 20, 4, 1, 0, 8, 5]
Expected Output: Peaks found at index 2 (value 20) and index 6 (value 8).

'''

# def find_peak_element(l):
#     peak_index=[]
#     peak_element=[]
#     for i in range(1,len(l)-1):
#        if l[i]>l[i+1] and l[i]>l[i-1]:
#            peak_element.append(l[i])
#            peak_index.append(i)
#     return peak_element,peak_index


# user=eval(input("enter your list"))
# result=find_peak_element(user)
# print(result)









'''

Puraane question mein hum strictly ascending (l[i+1] > l[i]) dhoond rahe the. Is baar interviewer ne bola: "Maaz,
 mujhe aisi sequence ki length chahiye jahan numbers ya toh badhein ya phir barabar rahein (l[i+1] >= l[i]), ghatna nahi chahiye!"

Challenge: Pattern tootne par else ke andar tum current = 2 karoge ya current = 1? Soch samajh kar condition lagana agar do numbers barabar hue toh!

Test Input: l = [1, 2, 2, 3, 1, 4, 5]

Expected Output: 6 (Kyunki [1, 2, 2, 3] aur aage tak ka stretch sabse bada hai).


'''
# def non_decreasing_strength(l):
#     current=1
#     longest=1
#     for i in range(len(l)-1):
#         if l[i+1]>=l[i]:
#             current=current+1
#         else:
           
#                 longest=current
#                 current=1
#     if current>longest:
#         longest=current

#     return longest



# user=eval(input("entr your list"))
# result=non_decreasing_strength(user)
# print(result)











'''
Ek list mein kisi element ko "Leader" tab kehte hain jab uske right side (aage) waale saare elements usse chhote hon.
 List ka sabse aakhiri element hamesha leader hota hai. Tumhe saare leaders dhoondhne hain.

Challenge: Isko agar tum seedha loop se karoge toh har element ke liye aage check karna padega (Slow ho jayega). 
Tumhe ise list ke aakhir se shuru karke (Reverse Loop) chala kar ek hi baar mein solve karna hai!

Test Input: l = [16, 17, 4, 3, 5, 2]

Expected Output: Leaders: [17, 5, 2] (Kyunki 17 ke aage sab chhote hain, 5 ke aage sab chhote hain, aur 2 aakhiri hai).

'''

# def leader_element(l):
#     leader_element=[]
#     max_from_right=l[-1]
#     leader_element.insert(0,max_from_right)
#     for i in range(len(l)-2,-1,-1):
#         if l[i]>max_from_right:
#             leader_element.insert(0,l[i])
#             max_from_right=l[i]
#     return leader_element




# user=eval(input("enter your list"))
# result=leader_element(user)
# print(result)  






'''
Mujhe sirf wahi students chahiye jinki CGPA 7.5 
ya usse zyada ho aur unka koi backlog
na ho (has_backlog == False).

'''
# students = [
#     {"name": "Maaz", "cgpa": 8.5, "has_backlog": False},
#     {"name": "Rohit", "cgpa": 6.2, "has_backlog": True},
#     {"name": "Amit", "cgpa": 7.8, "has_backlog": False},
#     {"name": "Suresh", "cgpa": 5.9, "has_backlog": False},
#     {"name": "Vikram", "cgpa": 9.1, "has_backlog": True}
# ]
# result=list(filter(lambda x:'cgpa' in x and x['cgpa']>=7.5 and x['has_backlog'],students))
# print(result)







'''
Jo students eligible hain, mujhe unka poora data nahi chahiye!
Mujhe unke naam ke aage " - Eligible for Interview" 
likh kar ek nayi list chahiye!
'''


# def filter_eligible_stutedt(l):
#     res=[('Eligible for Interview'+' '+'-'+' '+i['name'])for i in l if i['cgpa']>=7.2]
#     return res




# students = [
#   {"name": "Maaz", "cgpa": 8.5, "has_backlog": False},     {"name": "Rohit", "cgpa": 6.2, "has_backlog": True},
#    {"name": "Amit", "cgpa": 7.8, "has_backlog": False},
#      {"name": "Suresh", "cgpa": 5.9, "has_backlog": False},
#     {"name": "Vikram", "cgpa": 9.1, "has_backlog": True}
# ]

# result=filter_eligible_stutedt(students)
# print(result)