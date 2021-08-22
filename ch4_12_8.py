# sp = " " * 40
# print("%s        12341 Delta Rd" %sp)
# print("%s        Oxford, Mississippi" %sp)
# print("%s        USA\n\n\n" %sp)
# print("Dear Ivan")
# print("I am pleased to inform you that your application or fall 2020 has")
# print("been facorably reviewed by the Electrical and Computer Engineering")
# print("Office.\n\n")
# print("Best Regards")
# print("Peter Malong")
# print("----------------------")
x = "D:\Important\\tutroABC.txt"
# y=open("D:\Important\\tutroABC.txt",mode="r", encoding="utf-8")
with open("D:\Important\KMU\OMG\\316XRD\\1.txt", mode="r") as f:
    y=f.read()
    print(y)
print(type(y))