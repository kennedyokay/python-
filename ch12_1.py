# The cheapter 12
"""
class Banks():  #定義類別(class)，第一個字母建議使用大寫，使用方法與函數類似。
可以用類別來進行自創資料類型。

操作方法：
要先定義物件(object)變數，簡稱物件。
object.類別的屬性
object.類別的方法()
"""
#Ch12_2
# class Banks():
#     """定義銀行類別"""
#     bankname = "Taipei Bank" #定義屬性
#     def motto(self):         #定義方法，在類別中的def 要稱為"方法"，不能稱為函數，呼叫時只有這個類別中的物件可以使用此方法。
#         return "以客為尊" 

# userbank = Banks() #定義物件
# print("目前服務銀行是：", userbank.bankname)
# print("目前服務理念是：", userbank.motto())


#Ch12_3
# class Banks():
#     bankname = "Taipet Bank"
#     def __init__(self, uname, money): #self是Banks這個類別自己
#         # print(self)
#         # print(uname)                #會抓給進來的參數 = "hung"
#         # print(money)                #會抓給進來的參數 =  100
#         self.name = uname             #Banks這個類別的name屬性被定義為 uname = hung
#         self.balance = money 

#     def get_balance(self):
#         return self.balance #只有一個變數

# hungbank = Banks("hung", 100) #定義Banks時，會自動啟動__init__ (initialization)，而後面的self是必須的。
# print(hungbank.name.title(), "存款餘額是：", hungbank.get_balance()) #title()使第一個字母轉換為大寫
# print(hungbank.name.title(), "存款餘額是：", hungbank.balance) #也可以不用另外寫方法，直接從定義屬性中讓他拉出來。
#可以直接在外面呼叫表示可以直接進行修改，會造成資料的不安全。
# print(hungbank.balance)
# hungbank.balance = 100000
# print(hungbank.balance)

#Ch12_4  存款、提款、顯示餘額
# class Banks():
#     bankname = "Taipei Bank"
#     def __init__(self, uname, money):
#         self.name = uname 
#         self.balance = money 
#     def save_money(self, money):
#         self.balance += money 
#         print("存款", money, "完成")
#     def withdraw_money(self, money):
#         self.balance -= money 
#         print("提款", money, "完成")

#     def get_balance(self):
#         print(self.name.title(), "目前餘額：", self.balance)

# hungbank = Banks("hung", 100)
# hungbank.get_balance()
# hungbank.save_money(300)
# hungbank.get_balance()
# hungbank.withdraw_money(200)
# hungbank.get_balance()

#ch12_5
# """
# 設定好Ch12_4之後，就可以直接建立不同人的銀行內容
# """

