a = {"python", "Jave", "C", "python"}
print(a) #會刪除重複的元素，集合不會有重複的元素
integer_set = {1, 2, 3, 4, 5}
print(integer_set)
mixed_set = {1, "python", (2, 5, 10)}
print(mixed_set)
b = {}
print(type(b))
c = set()
print(type(c))
fruits = ["apple", "orange", "apple"]
print(fruits)
x = set(fruits)
print(x)
y = list(x) #不會在轉變回去 會是刪去重複後的樣子
print(y)
"""
＆(.intersection):交集，  |(.union)：聯集，  -(.difference)：差集，  ^(.symmetric_difference)：對稱差集，  ==：等於，  !=：不等於，  in：是成員，  not in：不是成員
"""
"""
適用於集合的方法：.add(), clear(), copy(), difference_update() 刪除集合內與另一集合重複的元素, 
discard() 如果是集合成員則刪除, intersection_update() 可以使用交集更新集合內容, isdisjoint() 如果2個集合沒有交集返回True, 
isupperset() 如果這個集合包含另一個集合返回True, isupperset() 如果這個集合包含另一個集合返回True, 
pop() 傳回所刪除的元素，空集合則回傳Flase, remove()刪除指定元素，元素不在時回傳KeyError, 
symmetric_differende_update()使用對稱差集更新集合內容, update()使用聯集更新集合內容
"""
x = frozenset([1, 3, 5])
x1 = {1, 3, 5}
y = frozenset([5, 7 ,9])
print(x)
print(x1)
print(y)