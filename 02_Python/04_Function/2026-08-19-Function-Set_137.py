'''
Diye gaye list se sirf even numbers filter karke unka square return karo.
'''

# def filter_even_number(l):
#     return [i**2 for i in l if i%2==0]

# user=eval(input('enter your list'))
# result=filter_even_number(user)
# print(result)



'''
Task: Agar number even hai toh 'Even', odd hai toh 'Odd' return karo. 
(Interview tip: if-else list comprehension ke shuru mein aata hai, jabki simple if filter end mein)
'''

# def filter_data(l):
#     return ['even' if i%2==0 else 'odd' for i in l]

# user=eval(input("enter your list"))
# result=filter_data(user)
# print(result)



'''
2D Matrix ko Flatten Karna (Flattening Nested List)
Task: Nested 2D list ko single 1D list mein convert karo.
'''

# def flatten_2d_list(l):
#     return [j for i in l for j in i]

# user=eval(input('enter your list'))
# resuult=flatten_2d_list(user)
# print(resuult)




'''
List of Dictionaries se Conditional Data Extract KarnaTask: Un users ke naam extract karo jinki age 18 ya usse zyadh ho
'''

def filter_age(d):
    return [ i['name'] for i in d if i['age']>=18]

user=eval(input("enter your list"))
result=filter_age(user)
print(result)