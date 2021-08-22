# def 函數名稱(參數值1[,參數值2....]):
#  """函數註解(docstring)"""
#  程式碼區塊
#  return [回傳值1, 回傳值2, ....]

"""
# ch11_3
def greeting(name):
  #python函數需回傳名字name
  print("Hi", name, "Good Morning")
#greeting() #有回傳值必須輸入值
greeting("Nelson")
"""""
"""
# ch11_5
def subtract(x1, x2):
  result = x1 - x2
  print(result)
print("相減程式")
a = int(input("a = "))
b = int(input("b = "))
print("a - b =", end=" ") #接下來輸出不跳行
subtract(a, b)
"""

#遞迴
# # def a(i):
#   if i ==1:
#     return 1
#   else:
#     return i * a(i-1)
# print(a(5))
# x = 9001
# pi = 0
# for i in range(1, x+1):
#   pi += 4 * ((-1) ** (i+1) / (2 * i -1))
#   if i != 1 and i%  1000 == 0:
#     print("當I = %7d時，PI = %20.19F" %(i, pi))


"""
#ch11_7
def interest(interest_type, subject):
  #顯示興趣和主題
  print("我的興趣是" + interest_type)
  print("在" + interest_type+ "中，最喜歡的是" + subject)
  print()
  
interest(interest_type = "旅遊", subject = "敦煌")
interest(subject = "敦煌", interest_type = "旅遊")
"""
"""
#ch11_10
val = None #可以將None 視為 False 但False不是None
if val:
  print("I love Jave")
else:
  print("I love python")
#以上程式可以簡化為：
val = None
print("I love jave" if val else "I love python")
"""
"""
#ch11_10_3
def is_None(string, x):
  if x is None:
    print("%s = None" % string)
  elif x:
    print("%s = True" % string)
  else:
    print("%s = False" % string)
is_None("空串列", [])
is_None("空元組", ())
is_None("空字典", {})
is_None("空集合", set())
is_None("None", None)
is_None("True", True)
is_None("False", False)
"""
"""
#ch11_13
def mutifunction(x1, x2):
  #四則運算
  addresult = x1 + x2
  subresult = x1 - x2
  mulresult = x1 * x2
  divresult = x1 / x2
  return addresult, subresult, mulresult, divresult

x1 = x2 = 10
add, sub, mul, div = mutifunction(x1, x2)
print("加法結果", add)
print("減法結果", sub)
print("乘法結果", mul)
print("除法結果", div)
"""
"""
#ch11_14 #包裝成元祖
def mutifunction(x1, x2):
  #四則運算
  addresult = x1 + x2
  subresult = x1 - x2
  mulresult = x1 * x2
  divresult = x1 / x2
  return addresult, subresult, mulresult, divresult

x1 = x2 = 10
ans = mutifunction(x1, x2)
print("加法結果", ans[0])
print("減法結果", ans[1])
print("乘法結果", ans[2])
print("除法結果", ans[3])
"""
"""
#ch11_18
def build_vip(id, name, tel = ""):
  #to build the vip information
  vip_dict = {"VIP_ID":id, "Name":name}
  if tel:
    vip_dict["Tel"] = tel
    return vip_dict
  return vip_dict
    
while True:
  print("建立ＶＩＰ資訊系統")
  idnum = input("請輸入ID：")
  name = input("請輸入姓名：")
  tel = input("請輸入電話號碼，不輸入按Enter：")
  member = build_vip(idnum, name, tel)
  print(member, "\n")
  repeat = input("是否繼續(y/n)?")
  if repeat !="y":
    break
print("歡迎下次使用")
"""
