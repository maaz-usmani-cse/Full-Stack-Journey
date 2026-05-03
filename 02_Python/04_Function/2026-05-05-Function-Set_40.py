'''
l = [{'id': 101, 'name': 'maaz'}, {'id': 102, 'name': 'amit'}].
Loop chalao aur jiski id 101 hai, us poori dictionary ko list se remove kar do.
'''
# def remove_id(l):
#     remove=[]
#     for i in l:
#         if 'id' in i and i['id']==101:
#             pass
#         else:
#             remove.append(i)
#     return remove

# user=eval(input("enter your list"))
# result=remove_id(user)
# print(result)







'''
l = [{'info': {'name': 'maaz', 'age': 20}}, {'info': {'name': 'amjad', 'age': 22}}].
Ek loop chala kar sirf names (maaz, amjad) print karo. (Dhyan do, dictionary ke andar dictionary hai).

'''

# def print_name(l):
#     for i in l:
#         if 'info' in i and 'name' in i['info'] :
#             print(i['info']['name'],end=' ')


# user=eval(input("enter your list"))
# print_name(user)







'''
l = [{'lang': 'python'}, {'lang': 'java'}, {'lang': 'python'}, {'lang': 'js'}].
Ek nayi dictionary banao jo bataye kaunsi language kitni baar aayi hai.

Expected Output: {'python': 2, 'java': 1, 'js': 1}
'''
# def frequency_count(l):
#     d={}
#     for i in l:
#         for key in i:
#             val=i[key]
#             if val in d:
#                 d[val]=d[val]+1
#             else:
#                 d[val]=1
#     return d

# user=eval(input("enter your list"))
# result=frequency_count(user)
# print(resuflt)








'''
l = [{'city': 'bhopal', 'user': 'maaz'}, {'city': 'patna', 'user': 'rahul'}, {'city': 'bhopal', 'user': 'ali'}].
Ek loop chalao aur 'bhopal' walo ko ek alag list mein daalo aur 'patna' walo ko alag.
'''

# def separate_city(l):
#     bhopal=[]
#     patna=[]
#     for i in l:
#         if 'city' in i:
#             if i['city']=='bhopal':
#                 bhopal.append(i)
#             elif i['city']=='patna':
#                 patna.append(i)
#     return bhopal,patna
  

# user=eval(input("enter your list"))
# result=separate_city(user)
# print(result)








'''
l = [{'score': 45}, {'score': 12}, {'score': 88}, {'score': 5}].
Loop chala kar sabse chota (Minimum) score find karo bina min() function ke.

'''
# def find_minimum_score(l):
#     minimum_score=None
#     for i in l:
#         if 'score' in i:
#             score=i['score']
#             if minimum_score is None or score<minimum_score:
#                 minimum_score=score
#     return minimum_score

# user=eval(input("enetr your list"))
# result=find_minimum_score(user)
# print(result)




      
'''
l = [{'a': 1}, {'b': 2}, {'c': 3}].
In teeno dictionaries ko merge karke ek single dictionary banao.

Expected Output: {'a': 1, 'b': 2, 'c': 3}
'''


# def merge_dict(l):
#     d={}
#     for i in l:
#         for key in i:
#             d[key]=i[key]
#     return d

# user=eval(input("enter your dict"))
# result=merge_dict(user)
# print(result)




'''
l = [{'price': 100}, {'price': 200}, {'price': 300}, {'price': 400}].
Loop chala kar sari prices ka Average nikaalo.
'''

def calculate_average(l):
    count=0
    total=0
    for i in l:
        if 'price' in i:
            total=total+i['price']
            count=count+1
    if count>0:
        average=total/count
        return average
    else:
        return 0
    


user=eval(input("enter your list"))
result=calculate_average(user)
print(result)

