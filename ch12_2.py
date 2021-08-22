"""
封裝 (encapsulation)：
可以從程式直接引用類別內的屬性與方法，這樣的屬性與方法，稱為公有(publice)屬性與公有方法。
這些可以從外部連接是可以直接修改類別內的屬性值的，因此，會造成資料的不安全性。
python 在精神上提供了一個私有屬性與方法的觀念，可以使得在類別外無法直接更改類別內的私有屬性，類別外也無法直接呼叫的私有方法，
這些稱為封裝。
可以參見ch12_3 (in ch12_1.py) 的註解。

但是，實際上，python 是沒有私有屬性與方法的，可以使用其他的方法來取得。

"""
# Ch12_8  私有屬性
# class Banks():
#     """私有屬性與私有方法，在定義屬性的時候，在屬性前面加__，
#     這樣，在外部就無法進行更改了。
#     """
#     def __init__(self, uname):
#         self.__name = uname 
#         self.__balance = 0
#         self.__bankname = "Taipei Bank" 
#     def save_money(self, money):
#         self.__balance += money 
#         print("存款", money, "完成")
#     def withdraw_money(self, money):
#         self.__balance -= money 
#         print("提款", money, "完成")

#     def get_balance(self):
#         print(self.__name.title(), "目前餘額：", self.__balance)

# hungbank = Banks("hung")
# hungbank.save_money(300)
# hungbank.get_balance()
# hungbank.balanece = 10000
# hungbank.get_balance()
# hungbank.__balanece = 10000
# hungbank.get_balance()
# """破解私有屬性"""
# #物件名稱._類別名稱私有屬性
# hungbank._Banks__balance = 15000
# hungbank.get_balance()

#私有方法
# class Banks():
#     """定義銀行類別"""
#     def __init__(self, uname):                                       #初始化方法
#         self.__name = uname                                          #設定私有存款者名字
#         self.__balance = 0                                           #設定私有開戶金額是0
#         self.__bankname = "Taipei Bank"                              #設定私有銀行名稱
#         self.__rate = 30                                             #預設美金與台幣換匯比率
#         self.__service_charge = 0.01                                 #換匯的服務費

#     def save_money(self, money):                                     
#         self.__balance += money
#         print("存款", money, "完成")
#     def withdraw_money(self, money):
#         self.__balance -= money
#         print("提款", money, "完成")
#     def get_balance(self):
#         print(self.__name.title(), "目前餘額：", self.__balance)

#     def usa_to_taiwan(self, usa_d):
#         self.result = self.__cal_rate(usa_d)
#         return self.result 
    
#     def __cal_rate(self, usa_d):                                         #計算換匯，私有方法，在前面加__
#         return int(usa_d * self.__rate * (1 - self.__service_charge))

# hungbank = Banks("hung")
# usdallor = 50
# print(usdallor, "美金可以兌換", hungbank.usa_to_taiwan(usdallor), "台幣")

# """破解私有方法"""
# #hungbank.__cal_rate(50) #直接呼叫會錯誤
# print(hungbank._Banks__cal_rate(100)) #類似於破解私有屬性，這樣就可以直接呼叫。

#Ch12_9_2
# class Score():
#     def __init__(self, score):
#         self.__score = score
#     def getscore(self):
#         print("inside the getscore")
#         return self.__score 
#     def setscore(self, score):
#         print("inside the setscore")
#         self.__score = score 
#         return self.__score 
# stu = Score(0)
# print(stu.getscore())
# stu.setscore(80)
# print(stu.getscore())

#python 新式屬性 = property(getter[,setter[,fdel[,doc]]])
"""
getter是獲取屬性值函數，setter是設定屬性值函數，fdel是刪除屬性值函數，doc是屬性描述，傳回的是新式函數，未來可以由此新式屬性存取私有屬性內容。
"""

# # Ch12_9_3
# class Score():
#     def __init__(self, score):
#         self.__score = score
#     def getscore(self):
#         print("inside the getscore")
#         return self.__score 
#     def setscore(self, score):
#         print("inside the setscore")
#         self.__score = score
#     sc = property(getscore, setscore)           #python風格 #設定sc為私有屬性，因此可以用.sc來使用私有屬性 #property(getter[,setter[,fdel[,doc]]])

# stu = Score(0)
# print(stu.sc)
# stu.setscore(80)
# print(stu.sc)     

#Ch12_9_4     #property(getter[,setter[,fdel[,doc]]])
# class Score():
#     def __init__(self, score):
#         self.__score = score
#     @property    #取代這行 sc = property(getscore, setscore) 
#     def sc(self):
#         print("inside the getscore")
#         return self.__score
#     @sc.setter 
#     def sc(self, score):
#         print("inside the setscore")
#         self.__score = score
#     # sc = property(getscore, setscore)  # 被@property() 取代 原始見ch12_9_3

# stu = Score(0)
# print(stu.sc)
# stu.sc = 80
# print(stu.sc)  

#Ch12_9_5 計算正方形面積
# class Square():
#     def __init__(self, sideLen):
#         self.__sideLen = sideLen
#     @property
#     def area(self):
#         return self.__sideLen ** 2

# obj = Square(10)
# print(obj.area)

"""
方法與屬性的類型：
可以分為"實例方法"以及"類別方法"。
實例方法：特色是有self，屬性開頭是self，同時所有的方法的第一個參數都是self，建立類別物件時，屬於物件的一部分。
類別方法：類別方法前面是 #classmethod (以裝飾器存在)，不同的是，第一個參數習慣是使用cls，不需要實例化，可以由類別本身直接調用，另外，類別屬性會隨時被更新。
"""
#ch12_9_6 類別方法
# class Counter():  
#     counter = 0 #類別屬性，可由類別本身調用
#     def __init__(self): 
#         Counter.counter += 1 #更新指標
#     @classmethod 
#     def show_counter(cls):  #類別方法，可由類別本身調用
#         print("class method")
#         print("counter = ", cls.counter) #也可以使用Counter.counter調用
#         print("counter = ", Counter.counter)

# one = Counter() #更新第一次
# two = Counter() #更新第二次
# three = Counter() #更新第三次
# Counter.show_counter() #調用show_counter()

#ch12_9_7 靜態方法
"""靜態方法是由staticmethod開頭，不需原先的self或是cls參數，這只是碰巧存在類別的函數，與類別方法和實例方法沒有綁定關係，這個方法也是由類別名稱直接調用。"""
# class Pizza():
#     @staticmethod
#     def demo():
#         print("I like Pizza")
# Pizza.demo()