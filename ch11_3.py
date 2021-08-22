"""
#ch11_26 遞迴式函數設計
#特色：每次呼叫自己時，都會使範圍越來越小；必須要有一個終止條件來結束遞迴函數
def factorial(n):
  #計算n的階乘，n必須為整數
  if n == 1:
    return 1
  else:
    return (n * factorial(n-1)) #5*後，開啟一個4的factorial程式，得出4*....直到輸出1，5*4*3*2*factorial(1)
value = 3
print(value, "的階乘結果是 ＝", factorial(value))
value = 5
print(value, "的階乘結果是 ＝", factorial(value))
"""
"""
#ch11_30_2 global 應用
def printmsg():
  global msg
  msg = "Java"
  print("函數列印：更改後：, msg")
  
msg = "Python"
print("主程式列印：更改前", msg)
printmsg()
print("主程式列印：更改後", msg)
"""
"""
#ch11_31  匿名函數的應用 lambda
def square(x):
  value = x ** 2
  return value
print(square(10))

square = lambda x: x **2
print(square(10))
"""
"""
#ch11_34 匿名函數使用與filter
def oddfn(x):
  return x if (x % 2 == 1) else None 
mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(oddfn, mylist)
print("奇數串列嗎：", [item for item in filter_object])
"""
# #Ch11_37
# mylist = [5, 10, 15, 20, 25, 30]

# squarelist = list(map(lambda x: x ** 2, mylist))        # map(func, iterable)，可以將string, list, tuple, 的item放進去function進行計算。

# print("串列平方值：", squarelist) 




"""
#ch11_39_1 設計自己的range()
def myRanger(start = 0, stop = 100, step = 1):
  n = start
  while  n < stop:
    yield n 
    n += step
print(type(myRanger))
for x in myRanger(0, 5):
  print(x)
#設計之函數資料型態為function，與range類似，但回傳值不是使用return 而是yield，同時整個函數內部不是立即執行，第一次for回圈執行到yield時會回傳n，下一次會繼續執行n+=6ㄝ然後回到起點執行到yield，直到沒有直回傳。
"""
"""
#ch11_39_2 裝飾器(Decorator)
#可以將函數程式傳入另一個函數程式
def upper(func): #裝飾器                     #func = greeting()
  def newFunc(args):
    oldresult = func(args)                  #greeting(args)    => return args
    newresult = oldresult.upper()           # (args).upper()
    print("函數名稱：", func.__name__)
    print("函數參數：", args)
    return newresult
  return newFunc
@upper #設定裝飾器
def greeting(string): #問號函數
  return string 
# mygreeting = upper(greeting) #手動裝飾器
# print(mygreeting("Hello! iPhone"))       #輸入 "Hello! iPhone" => string
print(greeting("Hello! iPhone"))
"""

# #ch11_39_4 除法除錯器
# """裝飾器應用"""
# def errcheck(func):
#   def newFunc(*args):
#     if args[1] != 0: #除數不等於0時
#       result = func(*args)
#     else:
#       result = "除數不可爲0"
#     print("函數名稱：", func.__name__)
#     print("函數參數：", args)
#     print("執行結果：", result)
#     return result
#   return newFunc
# @errcheck
# def mydiv(x, y):
#   return x/y
# print(mydiv(6, 3))
# print(mydiv(6, 0))