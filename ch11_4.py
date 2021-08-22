"""
# ch11_40 函數應用—替代字幕與運算
def modifySong(songStr):
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch, "")
    return songStr


def wordCount(songCount):
    global mydict
    songList = songCount.split()  # 字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    mydict = {wd: songList.count(wd) for wd in set(songList)}


data = "Are you sleeping, are you sleeping, Brother John, Brother John? Morning bells are ringing, morning bells are ringing. Ding ding dong, Ding ding dong."

mydict = {}
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)
print("以下是最後執行結果")
print(mydict)
"""
"""
#ch41 函數應用—質數 (prime numbe)
def isPrime(num):
  #測試num是否為質數#
  for n in range(2, num):
    if num % n == 0:
      return False
  return True
num = int(input("請輸入大於1的整數坐質數測試 = "))
if isPrime(num):
  print("%d是質數" % num)
else:
  print("%d不是質數" % num)
"""
"""
#ch11_42
def gcd(n1, n2):
  g = 1 
  n = 2 
  while n <= n1 and n1 <= n2:
    if n1 % n == 0 and n2 % n == 0:
      g = n
    n += 1
  #return g
  while  n <= n2 and n2 <= n1:
    if n2 % n == 0 and n1 % n == 0:
      g = n
    n += 1
  return g
  
n1, n2 = eval(input("請輸入兩個整數值："))
print("最大公約數：", gcd(n1, n2))
"""
"""
#ch11_43 輾轉相除法
def gcd(a, b):
  if a < b:
    a, b = b, a
  while b != 0:
    tmp = a % b
    a=b
    b =tmp
  return a
n1, n2 = eval(input("請輸入兩個整數值："))
print("最大公約數：", gcd(n1, n2))
"""
"""
#ch11_44 遞迴式函數設計處理歐幾里得算法
def gcd(a, b):
  return a if b == 0 else gcd(b, a %b)
  
a, b = eval(input("請輸入2個整數值："))
print("最大公約數是：", gcd(a, b))
"""

#ch11_45 最小公約數(least common multiple)
def gcd(a,b):
  return a if b ==0 else gcd(b, a %b)

def lcm(a, b):
  return a * b // gcd(a, b)

a, b = eval(input("請輸入2個整數值："))
print("最大公約數為：", gcd(a, b))
print("最小公倍數為：", lcm(a, b))