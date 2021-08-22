#ch07_practice2

"""
#12
title = "9x9 Culculate Table"
print(title.center(68, " "))
for i in range(1,10):
  for j in range(1,10):
    ans = i * j
    print("%d*%d=%3d" %(i, j, ans), end=" ")
  print()
"""


#13
t = 0
n = int(input("Please enter the number:"))
for x in range(2,n+1):
  if x == 2:
    t += 1
    print("%d是質數，第%d個質數" %(x, t))
    continue
  else:
    for y in range(2,n+1):
      if x % y ==0:
        #print("%d不是質數" %(x))
        break
      elif x % y !=0:
        t += 1
        print("%d是質數，第%d個質數" %(x, t))
        break


"""
#14
ans = 30 #自訂答案
guess = 0
t = 0
while guess != ans:
  guess = int(input("輸入1-100："))
  if guess > ans:
    t += 1 
    print("現在值為；%d，請猜小一點，這是第%d次猜" %(guess, t))
  elif guess < ans:
    t += 1
    print("現在值為；%d，請猜大一點，這是第%d次猜" %(guess, t))
  else:
    t += 1
    print("答案為；%d，恭喜答對，總共猜了%d次" %(guess, t))
"""

"""
#15
buyers = [["James", 1030], ["Curry", 893], ["Durant", 2050], ["Jordan", 990], ["David", 2110], ]
gold_buyers = []
vip_buyers = []
while buyers:
  index_buyer = buyers.pop()
  if index_buyer[1] >= 1000:
    vip_buyers.append(index_buyer)
  else:
    gold_buyers.append(index_buyer) 
print("VIP=", vip_buyers, "GOLD=", gold_buyers)
"""
"""
#16
num1 = int(input("數字一："))
num2 = int(input("數字二："))
CD1 = [n1 for n1 in range(1,num1+1) if num1 % n1 ==0] # CD of num1
CD2 = [n2 for n2 in range(1,num2+1) if num2 % n2 ==0] # CD of num2
if num1 > num2:
  CD = [c1 for c1 in CD2 if c1 in CD1]
  print("{}與{}的公因數為：{}".format(num1, num2, CD))
  print("{}與{}的最大公因數為：{}".format(num1, num2, CD.pop()))
elif num1 < num2:
  CD = [c1 for c1 in CD2 if c1 in CD1]
  print("{}與{}的公因數為：{}".format(num1, num2, CD))
  print("{}與{}的最大公因數為：{}".format(num1, num2, CD.pop()))
"""
"""
#17
fruits = ["李子", "香蕉", "蘋果", "西瓜", "桃子"]
for fruit in enumerate(fruits, 11):
  print(fruit)
"""