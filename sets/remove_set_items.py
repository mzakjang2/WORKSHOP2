thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # {'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)  # {'apple', 'cherry'}


thisset = {"apple", "banana", "cherry"}
thisset.pop()  # สุ่มตัวนึงจาก3ตัวออก
print(thisset)  # {'apple', 'cherry'}


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # {}