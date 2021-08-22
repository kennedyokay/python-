"""
#1
word = "Silicon Stone Education is an unbiased organization, concentrated on bridging the gap between academic and the working in order to benefit society as a whole. We have carefully crafted our online certification system and test content databases. The content for each topic is created by experts and is all carefully designed with a comprehnsive knowledge to greatly benefit all candidates who participate."
print(word)
word_lower = word.lower()
#print(word_lower)
new_word = ""
for ch in word_lower:
  if ch in ", . ?":
    new_word = word_lower.replace(ch, " ")
#print(new_word)
final = set(new_word.split())
print("-------")
print("final answer:", final)
"""
"""
#2 
A = []
B = []
for a in range(1, 101, 2):
  A.append(a) #不用加A = A.append(a)
#print("A=", A)
for b in range(0, 101, 5):
  B.append(b)
#print("B=", B)
A = set(A)
B = set(B)
print("-----------")
print("A=", A, "\n")
print("B=", B)
print("---------------")
print("交集：{}\n聨集：{}\nＡＢ差集：{}\nＢＡ差集：{}".format(A&B, A|B, A-B, B-A))
"""
"""
#3 
print("------")
Math = "Peter Norton Kevin Mary John Ford Nelson Damon Ivan Tom"
Computer = "Curry James Mary Turisa Tracy Judy Lee jarmul Damon Ivan"
Physics = "Eric Lee Kevin Mary Christy Josh Nelson Kazil Linda Tom"
M = set(Math.split())
C = set(Computer.split())
P = set(Physics.split())
print("同時參加三個夏令營名單：{}".format(M&C&P), "\n")
print("同時參加數學與電腦夏令營名單：{}".format(M&C), "\n")
print("同時參加數學與物理夏令營名單：{}".format(M&P), "\n")
print("同時參加電腦與物理夏令營名單：{}".format(C&P), "\n")
"""
"""
#4
A = []
B = []
for a in range(1, 100, 2):
  A.append(a)
for b in range(101):
  C = []
  for x in range(1, b+1):
    if b % x == 0:
      C.append(b)
  if len(C) == 2:
    B.append(b)
#print(B)
A = set(A)
B = set(B)
print("AB交集為：{}\nAB聯集為：{}\nA-B差集為：{}\nB-A差集為：{}\nAB對稱差集為：{}\nBA對稱差集為：{}".format(A&B, A|B, A-B, B-A, A^B, B^A))
"""
"""
#5
a = "Are you sleeping, are you sleeping, Brother John, Brother John,Morning bells are ringing, morning bells are ringing. Ding ding dong, Ding ding dong."
aLower = a.lower()
for ch in aLower:
  if ch in ",.?":
    aLower = aLower.replace(ch,"")
a_split = aLower.split()
#print(a_split)
times = {c:a_split.count(c) for c in set(a_split)} #set 可以增加程式效率
print("次數", times)
times = list(times)
times.sort(reverse = True)
print("由少到多", times)
"""
"""
#6
A = set()
print(A)
B = set()
for a in range(1, 101, 2):
  A.add(a) #不用加A = A.append(a)
#print("A=", A)
for b in range(0, 101, 5):
  B.add(b)
#print("B=", B)
# A = set(A)
# B = set(B)
print("-----------")
print("A=", A, "\n")
print("B=", B)
print("---------------")
print("交集：{}\n聨集：{}\nＡＢ差集：{}\nＢＡ差集：{}".format(A&B, A|B, A-B, B-A))
"""

#7
cocktail = {
"Horse\'s_Neck" : {"brandy", "ginger soda", "vodka"},
"Cosmopolitan" : {"vodka", "sweet wine", "lime juice", "cranberry juice"},
"Sex on the Beach" : {"vodka", "Peach Liqueur", "orange juice", "cranberry juice"},
}
# print(cocktail)
print("包含Vodka：")
for name, formulas in cocktail.items():
  if "vodka" in formulas:
    print(name)
print("包含sweet wine：")
for name, formulas in cocktail.items():
  if "sweet wine" in formulas:
    print(name)
print("包含Vodka和cranberry juice：")
for name, formulas in cocktail.items():
  if "vodka" and "cranberry juice" in formulas:
    print(name)
print("有Vodka但沒有cranberry juice的：")
for name, formulas in cocktail.items():
  if "vodka" in formulas and "cranberry juice" not in formulas:
    print(name)