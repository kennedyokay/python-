"""
許多類別可以達成目標，可以修改該類別達成所需工作，但這樣會讓工作變複雜，或是可以重新寫新的類別，但這樣會需要維護更多新程式。
因此，這個情況就可以使用"類別的繼承"。

類別的繼承：
物件導向中類別是可以繼承的，
被繼承者： 父類別(parent class)、基底類別(case class)、超類別(superclass)
繼承者： 子類別(child class)、衍生類別(derived class)。

類別繼承最大優點為：可以在child class中，直接引用parent class中的方法或屬性。
結構如下：
class BaseClassName(): #先定義base class
    Base Class 內容
cless DerivedClassName(BaseClassName): #再定義derived class
    Derived Class 內容
derived class 會繼承base class 的公有屬性與公有方法，並擁有自己的屬性與方法。
"""

#ch12_9_8 繼承類別範例
# class Father(): #定義bass class
#     def hometown(self): #定義bass class 的內容
#         print("我住在台北")

# class Son(Father): #定義child class
#     pass  #定義child class 的內容

# hung = Father()
# ivan = Son()
# hung.hometown()
# ivan.hometown() #child class 引用 base class 的方法

#ch12_10
# class Banks():
#     def __init__(self, uname):
#         self.name = uname
#         self.balance = 0 
#     def save_money(self, money):
#         self.balance += money 
#         print("存款", money, "完成")
#     def withdraw_money(self, money):
#         self.balance -= money 
#         print("提款", money, "完成")

#     def get_balance(self):
#         print(self.name.title(), "目前餘額：", self.balance)

# class Shilin_Banks(Banks):
#     #定義士林銀行
#     pass 

# hungbank = Shilin_Banks("hung")
# hungbank.save_money(500)
# hungbank.get_balance()

