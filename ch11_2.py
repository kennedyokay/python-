"""
#ch11_19 信件應用
def product_msg(customers):
  str1 = "親愛的"
  str2 = "本公司將在2020年12月20日舉辦產品發表會"
  str3 = "總經理 深石敬上"
  for customer in customers:
    msg = str1 + customer + "\n" + str2 + "\n" + str3
    print(msg, "\n")
  
members = ["Damon", "Peter", "Mary"]
product_msg(members)
"""
"""
#ch11_19_1.py 
def mydata(n):
  print("函數 id(n) = : ", id(n), "\t", n)
  n = 5 
  print("函數 id(n) = : ", id(n), "\t", n)

x = 1 
print("主程式 id(x) = : ", id(x), "\t", x)
mydata(x)
print("主程式 id(x) = : ", id(x), "\t", x)
"""
"""
#ch11_22_1.py
def insertChar(letter, myList=[], inList=[1,2]):
  myList.append(letter)
  inList.append(letter)
  print(myList)
  print(inList)
insertChar("x")
insertChar("y") #上一個加入的元素會存在，若要不在，參考下列程式
"""
"""
#ch11_22_2.py
def insertChar(letter, myList=None):
  if myList == None:
    myList = []
  myList.append(letter)
  print(myList)
  
insertChar("x")
insertChar("y")
"""
"""
#ch11_23 原本函數值只能一對一，可以利用*來送入0到多個函數值，以tuple形式傳送
def make_icecream(*toppings): #*任意數量
  #列印配料
  print("配料如下")
  for topping in toppings:
    print("-----", topping)
make_icecream("草莓醬")
make_icecream("草莓醬", "葡萄乾", "巧克力")
"""
"""
#ch11_24 **任意數量的關鍵字參數
def build_dict(name, age, **players):
  info = {}
  info["Name"] = name
  info["age"] = age
  for key, value in players.items():
    info[key] = value
  return info 
  
player_dict = build_dict("James", "32", City = "cleveland", State = "Ohio")
print(player_dict)