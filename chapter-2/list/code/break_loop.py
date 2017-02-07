# coding: utf-8


gold_list = [1, 2, 3, 8, 7, 'gold', 22, 45, 'ff']
for i in gold_list:
    # 使用 if 条件判断是否找到 gold
    # 如果找到打印 'find it' 并且结束循环
    # 如果没有找到直接打印当前遍历的元素
    if i == 'gold':
        print 'find it'
        break
    print i
