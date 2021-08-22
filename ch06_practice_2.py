#ch06_practice_2.py
#7 
# str = "FBI Mark told CIA Linda that the secret USB hab given to FBI Peter"
# print(str)
# str = str.replace("FBI", "XX")
# print(str)

#8
# url = input("Please enter the webpage:")
# if url.startswith("http://" or "https://" or "HTTP://" or "HTTPS://"):
#   print("True")
# else:
#   print("Wrong")

#9 
# str = "Are you sleeping are you sleeping Brother John Brother John Morning bells are ringing morning bells are ringring Ding ding dong Ding ding dong"
# print(str)
# lit = str.split()
# print(lit)
# print(len(lit))
# print(str.count("John"))

#11 
# list = []
# print("1. Add the invitation")
# print("2. Delete the invitation")
# print("3. End the system")
# while True:
#   choice = int(input("Please choice:"))
#   if choice ==1:
#     add = input("Please increase the participant")
#     list.append(add)
#     print(list)
#     continue
#   if choice ==2:
#     delete = input("Please enter")
#     del list["delete"]
#     print(list)
#     continue
#   if choice ==3:
#     print("End the system")
#     break
#   else:
#     print("Wrong enter")
#     break

#12 
abc = ["abcdefghijklmnopqrstuvwxyz"]
a1 = abc[0][5:]
a2 = abc[0][0:4]
abc_new = a1 + a2
print(abc_new)