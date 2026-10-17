print("Hello World.")

# def armstrong(n):
#     original = n
#     final = 0
#     l = len(str(n))
#     for i in range(l):       
#         a = n%10
#         final = (final*10) + a
#         n = n//10
#         # print(final)   this line used when you want to undertand the flow
#     return final == original

# print(armstrong(2332))

# class palindrome:
#     def fun(n):
#         final = 0
#         original = n
#         l = len(str(n))
#         for i in range(l):
#             a = original%10
#             final = (final*10) + a
#             original = original//10
#             print(final)
#         return final == n

# s = palindrome()
# print(palindrome.fun(1234))

# class palindrome:
#     def fun(n):
#         original = n
#         # original[::-1]        This is not a good practice 
#         # return original == n
#         final = original[::-1]
#         return final == n

# # s = palindrome() use this when you use @staticmethod in class other wise it give type error 
# print(palindrome.fun('nitin'))

# class solution:
#     def fun(n):
#         final = []
#         num = n
#         for i in range(1,(num//2)+1):
#             if num%i==0:
#                 final.append(i)
#         final.append(num)
#         return final

# print(solution.fun(20))
# import math
# class divisible:
#     def fun(n):
#         num = n
#         a = int(math.sqrt(num))
#         final = []
#         for i in range(1,a+1):
#             if num%i == 0:
#                 final.append(i)
#                 if i != num//i:
#                     final.append(num//i)
#         # return final.sort() give none if you wnat to use this method do like this final.sort() next line return final
#         return sorted(final)
# print(divisible.fun(25))

# class dicfrequency:
#     def fun(n):
#         num = n
#         dic = {}
#         for i in num:
#             dic[i] = dic.get(i,0)+1
#         return dic
# in_put = input("Enter value in spaces : ")
# final_input = [int(i) for i in in_put.split()]
# print(dicfrequency.fun(final_input))

# class solution:
#     def fun(n,m):
#         index = [0]*11
#         for i in n:
#             index[i] +=1
#             final = []
#         for i in m:
#             if i in n:
#                 final.append(index[i])
#             else:
#                 final.append(0)
#         return final
# in_put1 = list(map(int, input("Enter you numbers with spaces :").split()))
# in_put2 = list(map(int, input("Enter you numbers : ").split()))

# print(solution.fun(in_put1,in_put2))

# class solution:
#     def fun(n,m):
#         dic = {}
#         final = []
#         for i in n:
#             dic[i] = dic.get(i,0)+1
#         for i in m :
#             if i in n:
#                 final.append(dic[i])
#             else:
#                 final.append(0)
#         return final

# in_put1 = list(map(int, input("Enter you numbers with spaces :").split()))
# in_put2 = list(map(int, input("Enter you numbers : ").split()))

# print(solution.fun(in_put1,in_put2))      

# class solution:
#     def fun(n=[2,33,44,-65,8,99,6,121,22]):
#         num = n
#         largest = float("-inf")
#         for i in range(len(num)):
#             if num[i] > largest:
#                 largest = num[i]
#         return largest
# print(solution.fun())

# class solution:
#     def fun(n=[2,70,44,-65,8,99,6,121,22]):
#         num = n
#         largest = float("-inf")
#         second_largest = float("-inf")
#         for i in range(len(num)):
#             if num[i] > largest:
#                 second_largest = largest
#                 largest = num[i]
#             elif num[i] != largest and num[i] > second_largest:
#                 second_largest = num[i]
#         return f"Largest : {largest}\nSecond Largest : {second_largest}"

# print(solution.fun())

# class solution:
#     def fun(n=[-5,-2,4,5,6,7]):
#         num = n
#         count = 0
#         for i in range(len(num)-1):
#             if num[i] <= num[i+1]:
#                 count +=1
#             else:
#                 break
#         return count == len(num)-1

# print(solution.fun())