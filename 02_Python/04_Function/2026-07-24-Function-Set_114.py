'''
Reverse elements between first and last prime number 

'''


# def is_prime(n):
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     if n%2==0:
#         return False

#     for i in range(3,int(n**0.5)+1, 2):
#         if n%i==0:
#             return False
#     return True



# def reverse_element_between_first_and_last_prime(l):
#    prime_index=[]
#    for i in range(len(l)):
#        if is_prime(l[i]):
#            prime_index.append(i)

#    if len(prime_index)>2:
#            fist=prime_index[0]
#            last=prime_index[-1]
#            sub=l[fist:last+1]
#            l[fist:last+1]=sub[::-1]
#    return l


# user=eval(input("enter your list"))
# result=reverse_element_between_first_and_last_prime(user)
# print(result)           

        








          





'''
Replace each element with nearest greater element on right 

'''

# def replace_nearest_greater(l):
#     res=[-1]*len(l)
#     stack=[]

#     for i in range(len(l)-1,-1,-1):
#         while stack and stack[-1]<=l[i]:
#             stack.pop()

#         if stack:
#             res[i]=stack[-1]

#         stack.append(l[i])
#     return res


# user=eval(input("enter your list"))
# result=replace_nearest_greater(user)
# print(result)







'''
Extract First & Last Character as Key-Value Pairs

Task: Words ki list se dictionary banani hai jahan Key = 
Word ka pehla akshar, aur Value = Word ka aakhri akshar.

Input: words = ["python", "django", "bhopal"]

Expected Output: {'p': 'n', 'd': 'o', 'b': 'l'}

'''

# def extract_first_last_character_key_value(l):
#     res={}
#     for i in l:
#         res[i[0]]=i[-1]
#     return res


# user=eval(input("enter your list"))
# result=extract_first_last_character_key_value(user)
# print(result)
        
        






'''
List me Positive Number Check Karoge?
Ek list numbers di gayi hai. Check karo ki kya isme kam se kam ek positive number hai.

Input: [-5, -2, 0, -8, 3]

Output: True

'''

# def is_possitive(l):
#     res=any(i<0 for i in l)
#     return res


# user=eval(input('enter your list'))
# result=is_possitive(user)
# print(result)





'''
Kya koi String Non-Empty Hai?
Strings ki list me check karo ki kya koi bhi string non-empty (falsy nahi) hai.

Input: ["", "", "Python", ""]

Output: True

'''

# def is_empty_string(l):
#     res=any(i=='' for i in l)
#     return res


# user=eval(input("enter your list"))
# result=is_empty_string(user)
# print(result)





'''
Even Numbers Dhundna
List me check karo ki kya koi even number maujood hai.

Input: [1, 3, 5, 7, 9]

Output: False

'''
# def check_even(l):
#     res=any(i%2==0 for i in l)
#     return res


# user=eval(input('enter your list'))
# result=check_even(user)
# print(result)



