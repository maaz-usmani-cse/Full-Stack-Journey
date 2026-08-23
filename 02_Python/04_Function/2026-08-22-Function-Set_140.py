'''
Replace Multiple Vowels: Ek function banayein jo di gayi string ke saare
vowels (a, e, i, o, u) ko "#" se replace kare (Loop ya chaining use karein).
'''
# def mapped_vowels_string(s):
#     res=''
#     d={"A",'E','I','O','U','a','e','i','o','u'}
#     for i in s:
#         if i in d:
         
#             res=res+'#'

#         else:
#             res=res+i
#     return res

# user=input("enter your word")
# result=mapped_vowels_string(user)
# print(result)    





'''
String "cat and dog" mein jahan 'a' hai wahan 'o' aur jahan 'o' hai wahan 'a' swap karein
 (Hint: Ek temporary placeholder use karein).
'''
# def replace_a_with_o_and_o_with_a(s):
#     s=s.replace('a', '#')
#     s=s.replace('o','a')
#     s=s.replace('#', 'o')
#     return s


# user=input('enter your word')
# result=replace_a_with_o_and_o_with_a(user)
# print(result)





'find maximum and minimum element in array'

# def find_maximum_and_minimum(l):
#     min_val=None
#     max_val=None
#     for i in l:
#         if min_val is None or i<min_val:
#             min_val=i

#         if max_val is None or i>max_val:
#             max_val=i
#     return f'min_value{min_val} - maz_val{max_val}'

# user=eval(input('enteer your list'))
# result=find_maximum_and_minimum(user)
# print(result)





'एक स्ट्रिंग लें (जैसे "Python is very easy to learn") और split() का उपयोग करके पता करें कि उस वाक्य में कुल कितने शब्द हैं।'
# def word_count(s):
#     count_word=0
#     s=s.split()
#     for i in s:
#         count_word+=1
#     return count_word

# user=input('enter your word')
# result=word_count(user)
# print(result)







'find second largest'
# def second_largest(l):
#     first=None
#     second=None
#     for i in l:
#         if first is None or i>first:
#             second=first
#             first=i

#         elif i!=first and (second is None or i>second):
#             second=i
#     return f'second largest is {second}'

# user=eval(input('enter your list'))
# result=second_largest(user)
# print(result)