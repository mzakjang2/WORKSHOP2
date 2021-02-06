# EX 1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# {'apple', 'banana', 'cherry', 'orange'}
# #ไม่การันตีเรื่องตำแหน่ง

# EX 2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# {'mango', 'cherry', 'pineapple', 'apple', 'banana', 'papaya'}