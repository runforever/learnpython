# coding: utf-8


def get_multiple(value, multiple=2):
    return value * multiple

# 3 的 5 倍
print get_multiple(3, multiple=5)

# 6 的 3 倍，根据参数顺序，可以这样调用
print get_multiple(6, 3)

# 不传倍数，默认是 2 倍
print get_multiple(3)
