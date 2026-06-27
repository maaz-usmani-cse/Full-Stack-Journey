'''
Anagram Checker
Question: Do strings check karo ki wo anagrams hain ya nahi (words jinke letters same ho, 
jaise "listen" aur "silent"). Dictionary ka use karna hai.

Logic: Dono strings ka character count dictionary banayein aur dono dicts ko compare karein.

'''

# def anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return 'its not angram'
#     d1={}
#     d2={}
#     for i in s1:
#         if i in d1:
#             d1[i]=d1[i]+1
#         else:
#             d1[i]=1
#     for i in s2:
#         if i in d2:
#             d2[i]=d2[i]+1
#         else:
#             d2[i]=1
#     if d1==d2:
#         return 'anagram'
#     else:
#         return 'not angram'
    

# s1=input("enter  your word")
# s2=input("enter your word")
# result=anagram(s1,s2)
# print(result)




'''
Agar dictionary ke andar ek aur dictionary ho (nested), 
toh use single level dictionary mein convert karo 
(e.g., {'a': {'b': 1}} $\rightarrow$ {'a_b': 1}).
'''

# def single_level_dictionary(d,parent_key=''):
#     for i in d:
#         res={}
#         v=d[i]
#         if parent_key:
#             new_key=parent_key+'_'+i
#         else:
#             new_key=i
#         if type(v)==dict:
#             recursion=single_level_dictionary(v,new_key)
#             for j in recursion:
#                 res[j]=recursion[j]
#         else:
#             res[new_key]=v

#     return res


# user=eval(input("enter your list"))
# result=single_level_dictionary(user)
# print(result)





'Merge two sorted lists '
def merge_sorted_list_simple(l1, l2):
    res = []
    i = 0  
    j = 0  
    
   
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1 
        else:
            res.append(l2[j])
            j += 1  
            
   
    while i < len(l1):
        res.append(l1[i])
        i += 1
        
    
    while j < len(l2):
        res.append(l2[j])
        j += 1
        
    return res



l1=eval(input("enter your list"))
l2=eval(input("enter your list"))
result=merge_sorted_list_simple(l1,l2)
print(result)
