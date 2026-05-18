'.Find longest increasing streak with difference = 2 '
# nums = [1, 3, 5, 10, 12, 14, 16, 20]
# def find_longest_streak(l):  
#     longest_streak = 1
#     current_streak = 1
#     for i in range(1, len(nums)):
#         if nums[i] - nums[i-1] == 2:
#             current_streak += 1
#         else:
#             if current_streak > longest_streak:
#                 longest_streak = current_streak 
                
#             current_streak = 1 
#     if current_streak > longest_streak:
#         longest_streak = current_streak
#     return longest_streak


# user=eval(input("enyer your list"))
# result=find_longest_streak(user)
# print(result)











'Find longest decreasing streak '
# def longest_decreasing(l):
#     longest_decrease=1
#     current_streak=1
#     for i in range(1,len(l)):
#         if l[i]<l[i-1]:
#             current_streak=current_streak+1
#         else:
#             if current_streak>longest_decrease:
#                 longest_decrease=current_streak
#             current_streak=1
#     if current_streak>longest_decrease:
#         longest_decrease=current_streak
#     return longest_decrease


# user=eval(input("enter your list"))
# result=longest_decreasing(user)
# print(result)














'Replace each element with count of prime digits '
# def replace_with_count_of_prime(l):
#     for i in range(len(l)):
#         change_str=str(l[i])
#         count=0
#         for j in change_str:
#             if int(j)<2:
#                 continue
#             for k in range(2,int(int(j)**2)+1):
#                 if i%k==0:
#                     break
#             else:
#              count=count+1
#         l[i]=count

# user=eval(input("enter your list"))
# result=replace_with_count_of_prime(user)
# print(result)
    

