'''
Aapko ek list di hai jisme alag-alag data types mix hain (strings, numbers, aur None).
Aapko list comprehension ka use karke ek line mein sirf integers (int) ya
float numbers ka square ($i \times i$) nikaalna hai, aur baaki saare data types
(jaise strings ya None) ko chupchaap safe tarike se filter karke baahar nikaal 
dena hai taaki code crash na ho.Real Example: 
l = [2, "Maaz", 3.0, None, 4]Output: [4, 9.0, 16]

'''
# def square_int_float(l):
#     res=[i**2 for i in l if type(i)==int or type(i)==float]
#     return res


# user=eval(input("enter your list"))
# result=square_int_float(user)
# print(result)





'''
Humne pichle baar double-split (.split('@')[1].split('.')[0]) se domain nikala tha.
Par agar us list mein galti se koi None ya koi Integer (jaise 123) aa gaya, toh 
.split() crash ho jayega! Aapko ek line mein saare emails mese unka domain nikaalna
hai, par sirf tabhi jab wo element ek asli string ho aur usme @ ka sign maujood ho!
Real Example: emails = ["maaz@gmail.com", None, "bhopal@yahoo.com", 404, "invalid-email"]

'''

# def domain_find(l):
#     for i in l:
#        res = [i.split('@')[1].split('.')[0] for i in l if isinstance(i, str) and '@' in i and '.' in i]
#        return res

# user=eval(input("enter your list"))
# result=domain_find(user)
# print(result)





'''
Ek e-commerce inventory ki list mein prices mix format mein hain.
Kuch prices string mein hain (jaise "500"), kuch pehle se integer hain 
(jaise 1200), aur kuch fields khali (None) hain. Aapko ek line mein saare valid prices ko
integer format (int) mein badalna hai, aur None ko filter out kar dena hai.
Real Example: prices = ["400", 1500, None, "2000"]

Output: [400, 1500, 2000]
'''



# def only_string_data(l):
#     res=[int(i) if isinstance(i,str) else i for i in l if i is not None]
#     return res


# user=eval(input("enter your list"))
# result=only_string_data(user)
# print(result)







'''
l: Aapko ek form input data ki list di hai. Aapko un saari strings ko UPPERCASE 
(.upper()) mein badalna hai jo ki asli strings hon aur khali na hon. Agar list mein koi 
number ya None hai, toh use bina chhede filter out kar dena hai.
Real Example: data = ["django", "   ", None, "bhopal", 2026]

Output: ["DJANGO", "BHOPAL"]

'''

# def filter_out_data(l):
#     res=[i for i in l if isinstance(i,str) and i.strip()]
#     return res


# user=eval(input("enter your list"))
# result=filter_out_data(user)
# print(result)





