'''
Ek string di gayi hai: "programming".
Ek dictionary banaiye jo bataye ki kaunsa character kitni baar aaya hai.

(Expected output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1})

'''

# def character_frequency(d):
#     res={}
#     for i in d:
#         if i in res:
#             res[i]=res[i]+1
#         else:
#             res[i]=1
#     return res

# user=eval(input("enter your dict"))
# result=character_frequency(user)
# print(result)


'''
Ek string di gayi hai: "programming".
Ek dictionary banaiye jo bataye ki kaunsa character kitni baar aaya hai.

(Expected output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1})

'''

# def swap_using_comprehenshions(d):
#     return {value:key for key, value in d.items()}


# user=eval(input("enter your dict"))
# result=swap_using_comprehenshions(user)
# print(result)



'''
Aapke paas words ki ek list di gayi hai:

Python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Ek function likhiye jo anagrams ko ek saath group karke dictionary values ki list banaye.

Expected Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
'''


# def quick_sort_pivot(s):
#     if len(s) <= 1:
#         return s
#     pivot = s[0]
#     left = ''
#     middle = ''
#     right = ''
#     for i in s:
#         if i < pivot:
#             left += i
#         elif i == pivot:
#             middle += i
#         else:
#             right += i
#     return quick_sort_pivot(left) + middle + quick_sort_pivot(right)

# def anagram_group(words):
   
#     groups = {}
    
#     for word in words:
        
#         sorted_key = quick_sort_pivot(word)
        
#         if sorted_key not in groups:
#             groups[sorted_key] = []
        
        
#         groups[sorted_key].append(word)
  
#     return list(groups.values())

# # Test Run:
# words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = anagram_group(words_list)
# print(result)
