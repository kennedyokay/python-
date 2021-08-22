#1
# def abs():
#     n = int(input("請輸入整數："))
#     if n >=0:
#         print(n)
#     elif n <=0:
#         n = n*-1
#         print(n)
# abs()

#2
# def mymax(n1, n2):
#     l = [n1, n2]
#     print(max(l))
# mymax(500, 20)

#3 
# def isPalindrome(n):
#     l = list(str(n))
#     l.reverse()
#     print("".join(str(e) for e in l))
# isPalindrome(12345)

#4
# def add(n1, n2):
#     ans = n1 + n2
#     return ans
# def sub(n1, n2):
#     ans = n1 - n2
#     return ans
# def mul(n1, n2):
#     ans = n1 * n2
#     return ans
# def div(n1, n2):
#     ans = n1 / n2
#     return ans
# print(add(5, 10), sub(5, 10), mul(5, 10), div(5, 10))

# 5
#def #add(n1, n2):
#    ans = n1 + n2
#    return ans
#def sub(n1, n2):
#    ans = n1 - n2
#    return ans
#def mul(n1, n2):
#    ans = n1 * n2
#    return ans
#def div(n1, n2):
#    ans = n1 / n2
#    return ans
#while True:
#  n1 = float(input("請輸入數字1："))
#  n2 = float(input("請輸入數字2："))
#  print(add(n1, n2), sub(n1, n2), mul(n1, n2), div(n1, n2))
#  con = input("是否繼續?(y/n)")
#  if con == "n":
    
#6
#def guest_info(firstname, middlename, lastname, gender):
#  """整合客戶資料"""
#  if gender == "M":
#    welcom = fitstname + " " + middlename + " " + lastname + "先生歡迎您"
#  elif gender == "F":
#    welcom = firstname + " " + middlename + " " + lastname + "小姐歡迎您"
#  return welcom
#name = input("enter a name")
#name = name.split()
#print(name)
#print(guest_info("馨", "文", "張", "F"))
#print(guest_info("Ivan", "Carl", "Hung", "F"))

#7
#def CtoF(c):
#  degree_F = (9 * c) / 5 +32
#  return degree_F
#def FtoC(f):
#  degree_C = 5 * (f-32) / 9
#  return degree_C
#print(CtoF(-40), FtoC(-40))

#8
# import sys
# print("預設遞迴極限:{}",format((sys.getrecursionlimit())))
# sys.setrecursionlimit(100000)
# print("新的遞迴極限:{}",format((sys.getrecursionlimit())))

# def calculate_Pi(i):
#   Pi =(((-1) ** (i + 1)) / (2 * i - 1))
#   if i == 1:
#     return 1
#   else :
#     return (Pi + calculate_Pi(i-1))
# for n in range(1, 9002, 1000):
#       print("第%d次計算，Pi=%2.5f"%(n, 4 * calculate_Pi(n)))

#9
# def isTriangle(s1, s2, s3):
#   s_total = (s1 + s2 +s3)
#   s_max = max(s1, s2, s3)
#   # print(s_max)
#   if s_total - s_max >s_max:
#     print("It's triangle")
#     print(area(s1, s2, s3))
#   else:
#     print("It isn't triangle")

# def area(s1, s2, s3):
#   s_total = (s1 + s2 +s3) / 2 
#   area = ((s_total * (s_total - s1) * (s_total - s2) * (s_total - s3)) ** (1/2))
#   return area
# isTriangle(3, 4, 5) gefg

#10 
# """
# Palindrome(回文)應用，輸入數字並判別他是否為回文數
# """
# def isPalindrome(n):
#     l = list(str(n))
#     l.reverse()
#     # print("".join(str(e) for e in l))
#     reverse_l = "".join(str(e) for e in l)
#     if int(reverse_l) == n:
#         print("It's Palindrome")
#     else:
#         print("It isn't Palindrome")

# isPalindrome(int(input("Enter a nubmber:")))

#11
# """
# 不指定數量函式
# """
# def make_pizza(size, *toppings):
#     #列出製作冰淇淋的配料
#     print("%s吋 pizza的配料如下：" %(size))
#     for topping in toppings:
#         print("---", topping)

# make_pizza("18", "夏威夷", "海鮮", "豬肉", "牛肉", "羊肉")

#12
# """
# 文字回文
# """
# l = []
# def isPalindrome(n):
#     l = list(n)
#     l.reverse()
#     # print("".join(str(e) for e in l))
#     reverse_l = "".join(str(e) for e in l)
#     if reverse_l == n:
#         print("It's Palindrome")
#     else:
#         print("It isn't Palindrome")

# isPalindrome(input("Enter alphabets:"))

#13
# def fib(bs):
#     """
#     費波納茲係數，費氏數列。
#     """
#     l = []
#     Fn = 0
#     for b in range(0, bs+1):
#         if b == 0:
#             l.append(b)
#         elif b == 1:
#             l.append(b)
#         elif b >= 2:
#             Fn = (l[b - 1]) + (l[b -2])
#             l.append(Fn)
#     print(l)
#     print("The Fibonacci namber of index({}) are: {}".format(bs, ", ".join(str(e) for e in l)))

# fib(10)

#14
# def oddfn(x):
#     """
#     偶數篩選器
#     """
#     return x if (x % 2 == 0) else None 
# mylist = [5, 10, 15, 20, 25, 30]
# filter_object = filter(oddfn, mylist)
# print("偶數串列嗎：", [item for item in filter_object])

#15
# """
# 使用匿名函數，進行偶數篩選器
# lamdba: 匿名函數
# """
# mylist = [5, 10, 15, 20, 25, 30]
# oddlist = list(filter(lambda x: (x % 2 == 0), mylist))

# print("偶數串列嗎：", oddlist)

#16
# point = [25, 18, 12, 22, 31, 17, 26, 19, 18, 10]
# batter_20 = list(filter(lambda x:(x >= 20), point))
# print(batter_20)

#17
# def upper(func):
#     def newFunc(args):
#         oldresult = func(args)
#         newresult = oldresult.upper()
#         return newresult
#     return newFunc
# def bold(func):
#     def wrapper(args):
#         return " bold " + func(args) + " bold "
#     return wrapper 
# def italic(func):
#     def wrapper(args):
#         return " italic " + func(args) + " italic "
#     return wrapper

# @italic
# @bold
# @upper
# def greeting (string):
#     return string 

# print(greeting("Hello! iPhone"))

#18 
# mystr = "12345"
# anslist = list(map(lambda x: x, mystr))
# print(anslist)