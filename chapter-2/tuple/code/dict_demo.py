# coding: utf-8


# 定义空 dict
foo_dict = {}

# 新增元素到 dict 中, key 1 value 'a' 和 key 2 value 'b'
foo_dict[1] = 'a'
foo_dict[2] = 'b'

# 修改 dict 中的元素, 修改 key 1 的 value 为 'e'
foo_dict[1] = 'e'
print foo_dict

# 删除 dict 中的 key 为 1 的元素
del foo_dict[1]
print foo_dict

# 使用 get 方法获取 dict 中的元素，若 key 不存在，则默认返回 value 0
# 获取 key 为 2 的元素的 value
bar = foo_dict.get(2, 0)
# 获取 key 为 3 的元素的 value
bar = foo_dict.get(3, 0)

# 使用 pop 方法获取 dict 中的元素，若 key 不存在，则默认返回 value False
bar = foo_dict.pop(2, False)
bar = foo_dict.pop(5, False)

# 使用 update 方法扩展一个 dict
foo_dict = {1: 1, 2: 2}
bar_dict = {3: 3, 4: 4}
foo_dict.update(bar_dict)
# foo_dict 的值 {1: 1, 2: 2, 3: 3, 4: 4}

# 使用 items 方法获取 dict 的所有元素
foo_dict = {1: 'a', 2: 'b'}
all_items = foo_dict.items()
# all_items 的值 [(1, 'a'), (2, 'b')]

# 使用 keys 方法获取 dict 的所有 key
foo_dict = {1: 'a', 2: 'b'}
all_items = foo_dict.keys()
# all_items 的值 [1, 2]

# 使用 values 方法获取 dict 的所有 value
foo_dict = {1: 'a', 2: 'b'}
all_items = foo_dict.keys()
# all_items 的值 ['a', 'b']

# 遍历 dict，打印输出所有 key 和 value
foo_dict = {1: 'a', 2: 'b'}
for key, value in foo_dict.items():
    print key, value
