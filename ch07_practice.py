#Ch07_practice
"""
#1
files = ["da1.jpg", "da2.png", "da3.gif", "da4.gif", "da5.jpg", "da6.jpg", "da4.gif"]
print(files)
file_jpg = []
file_png = []
file_gif = []
for file in files:
  if file.endswith(".jpg"):
    file_jpg.append(file)
  elif file.endswith(".png"):
    file_png.append(file)
  elif file.endswith("gif"):
    file_gif.append(file)
print(file_jpg)
print(file_png)
print(file_gif)
"""

"""
#2 
players = ["James", 202], ["Curry", 193], ["Jordan", 199], ["David", 211]
print(players)
player_200 = []
for player in players:
  if player[:][1] > 200:
    player_200.append(player[:][0])
print("The players who higher than 200: ", player_200)
"""

"""
#3
money = int(input("Please enter the money:"))
rate = float(input("Pleaes enter the rate:"))
n = int(input("Please enter the years:"))
for i in range(n):
  money *= (1+rate)
  print("第 %d 年本金和： %d" %((i+1), int(money)))
"""

"""
#4 
wight = 50 
n = 1.2
for i in range(1,6):
  fw = wight + n*i
  print(fw)
"""

"""
#5 
n = int(input("Please enter a number for \"n\":"))
m = int(input("Please enter a number for \"m\":"))
n2 = 0
if m > n:
  for i in range(n,m+1):
    n2 += i
  print(n2)
if m <= n:
  print("The m have to greater then n")
else:
  print("Wrong type")
"""

"""
#6
F = [32, 77, 104]
for f in F:
  C = f *9/5 + 32 
  print(C)
"""

"""
#7 
a = range(2,21,2)
b = list(a)
#print(b)
l = []
for i in range(2,21,2):
  print(i)
  l.append(i)
print(l)

"""

"""
#8 
list = [1, 2, 3, 4, 5]
for i in list:
  for j in list:
    print([i, j])
"""

#9
i = int(input("Enter the i"))
e = 1 
y = 1
for x in range(1, i+1):
  y *= x
  e = e + 1/y 
  print(e)