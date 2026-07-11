'''
find dublicate element in first jo pehla bar repeta ho rha usse
 '''
# def find_repeat_number(l):
#     d={}
#     for i in l:
#         if i in d:
#             return f'repeated number is {i}'
#         else:
#             d[i]=True
        

# user=eval(input("enter your list"))
# result=find_repeat_number(user)
# print(result)



'count vowels and consonant'
# def count_vowels_consonant(s):
#     vowels=0
#     consonant=0
#     for i in s:
#         if i.isalpha():
#             if i in ['a','e','i','o','u']:
#                 vowels=vowels+1
#             else:
#                 consonant=consonant+1
#     return f'vowels:{vowels} consonat:{consonant}'


# user=input("enter your word")
# result=count_vowels_consonant(user)
# print(result)




'Do dictionaries ko merge karna hai. Agar dono dictionaries mein koi key common '
'(ek jaisi) hai, toh unki values aapas mein add (plus) ho jani chahiye.'

# def merge_dictionaries(dict1, dict2):
#     # 1. Ek khali dictionary banayi
#     result = {}
    
#     # 2. Pehli dictionary ka data daala
#     for key in dict1:
#         result[key] = dict1[key]
        
#     # 3. Dusri dictionary ka data check karke daala
#     for key in dict2:
#         if key in result:
#             result[key] = result[key] + dict2[key]
#         else:
#             result[key] = dict2[key]
            
#     # 4. Final dictionary ko return kar diya
#     return result

# # --- Function ko chala kar check karte hain ---

# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'b': 5, 'c': 15, 'd': 50}

# # Function ko call kiya aur result ko print kiya
# final_output = merge_dictionaries(d1, d2)
# print(final_output)

