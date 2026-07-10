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
def count_vowels_consonant(s):
    vowels=0
    consonant=0
    for i in s:
        if i.isalpha():
            if i in ['a','e','i','o','u']:
                vowels=vowels+1
            else:
                consonant=consonant+1
    return f'vowels:{vowels} consonat:{consonant}'


user=input("enter your word")
result=count_vowels_consonant(user)
print(result)