print("Hello World!")

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


