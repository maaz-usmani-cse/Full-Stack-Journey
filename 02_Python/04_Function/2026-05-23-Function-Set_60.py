'''
Ek list ke har number ke andar jao aur har akshar (digit) ko check karo 
(index 1 se lekar aakhir se ek pehle tak):Agar koi digit apne left aur right
dono padosiyon se chhoti hai (Valley), toh use 'V' se replace kar do.Agar
koi digit apne left aur right dono padosiyon se badi hai (Peak), toh use
    
'P' se replace kar do.Shuruat aur aakhiri digit ko normal chhor dena.
Test Input: l = [152, 9384]Hint: * 152 $\rightarrow$ 5 left (1) aur 
right (2) dono se bada hai, toh ban gaya 'P'. Output: "1P2".9384 $\rightarro
w$ 3 dono se chhota hai (9 aur 8 se) $\rightarrow$ 'V'. 8 dono se bada hai 
(3 aur 4 se) $\rightarrow$ 'P'.
Output: "9V P4".Expected Output: ["1P2", "9VP4"]

'''
# def replace_element(l):
#     for i in range(len(l)):
#         digit=str(l[i])
#         res=digit[0]
#         for j in range(1,len(digit)-1):
#             current=int(digit[j])
#             right=int(digit[j+1])
#             left=int(digit[j-1])
#             if current>right and current>left:
#                 res=res+'P'
#             elif current<right and current<left:
#                  res=res+'V'
#             else:
#                  res=res+digit[j]
#         res=res+digit[-1]
#         l[i]=res
#     return l

# user=eval(input("enter your list"))
# result=replace_element(user)
# print(result)                    
        







'next greater replace'
# def next_greater_replace(l):
#     next_greater=[-1]*len(l)
#     for i in range(len(l)):
#        for j in range(1,len(l)):
#            index=(i+j)%len(l)
#            if l[index]>l[i]:
#                next_greater[i]=l[index]
#                break
#     return next_greater

# user=eval(input("enter your list"))
# result=next_greater_replace(user)
# print(result)


           
            

        
   
'''
Database se employees ka data aaya hai. Tumhe ek list comprehension chala kar sirf un
employees ke Naam (name)
nikaalne hain jo "IT" department mein hain.

'''

# def find_it_dept(d):
#     res = [d[i]['name'] for i in d if 'dept' in d[i] and d[i]['dept'].upper() == 'IT']
#     return res

# employees = {
#     1: {"name": "Maaz", "dept": "IT"},
#     2: {"name": "Amjad", "dept": "HR"},
#     3: {"name": "Rohit", "dept": "IT"}
# }
# result=find_it_dept(employees)
# print(result)






'''

Jab users website par form bharte hain, toh koi naam ke aage-piche galti se bahut saare spaces
chhor deta hai, koi khali chhor deta hai, toh koi galti se galat data daal deta hai. backend par 
data save karne se pehle humein use saaf karna hota hai.

Sawaal: Ek products ke naamon ki list hai. Kuch naamon ke aage-piche bematlab ke spaces hain
("  Laptop  "), kuch ekdam khali hain (""), aur kuch mein sirf 'N/A' likha hai.
Tumhe ek list comprehension chalani hai jo:

Saare valid naamon ke aage-piche ke spaces khatam kare (.strip() ka use karke).

Khali strings "" aur "N/A" ko list se ekdam bahar (filter) nikal phenke!

Test Input: products = ["  iPhone 15 ", "", "MacBook Air  ", "N/A", "  iPad Pro "]

Expected Output: ['iPhone 15', 'MacBook Air', 'iPad Pro']

'''

# def clean_data(l):
#    res=[i.strip()for i in l if i!='' and i!='N/A']
#    return res


# user=eval(input("enter your list"))
# result=clean_data(user)
# print(result)









'''
Tumhe database se active users ka data mila hai. Tumhe list comprehension ka
use karke ek nayi list banani hai, jisme har user ka sirf (id, name)
ka ek Tuple hona chahiye. Par dhyan rahe,
sirf unhi users ko uthana jinka status "active" hai!
'''
# def filter_DATA(l):
#     res=[(i['id'], i['name'])for i in l if 'id'and'name'and 'status' in i if i['status']=='active']
#     return res


# user=eval(input("enter your list"))
# result=filter_DATA(user)
# print(result)


