'''

Mujhe sirf un students ki list chahiye jinka status ekdam "active" hai, AUR unka "token" 
badal kar "REFRESHED_2026" ho jana chahiye.
Baaki name aur status waisa ka waisa copy hona chahiye!

students = [
    {"name": "Maaz", "status": "active", "token": "OLD_11"},
    {"name": "Rohit", "status": "inactive", "token": "OLD_22"},
    {"name": "Amit", "status": "active", "token": "OLD_33"}
]
'''


# def filter_list(l):
#     active_status=[]
#     for i in l:
#         if 'status' in i and i['status']=='active':
#             active_status.append({**i,'token':'REFRESHED_2026'})
#     return active_status


# user=eval(input("enter your list"))
# result=filter_list(user)
# print(result)




'''
phone_numbers = ["9876543210", "12345", "8877665544", "9900"]
Sawaal: Agar phone number ki length ekdam 10 character hai, toh uske beech ke 
4 digits ko security ke liye "X" se badal do (mask kar do), yaani pehle 3 dikhein,
beech ke 4 badal jayein, aur aakhiri ke 3 dikhein. Agar number 10 digit ka nahi hai,
toh use "Invalid" likh kar list mein daalo!

Expected Output: ['987XXXX210', 'Invalid', '887XXXX544', 'Invalid']

'''

# def mask_phone_number(l):
#     expected_outp=[]
#     for i in l:
#         if len(i)==10:
#             mask=i[:3]+'X'*4+i[7:]
#             expected_outp.append(mask)
#         else:
#             expected_outp.append('invalid')
#     return expected_outp


# user=eval(input("enter your list"))
# result=mask_phone_number(user)
# print(result)





'''

api_response = [
    {"user": "Maaz", "courses": ["Python", "Django"]},
    {"user": "Rohit", "courses": ["HTML", "CSS", "JS"]},
    {"user": "Amit", "courses": ["Python"]}
]
Sawaal: Mujhe ek single normal list nikaal kar do jisme saare unique courses ke naam hon, bina kisi duplicate ke!

Expected Output: ['Python', 'Django', 'HTML', 'CSS', 'JS']
'''


# def flatten_uniques_courses(l):
#     uniques_course=[]
#     for i in l:
#         if 'courses' in i:
#             for j in i['courses']:
#                 if j not in uniques_course:
#                     uniques_course.append(j)
#     return uniques_course


# user=eval(input("entr our list"))
# result=flatten_uniques_courses(user)
# print(result)









'''
Tumhe ek numbers ki list di gayi hai. Tumhe is list ke saare "Leaders" nikaal kar ek nayi list mein daalne hain.
'''
# def leader_elemnt(l):
#     leader=[]
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#            if l[j]>l[i]:
#                break
#         else:
#             leader.append(l[i])
#     return leader

# user=eval(input("enter your list"))
# result=leader_elemnt(user)
# print(result)





'''
Tumhe ek list di gayi hai jisme har number do-do baar (duplicate) aaya hai, 
lekin sirf ek number aisa hai jo akela (unique) hai,
 uska koi jodi daar nahi hai. Mujhe us akele number ko dhoond kar nikaal ke do!

'''

# def find_single_element(l):
#     res=False
#     for i in l:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         if count==1:
#             res=i
#             break
#     return res


# user=eval(input("enter your list"))
# result=find_single_element(user)
# print(result)







'''
Ek sorted list ko Wave (leher) ki tarah arrange karo! Yaani pehla element bada hona chahiye,
doosra chhota, teesra bada, chautha chhota... (arr[0] >= arr[1] <= arr[2] >= arr[3]...)
[10, 20, 30, 40, 50, 60]
expected output=[20, 10, 40, 30, 60, 50]

'''
# def arrange_wave(l):
#     for i in range(0,len(l)-1,2):
#         temp=l[i]
#         l[i]=l[i+1]
#         l[i+1]=temp
#     return l


# user=eval(input("enter your list"))
# result=arrange_wave(user)
# print(result)




'''
Tumhe ek list di gayi hai aur ek target number diya gaya hai. Mujhe list mein se un do numbers ka pair (jodi) nikaal kar do jinko aapas mein plus (+) karne par target mil jaye!

Python
arr = [2, 7, 11, 15]
target = 9

'''


# def target_pair_find(l,target):
#     d={}
#     for i in l:
#         required=target-i
#         if required in d:
#             return[i,required]
#         d[i]=True
#     return []



# li=eval(input("enter your list"))
# target=int(input("enter your number"))
# result=target_pair_find(li,target)
# print(result)





'''
one of the fastest way to sort list 

'''

def quick_sort_simple(arr):
    # 1. Base Case: Agar list khali hai ya 1 element hai, toh ruk jao
    if len(arr) <= 1:
        # Yeh line recursion ko full stop lagati hai
        return arr
        
    # 2. Pivot Chunna: Ekdam beech ka element pakad lo
    pivot = arr[len(arr) // 2]
    
    # 3. Teen khaali boriyaan banayein maal alag karne ke liye
    left = []
    middle = []
    right = []
    
    # 4. 🔥 PURE FOR LOOP: Ek-ek karke element ko bina list comprehension ke alag karo
    for x in arr:
        if x < pivot:
            left.append(x)     # Pivot se chhote numbers
        elif x == pivot:
            middle.append(x)   # Pivot ke barabar numbers
        else:
            right.append(x)    # Pivot se bade numbers
            
    # 5. 🚀 Recursion Ka Magic: Chhote aur bade tukdon ko fir se sort karo aur jodo
    return quick_sort_simple(left) + middle + quick_sort_simple(right)


# ---- TESTING ----
user = eval(input("Enter your list (e.g., [10, 7, 8, 9, 1, 5]): "))
result = quick_sort_simple(user)
print("Sabse Fast Sorted List:", result)