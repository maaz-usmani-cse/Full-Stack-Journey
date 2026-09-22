'''
List me mixed items hain ["10", "hello", 25, None, "99.5", "100"]. 
Sirf integers filter karo jo successfully convert ho sakein.
'''
# def filter_only_integer(val):
#     try:
#         int(val)
#         return True

#     except(ValueError,TypeError):
#         return False

# user=eval(input("enter your list"))
# result=list(filter(filter_only_integer,user))
# print(result)
    

'''
Target word "listen" ke anagrams filter karo words ki list me se bina direct external library ke.
words = ["silent", "enlist", "banana", "google", "inlets"]

'''

# def is_anagram(s1):
#     target='listen'
#     d1={}
#     d2={}

#     if len(s1)!=len(target):
#         return False
    
#     for i in s1:
#         if i in d1:
#             d1[i]=d1[i]+1

#         else:
#             d1[i]=1

#     for j in target:
#         if j in d2:
#             d2[j]=d2[j]+1

#         else:
#             d2[j]=1

#     return d1==d2

# user=eval(input("enter your list"))
# result=list(filter(is_anagram,user))
# print(result)

        

'List me se Armstrong numbers filter karo nums = [153, 370, 120, 9474, 89]'

# def is_ram_strong_num(n):
#     temp=n
#     total=0
#     power=len(str(n))

#     while n>0:
#         digit=n%10

#         total=total+(digit**power)
#         n=n//10

#     return total==temp


# user=eval(input("enter your list"))
# result=list(filter(is_ram_strong_num,user))
# print(result)




'''
. Consecutive Duplicate Characters
Problem: Wo words filter karo jinme koi letter lagatar do baar aaye (jaise "book", "apple").
words = ["tree", "cat", "door", "python", "balloon"]
'''


# def consecutive_dublicate_filter(word):
#     for i in range(len(word)-1):
#         if word[i]==word[i+1]:
#             return True

#     return False


# user=eval(input("enter your list"))
# result=list(filter(consecutive_dublicate_filter,user))
# print(result)




'''
Password tabhi valid hai jab: length  8, at least 1 uppercase, 1 lowercase, 1 digit aur 1 special character ho.
passwords = ["Admin@123", "weakpass", "HELLO1234", "P@ss1"]
'''

# def is_password_valid(password):
#     if len(password)<8:
#         return False

#     upper_case=any(i.isupper() for i in password)
#     lowercase=any(i.islower() for i in password)
#     digit=any(i.isdigit() for i in password)
#     special_char=any(not i.isalnum() for i in password)


#     return upper_case and lowercase and digit and special_char

# user=eval(input('enter your list'))
# result=list(filter(is_password_valid,user))
# print(result)



'''
Wahi matrix rows filter karo jinka arithmetic average 50 se bada ho
matrix = [[10, 20, 30], [80, 90, 100], [], [50, 60]]
'''

# def is_high_avg_row(row):
#     if not row:
#         return False

#     total=0
#     for i in row:
#         total+=i

#     return True if total/len(row)>50 else False

# user=eval(input("enter your list"))
# result=list(filter(is_high_avg_row,user))
# print(result)



