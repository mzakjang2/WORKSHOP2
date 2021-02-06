# example1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # ['apple', 'cherry']#ลบbanana

# example2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # ['apple', 'cherry'] #ลบbanana

# example3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # ['apple', 'banana'] #จะลบตัวสุดท้ายของlist

# example4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # ['banana', 'cherry'] #ตำแหน่งที่0

# example1
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # []