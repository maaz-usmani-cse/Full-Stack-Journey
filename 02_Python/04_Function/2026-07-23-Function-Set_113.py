'''
Arrange array so local minimums come at even indexes --done

Is question ka simple matlab yeh hai ki aapko array ko is tarah re-arrange
 karna hai ki har even index ($0, 2, 4, 6 ots$) par baitha element 
apne aaju-baaju (left aur right) ke elements se chhota (ya barabar) ho.

nums = [9, 6, 8, 3, 7, 2]
# Output: [6, 9, 3, 8, 2, 7]
'''


# def rearrange_local_minima(l):
#     for i in range(0,len(l),2):
#         if i>0 and l[i]>l[i-1]:
#             temp=l[i]
#             l[i]=l[i-1]
#             l[i-1]=temp
#         if i<len(l)-1 and l[i]>l[i+1]:
#             temp=l[i]
#             l[i]=l[i+1]
#             l[i+1]=temp
#     return l

# user=eval(input("enter your list"))
# result=rearrange_local_minima(user)
# print(result)







'''
Rotate only the longest increasing subarray --done
'''

# def rotate_longest_increasing_array(l):
#     if not l:
#         return l

#     current = 1
#     longest = 1
#     start = 0
#     end = 1  
#     current_start = 0

#     for i in range(len(l) - 1):
#         if l[i + 1] > l[i]:
#             current = current + 1
#         else:
#             if current > longest:
#                 longest = current
#                 start = current_start
#                 end = i + 1  

#             current = 1
#             current_start = i + 1

    
#     if current > longest:
#         longest = current
#         start = current_start
#         end = len(l)  # Slicing ke liye direct len(l)

#     # Subarray rotation
#     sub = l[start:end]
#     if len(sub) > 1:
#         roated_subarray = sub[1:] + sub[:1]
#         l[start:end] = roated_subarray  # Fix 2: Overwrite only if rotated

#     return l


# user = eval(input("enter your list: "))
# result = rotate_longest_increasing_array(user)
# print(result)





'''

Selective Key Prefixing based on Value ConditionTask: Agar value $100$
 se badi hai toh key ke aage "pref_" add kar do, warna key waisi hi rehne do.Input: inventory = 
{"apple": 50, "mango": 150}Expected Output: {"apple": 50, "pref_mango": 150}
'''


# def add_pref_value_greater100(d):
#     res={}
#     for i in d:
#         value=d[i]
#         if value>100:
#           res['pref_'+i]=value
#         else:
#            res[i]=value
#     return res


# user=eval(input("enter your list"))
# result=add_pref_value_greater100(user)
# print(result)






'''
Create Dictionary of Character ASCII Divisibility

Task: String ke har unique character ko key banana hai aur value mein True agar uski ASCII value (ord()) even hai, warna False.

Input: s = "code"

Expected Output: {'c': False, 'o': False, 'd': True, 'e': True}  (ASCII: c=99, o=111, d=100, e=101)

'''

# def create_ord_based_dic_of_char(s):
#     d={}
#     for i in s:
#         if ord(i)%2==0:
#             d[i]=True
#         else:
#             d[i]=False

#     return d


# user=input('enter your word')
# result=create_ord_based_dic_of_char(user)
# print(result)








'''
Remove Keys with Vowel Starts

Task: Dictionary mein se un keys ko hatana hai jo kisi vowel (a, e, i, o, u) se start hoti hon.

Input: d = {"apple": 1, "banana": 2, "orange": 3, "mango": 4}

'''

def remove_keys_start_with_vowel(d):
    vowel={'a','e','i','o','u' ,'A','E','I','O','U'}
    for i in list(d):
        if i[0] in vowel:
            del d[i]
    return d

user=eval(input("enter your list"))
result=remove_keys_start_with_vowel(user)
print(result)