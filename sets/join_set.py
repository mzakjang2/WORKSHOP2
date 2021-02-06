set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3)  # {'d', 'f', 'e', 'a', 'c', 'b'}
# รวม

set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)  # {'d', 'f', 'e', 'a', 'c', 'b'}
# อัพเดท

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  # {'apple'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)  # {'banana', 'cherry', 'google', 'microsoft'}


# -----------------------
number_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
print(list(set(number_list)))
# vvvvvv like set
result = []
number_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
for number in number_list:
    if not number in number_list:
        result.append(number)
print(result)

# ของซ้ำอยากให้เป็นเดี่ยวๆใช้setครอบ