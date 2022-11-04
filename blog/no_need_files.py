



#
# def is_palindrome(string):
#     flag = 1
#     str1 =''
#     str2 = ''
#     # for i in string:
#     #     str1 +=i
#     #
#     # # for j in range(len(string)-1, -1, -1):
#     for j in string[::-1]:
#         # str2 += string[j]
#         str2 += j
#     if string == str2:
#         return 'Palindrome'
#     else:
#         return 'Not Palindrome'
#
#
# result = is_palindrome('abba')
# print(result)
#


# # flag = 1
#
#
# def nearly_equal(a, b):
#     flag = 1
#     for i in a:
#         if i in b:
#             flag = 1
#         else:
#             flag = 0
#             break
#     return flag
#
#
# # is_nearly_equal = nearly_equal('perl', 'pearl')
# is_nearly_equal = nearly_equal('python', 'perl')
# # is_nearly_equal = nearly_equal('', '')
#
# if is_nearly_equal == 1:
#     print(True)
# else:
#     print(False)



# def dp(l1, l2):
#     def p(ll1, ll2, n):
#         return ll1[n] * ll2[n]
#
#     r = 0
#     for i in range(len(l1)):
#         r += p(l1, l2, i)
#     return r
#
#
# print(dp([1, 2, 3], [4, 5, 6]))

# ll1 = [1, 2, 3]
# print(len(ll1))
#
# def outer_func():
#     def inner_func():
#         print("Hello, World!")
#     inner_func()
# outer_func()
