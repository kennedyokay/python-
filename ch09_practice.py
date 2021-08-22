"""
#1
week = {"monday":"星期一", "tuesday":"星期二", "wednesday":"星期三", "thusday":"星期四", "friday":"星期五", "saturday":"星期六", "sunday":"星期日"}
date = (input("Please enter the date:"))
if date.lower() not in week:
  print("Wrong")
else:
  print(week[date.lower()])
"""
"""
#2
months = {"一月":"January", "二月":"Feburary", "三月":"March","四月":"Apirl", "五月":"May", "六月":"June", "七月":"July", "八月":"August", "九月":"Septembers", "十月":"October", "十一月":"November", "十二月":"December"}
month = (input("請出入月份："))
if month in months:
  print(months[month])
else:
  print("Wrong")
"""
"""
#3
fruits = {"Watermelon":50, "Banana":20, "Pineapple":25, "Orange":12, "Apple":18}
new_fruits = {}
print(fruits)
for name in sorted(fruits.keys()):
  new_fruits[name] = fruits[name]
print(new_fruits)
"""
"""
#4,5 %%%%%%%%%%
noodles = {"牛肉麵":100, "肉絲麵":80, "陽春麵":60, "大滷麵":90, "麻醬麵":70}
new_noodles = {}
print(noodles)
for price in sorted(noodles.values()):
"""
"""
#6
armys = []
for soldier in range(50):
  soldier = {"tag":"red", "score":3, "speed":"slow"}
  armys.append(soldier)
print(armys)
print("------")
for soldier2 in armys[47:50]:
  if soldier2["tag"] == "red":
    soldier2["tag"] = "green" 
    soldier2["score"] = 10 
    soldier2["speed"] = "fast" 
print(armys)
"""
"""
#7是字典時 item()應用
cities = {"台北":{"first":"中山", 
                 "secend":"永和", 
                 "thired":"信義"},
           "台中":{"first":"烏日", 
                   "secend":"西區", 
                   "thired":"梧棲"},
           "高雄":{"first":"三民", 
                  "secend":"鳳山", 
                  "thired":"岡山"}, }
print(cities)
for city, place in cities.items():
  print(city, place)
  print(place["first"])
"""
