# coding: utf-8

# 定义 tuple
fruit_tuple = ("apple", "mongo", "pear", "grape")

# 查看 tuple
print fruit_tuple[0]

# tuple 不能修改，但是可以用 tuple 组成新的 tuple
foo_tuple = (1, 2, 3)
bar_tuple = (4, 5, 6)
merge_tuple = foo_tuple + bar_tuple
# merge_tuple 是 (1, 2, 3, 4, 5, 6)
print merge_tuple
