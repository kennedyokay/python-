# 深複製與淺複製 以dictionaty 為例
"""
dic = {"a": [1,2,3], "b":[4,5,6]}
dic2 = dic.copy()
print(dic2)
# 增加鍵值進入dic2
dic2["c"] = [7,8,9]
print("dic={}, dic2={}".format(dic, dic2) 
dic2["a"].append(4)
print("dic={}, dic2={}".format(dic, dic2) # 增加2但因為淺複製，因此跟著改變，增加內容不會，但改變值會
"""
"""
#深複製
import copy
dic3 = {"a":[1,2,3]}
dic4 = copy.deepcopy(dic3)
print("dic3={}, dic4={}".format(dic3, dic4))
dic4["a"].append(4)
print("dic3={}, dic4={}".format(dic3, dic4))
"""
"""
#合併字典
dealerA = {1:"Nissan", 2:"Toyota", 3:"Lexus"}
dealerB = {3:"BMW", 4:"Benz"}
print("A={}, B={}".format(dealerA, dealerB))
dealerB.update(dealerA)
print("New A = %s" %(dealerB))()
"""
"""
armys = []
for soldier_number in range(50):
  soldier = {"tag":"red", "score":3, "speed":"slow"}
  armys.append(soldier)
#for soldier in armys[:3]:
  print("soldier{}".format(soldier_number), soldier)
print("number=", len(armys))
"""
"""
#字典內鍵的值為串列 items()應用
sports = {"Curry":["basketball", "football"], 
          "Durant":["baseball"], 
          "James":["football", "baseball", "basketball"]}
for name, favorite_sport in sports.items():
  print("球員%s：" %(name))
  for sport in favorite_sport:
    print("喜歡的運動是%s" %sport)
"""
"""
#字典內鍵的值是字典時 item()應用
wechat_account = {"cshung":{"last_name":"洪", "first_name":"錦魁", "city":"台北"}, 
                  "kevin":{"last_name":"鄭", "first_name":"義盟", "city":"北京"}}
for account, account_info in wechat_account.items():
  print("使用者名稱", account)
  print("使用者姓名:{}{}".format(account_info["last_name"], account_info["first_name"]))
  print("城市:{}".format(account_info["city"]))
"""
"""
# get() setdefault 用法
fruits = {"apple":20, "orange":25}
ret_value1 = fruits.get("apple")
print(ret_value1)
ret_value2 = fruits.get("grape")
print(ret_value2)
ret_value3 = fruits.get("grape", 10)
print(ret_value3)
print(fruits) # It doesn't add the key-value into the dictionary

# setdefault
ret_value4 = fruits.setdefault("apple")
print(ret_value4)
#ret_value5 = fruits.setdefault("banana")
#print(ret_value5) #It show none, and then add the key-value into the dictionary
ret_value6 = fruits.setdefault("banana", 50)
print(ret_value6) 
print(fruits) # The setdefault will add the key-value into the dictionary
"""
"""
word = "deepstone"
alphabetCount = {alphabet:word.count(alphabet) for alphabet in word}
print(alphabetCount)
"""
