'''
Merge Two Dictionaries with Value Summation
Question: Do dictionaries d1 aur d2 ko merge karna hai. Agar key dono mein ho, 
toh values ka sum aana chahiye, warna original value.

Input: d1 = {"apple": 10, "banana": 20}, d2 = {"banana": 15, "orange": 5}

Expected Output: {"apple": 10, "banana": 35, "orange": 5}

Interview Point: Merging logic, handling missing keys gracefully.

'''


# def merge_dict_key_same_value_add(d1,d2):
#     res={}
#     for i in d1:
#         res[i]=d1[i]

#     for i in d2:
#         if i in res:
#             res[i]=res[i]+d2[i]
#         else:
#             res[i]=d2[i]
#     return res


# d1=eval(input("entr your list"))
# d=eval(input("enter you diact"))
# result=merge_dict_key_same_value_add(d1,d)
# print(result)









'''
Find Top K Most Frequent Elements
Question: Numbers ki list se Top 2 sabse zyada repeat hone wale elements unke count ke saath return karo.

Input: nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4], k = 2

Expected Output: {4: 4, 1: 3} (4 aaya 4 baar, 1 aaya 3 baar)

Interview Point: Hashmap frequency counting + Sortin


'''
# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l
#     pivot=l[0]
#     value=pivot[1]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#          if i[1]>value:
#              left.append(i)
#          elif i[1]==value:
#               middle.append(i)
#          else:
#              right.append(i)
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)
        
                

# def top_2_repeat_element(l,k=2):
#     res={}
#     top={}
#     for i in l:
#         if i in res:
#             res[i]=res[i]+1
#         else:
#             res[i]=1
#     l=[]
#     for i in res:
#         l.append((i,res[i]))
#     sorting=quick_sort_pivot(l)

#     for i in range(k):
#         key=sorting[i][0]
#         value=sorting[i][1]
#         top[key]=value
#     return top


# user=eval(input("enter your list"))
# result=top_2_repeat_element(user)
# print(result)
   
        
    




'''
Find First Non-Repeating Character in String
Question: String mein sabse pehla aisa character dhoondho jo repeat na hua ho. Output mein character aur uska index return karo as a dict.

Input: "swiss"

Expected Output: {"char": "w", "index": 1}

Interview Point: Two-pass hashmap algorithm (1st pass for frequency, 2nd pass for first index).

'''


# def find_first_rst_non_repeating(s):
#     res={}
#     for i in s:
#         if i in res:
#             res[i]=res[i]+1
#         else:
#             res[i]=1


#     for i in range(len(s)):
#         char=s[i]
#         if res[char]==1:
#             return {'char':char , 'index':i}
        


# user=input('enter your word')
# result=find_first_rst_non_repeating(user)
# print(result)








