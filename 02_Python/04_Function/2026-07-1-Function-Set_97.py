'''
Aapko ek names ki list di gayi hai: names = ['amit', 'rohit', 'maaz', 'aniket', 'vikas']

Task: List comprehension ka use karke ek nayi list banani hai jismein sirf wahi naam hon 
jo 'a' letter se start hote hain, aur unka naam UPPERCASE (bade aksharon) mein hona chahiye.

Expected Output: ['AMIT', 'ANIKET']


'''
# def filter_name(l):
#     res=[i.upper() for i in l if i[0]=='a'.lower() ]
#     return res

# user=eval(input("enter your list"))
# result=filter_name(user)
# print(result)




'''
Aapko ek numbers ki list di gayi hai jismein kuch numbers repeat ho rahe hain: nums 
= [1, 2, 2, 3, 4, 4, 5]

Task: List comprehension ka use karke saare numbers ka square (varg) nikalna hai,
 lekin output mein koi bhi square repeat nahi hona chahiye (Unique hona chahiye).

(Hint: Jo abhi humne side mein dictionary ya set wala dimaag lagaya tha, wahi yahan lagao).

Expected Output: [1, 4, 9, 16, 25]

'''

# def non_repeated_square(l):
#     d={}
#     res=[i**2 for i in l if i**2 not in d and not d.update({i**2:True})]
#     return res

# user=eval(input("enter tour list"))
# result=non_repeated_square(user)
# print(result)



'''
Matrix ke Column Elements nikalnaAbhi humne diagonal nikalna seekha tha. Ab aapke paas wahi $3 \times 3$ matrix hai:Pythonmatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Task: range() aur list comprehension ka use karke is matrix ka 
pehla khada column (Vertical Column) nikalna hai (yaani 1, 4, 7).
(Hint: Abhi thodi der pehle jo humne [i][0] ka dry-run kiya tha, 
use yaad karo!)Expected Output: [1, 4, 7]

'''

# def matrix_column_element(l):
#     res=[[i][0] for i in range(len(l))]
#     return res

# user=eval(input("enter your list"))
# result=matrix_column_element(user)
# print(result)




'''
Strings ki list se sirf Odd Numbers nikalna
Aapko strings ke roop mein kuch digits diye gaye hain: str_nums 
= ['12', '15', '22', '33', '40', '45']

Task: List comprehension ka use karke pehle in strings ko integer mein badalna hai, 
aur fir sirf unhe filter karna hai jo Odd (visham sankhya) hain.

Expected Output: [15, 33, 45]

'''

# def find_odd_number(l):
#     res=[int(i) for i in l if int(i)%2!=0]
#     return res

# user=eval(input("enter your list"))
# result=find_odd_number(user)
# print(result)



'''
Aapko ek list di gayi hai: arr = [3, 5, 15, 9, 20, 30, 25]

Task: Ek list comprehension likhni hai jo sirf un numbers ko filter kare jo 3 se divide hote hain ya
 5 
se divide hote hain, lekin 15 se divide NAHI hote hon (yaani dono se ek saath divide na hote hon).

Expected Output: [3, 5, 9, 20, 25] (Kyunki 15 aur 30 dono se divide ho jate hain, toh wo hat gaye).

Bhai, ho jao shuru! Is baar matrix ka column wala (Question 18) pehle try karoge ya koi aur? 
Code likho aur bhejo, sath mein dekhte hain!

'''

# def divisible_by_3_or_5(l):
#     res=[i for i in l if (i%3==0 or i%5==0) and i%15!=0]
#     return res

# user=eval(input("enter your list"))
# result=divisible_by_3_or_5(user)
# print(result)





'''
Aapko ek dictionary di jayegi jahan keys rolls hain aur values students ke naam hain. 
Aapko sirf un entries ko swap (ulta) karna hai (yaani value ko key aur key ko value banana hai)
 jinke roll numbers Even hain.

Python
def swap_even_rolls(d):
    # Dictionary comprehension ka khel
    pass

# Test Case
data = {101: "Amit", 102: "Rohit", 103: "Vikas", 104: "Maaz"}
print(swap_even_rolls(data))
# Expected Output: {'Rohit': 102, 'Maaz': 104}  (Kyunki 101 aur 103 odd hain, toh wo h
'''

# def swap_even_rolls(d):
#     res={}
#     for i in d:
#         name=d[i]
#         if i % 2==0:
#             res[name]=i
#     return res

# user=eval(input("enter your list"))
# result=swap_even_rolls(user)
# print(result)