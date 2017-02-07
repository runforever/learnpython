# coding: utf-8

# 定义一个 list，里面包含 "hello", 1, 1.1
foo_list = ["hello", 1, 1.1]

# 根据下标打印列表中第一个和第二个元素的值
print foo_list[0], foo_list[1]
# 结果 hello，1

# 添加元素 2 到上面的列表末尾
foo_list.append(2)
print foo_list
# 结果 ['hello', 1, 1.1, 2]

# 修改第一元素为hi
foo_list[0] = "hi"
print foo_list[0]
# 结果 hi

# 查看 list 的长度
print len(foo_list)
# 结果 4
