# list1


fruits = ["apple", "banana", "cherry"]
apple, banana, cherry = fruits
print(apple)
print(banana)
print(cherry)

print("------------")
# tuple #กรณีเยอะจะไม่ใช้
fruits = ("apple", "banana", "cherry")
# แบบ 1
(apple, banana, cherry) = fruits

# แบบ 2
apple = fruits[0]
banana = fruits[1]
fruits = fruits[2]


print(apple)
print(banana)
print(cherry)