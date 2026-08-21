'''
Decode Number-First Encoded String

Task: Encoded string jahan pehle count hai aur baad mein character, use original string mein expand karo.

Input: s = "3a2b1c2a"

Expected Output: "aaabbcaa"

'''
# def decode_number_with_string(s):
#     res=''
#     for i in range(0,len(s),2):
#         count=int(s[i])
#         char=s[i+1]
#         res+=count*char
#     return res

# user=input("enter your word")
# result=decode_number_with_string(user)
# print(result)




'''
String ke har consecutive pair ke characters ko aapas mein swap karo. Agar length odd ho toh aakhri character waise hi rahega.

Input: s = "abcdefg"

Expected Output: "badcfeg"
'''
# def swap_consecutive_pair_exclude_odd_length(s):
#     res=''
#     for i in range(0,len(s),2):
#         if i+1<len(s):
#             res+=s[i+1]+s[i]
#         else:
#             res+=s[i]
#     return res


# user=input("entwer your word")
# result=swap_consecutive_pair_exclude_odd_length(user)
# print(result)




'''
Consecutive numbers agar +1 ke difference par chal rahe hain toh 
unka start aur end index note karke length nikalo.
Input: nums = [1, 2, 3, 7, 8, 12]Expected Output: [[1, 2, 3], [7, 8], [12]]

'''
# def consecutive_number(l):
#     start_index=0
#     res=[]
#     for i in range(len(l)-1):
#        if l[i+1]!=l[i]+1:
#           res.append(l[start_index:i+1])
#           start_index=i+1
#     res.append(l[start_index:])
#     return res
    
    

         
# user=eval(input("enter your list"))
# result=consecutive_number(user)
# print(result)






'ek function jo multiple list handle karey'

# def unliited_argement(*args):
#     total=0
#     for single_list in args:
#         for i in single_list:
#             total+=i
#     return total

# user=eval(input("enter your list"))
# if isinstance(user,tuple):
#     result=unliited_argement(*user)

# else:
#     result=unliited_argement(user)
# print(result)


