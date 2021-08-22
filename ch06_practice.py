#ch06_practice
#1
# a=[84, 99, 69, 52, 78, 98, 80, 92]
# print(a[:])
# a.sort() # need to divide use  
# print(a)

#2 
# a=["Toyota", "Nissan", "Honda"]
# a[1] = "Ford"
# print(a)

#3 
# str1 = " Python "
# str2 = "is "
# str3 = " easy"
# str = str1.strip() + " " + str2.rstrip() + " " + str3.lstrip()
# print(str)

#4 
# sity = ["Taipai", "Tokyo", "Tainan", "New york", "Pington"]
# print(sity)
# sity.append("London")
# print(sity)
# sity.insert(3, "Xian")
# print(sity)
# sity.remove("Tokyo")
# print(sity)

#5 
# grade = [48, 59, 19, 80, 98]
# print(grade)
# grade.sort()
# print(grade)
# grade.sort(reverse=True)
# print(grade)
# d = max(grade)
# e = sum(grade)
# print("max={}, sum={}".format(d, e))

#6 
sc = [["洪錦魁", 80, 95, 88, 0, 0], 
["洪冰儒", 98, 97, 96, 0, 0],
["洪雨星", 90, 91, 92, 0, 0],
["洪冰雨", 91, 93, 95, 0, 0],
["洪星宇", 92, 97, 90, 0, 0],]
sc[0][4] = sum(sc[0][1:3])
sc[1][4] = sum(sc[1][1:3])
sc[2][4] = sum(sc[2][1:3])
sc[3][4] = sum(sc[3][1:3])
sc[4][4] = sum(sc[4][1:3])
sc[0][5] = sum(sc[0][1:3]) / 3
sc[1][5] = sum(sc[1][1:3]) / 3
sc[2][5] = sum(sc[2][1:3]) / 3
sc[3][5] = sum(sc[3][1:3]) / 3
sc[4][5] = sum(sc[4][1:3]) / 3
print("%s %2d %2d %2d %2d %2.1f" %(sc[0]))
