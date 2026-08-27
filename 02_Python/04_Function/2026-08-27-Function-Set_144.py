'''
Find All Peaks (Elements Greater Than Both Neighbors)

Task: List mein un sabhi numbers ko dhundho jo apne pichle aur agle dono padosi elements se strictly bade hain.

Input: nums = [1, 3, 2, 5, 4, 7, 1]

Expected Output: [3, 5, 7]

'''

# def find_peak_element(l):
#     res=[]
#     for i in range(1,len(l)-1):
#         if l[i]>l[i+1] and l[i]>l[i-1]:
#             res.append(l[i])
#     return res

# user=eval(input("enter your list"))
# result=find_peak_element(user)
# print(result)





'''
Remove Consecutive Duplicates OnlyConsecutive duplicate characters ko 
hata kar single character bana do.Input: s = "aaabbcddd" Output: "abcd"
'''
# def remove_consecutive_dublicate(s):
#     res=''
#     for i in range(1,len(s)):
#         if s[i]!=s[i-1]:
#             res=res+s[i-1]
#     res=res+s[-1]

#     return res


# user=input('enter your character')
# result=remove_consecutive_dublicate(user)
# print(result)



'''
Check Pair Sum (Two Consecutive)Check karo ki kya list mein koi bhi do lagataar (adjacent)
 numbers ka sum target ke barabar hai.
Input: nums = [1, 3, 5, 2, 7], target = 8 Output: True (kyunki 3 + 5 = 8)
'''
# def check_pair_consecutive(l,k):
#     for i in range(len(l)-1):
#         if l[i]+l[i+1]==k:
#             return True

#     return False

# user=eval(input("enter your list"))
# k=int(input("enter your k"))
# result=check_pair_consecutive(user,k)
# print(result)




'''
Run-Length Decoding (Reverse Compression)Compressed string ko wapas original
string mein badlo.Input: s = "a3b2c1" Output: "aaabbc"
'''
# def decode_string(s):
#     res=''
#     for i in range(1,len(s),2):
#         digit=int(s[i])
#         char=s[i-1]
#         res=res+digit*char
#     return res

# user=input("enter your word")
# result=decode_string(user)
# print(result)




