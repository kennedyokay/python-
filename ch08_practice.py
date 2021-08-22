"""
#1
group = ("Jhon", "Peter", "Curry", "Mike", "Kevin")
for name in group:
  print(name)
"""
"""
#3
group = ("Jhon", "Peter", "Curry", "Mike", "Kevin")
group = group + ("Mary", "Tom", "Carlo")
print(group)
"""
"""
#4
tp = (1,2,3,4,5,2,3,1,4)
ltp = list(tp)
new_tp=[]
print(ltp)
for n1 in ltp:
  index_tp=ltp.pop()
  #print(index_tp)
  if index_tp in ltp:
    continue
  else:
    ltp.append(index_tp)
    new_tp = tuple(ltp)
    print(new_tp)
"""
"""
#5
season = ("Spring", "Summer", "Full", "Winter")
chinese = ("春天", "夏天", "秋天", "冬天")
zipdata = zip(season, chinese)
print(zipdata)
a = list(zipdata)
b = tuple(zipdata)
print(a)
print(b)
"""
"""
#6
T_max = (30, 28, 29, 31, 33, 35, 32)
T_min = (20, 21, 19, 22, 23, 24, 20)
highest = max(T_max)
lowest = min(T_min)
print("最高溫為{}，最低溫為{}".format(highest, lowest))
"""
"""
#7
a = (1100, 652, 946, 821, 955, 1024, 1155)
average = sum(a) / len(a)
print("平均值為%f" %(average))
varies = 0
for v in a:
  varies += ((v-average)**2)
varies = varies / (len(a)-1)
print("變異數為%f" %(varies))
deviation = 0
for v in a:
  deviation += ((v-average)**2)
deviation = (deviation/(len(a)-1))**0.5
print("標準差為{}".format(deviation))