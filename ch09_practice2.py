"""
#8
song = "Are you sleeping, are you sleeping, Brother John, Brother John, Morning bells are ringing, morning bells are ringring. Ding ding dong, Ding ding dong."
mydict = {}
songLower = song.lower()
for ch in songLower:
  if ch in ",.?":
    songLower = songLower.replace(ch,"")
print(songLower)
print("---------")
b = {c:songLower.count(c) for c in songLower}
del b[" "]
print(b)
max_value = max(b.values())
min_value = min(b.values())
ans = {}
for key in b.keys():
  if b[key] == max_value:
    ans[key] = max_value
    break
for key2 in b.keys():  
  if b[key2] == min_value:
    ans[key2] = min_value
    continue
"""
"""
#9
a = "Are you sleeping, are you sleeping, Brother John, Brother John, Morning bells are ringing, morning bells are ringring. Ding ding dong, Ding ding dong."
aLower = a.lower()
for ch in aLower:
  if ch in ",.?":
    aLower = aLower.replace(ch,"")
a_split = aLower.split()
#print(a_split)
times = {c:a_split.count(c) for c in a_split}
print(times)
"""

#10
abc = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(subText, abc))
print("密碼字典：\n", encry_dict)
msgText = "python"
chipher = []
for i in msgText:
  v = encry_dict[i]
  chipher.append(v)
chipherText = "".join(chipher)
print("原始碼：",msgText)
print("加密後：", chipherText)