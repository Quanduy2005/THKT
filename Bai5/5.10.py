﻿print("Sinh vien: Nguyen Duy Quan")
print("Ma so SV:235752021610107")
print("**************************")

from sort_module import bubbleSort
n = int(input("Nhập số lượng phần tử trong danh sách: "))
nlist = []
for i in range(n):
  value = float(input(f"Nhập phần tử thứ {i+1}: "))
  nlist.append(value)

sorted_list = bubbleSort(nlist)

print("Danh sách sau khi sắp xếp:", sorted_list)