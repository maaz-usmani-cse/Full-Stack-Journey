'''

: Words ki list se un words ko ek saath group karke dictionary banani hai jo aapas mein anagrams hain (yaani same letters se bane hain).

Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]

Expected Output: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

Interview Point: Sorting + Dictionary mapping key concept.


'''

# def quick_sort_pivot(l):
#     if len(l)<=1:
#         return l

#     pivot=l[0]
#     left=[]
#     middle=[]
#     right=[]
#     for i in l:
#         if i<pivot:
#             left.append(i)

#         elif i==pivot:
#             middle.append(i)

#         else:
#             right.append(i)

#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)




# def sorting_string(s):
#     l=list(s)
#     sorting=quick_sort_pivot(l)
#     res=''
#     for i in sorting:
#         res=res+i

#     return res



# def grouping_anagram(l):
#     res={}
#     for i in l:
#         key=sorting_string(i)

#         if key not in res:
#             res[key]=[]
#         res[key].append(i)

#     return res



# user=eval(input("enter your list"))
# result=grouping_anagram(user)
# print(result)


 


    



'''

Question: Ek JSON/Dict response se saare None, empty string "", aur whitespaces "   " wale key-value pairs remove karne ke liye function likho.

Input: {"name": "Maaz", "age": None, "bio": "   ", "city": "Bhopal", "phone": ""}

Expected Output: {"name": "Maaz", "city": "Bhopal"}

Interview Point: API response sanitization, string .strip(), and not None checks


'''


# def clean_data(d):
#     res={}
#     for i in d:
#         if d[i] is not None:
#           if isinstance(d[i],str):
#              if d[i].strip():
#                 res[i]=d[i]
#           else:
#              res[i]=d[i]
#     return res


# user=eval(input("enter your list"))
# result=clean_data(user)
# print(result)








'''

Ek paragraph se har word ka count nikalna hai. Condition: Case-insensitive hona chahiye aur special characters (., ,, !) count nahi hone chahiye.

Input: "Hello world! Hello Maaz, welcome to Python world."

Expected Output: {'hello': 2, 'world': 2, 'maaz': 1, 'welcome': 1, 'to': 1, 'python': 1}

Interview Point: String cleaning + Frequency dict logic.

'''

# def count_word_in_paragraph(s):
#     l=s.split()
#     d={}
#     for word in l:
#         word=word.lower()
#         clean_word=''
#         for j in word:
#             if j.isalnum():
#                 clean_word=clean_word+j
#         if clean_word:
#             if clean_word in d:
#                 d[clean_word]=d[clean_word]+1
#             else:
#                 d[clean_word]=1
#     return d


# user=input('enter your word')
# result=count_word_in_paragraph(user)
# print(result)

        

        





'''
tring mein sabse pehla aisa character dhoondho jo repeat na hua ho. Output mein character aur uska index return karo as a dict.

Input: "swiss"

Expected Output: {"char": "w", "index": 1}

Interview Point: Two-pass hashmap algorithm (1st pass for frequency, 2nd pass for first index).

'''


# def first_non_repeating_element_index(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     for i in range(len(s)):
#         if d[s[i]]==1:
#             return {'char':s[i] , 'index':i}

#     return None


# user=input("enter your word")
# result=first_non_repeating_element_index(user)
# print(result)




'left_shift k time'
# def left_shift(l,k):
#     k=k%len(l)
#     return l[k:]+l[:k]



# user=eval(input("enter your list"))
# result=left_shift(user)
# print(result)



