# coding: utf-8


gold_list = [1, 2, 3, 8, 7, 'gold', 22, 45, 'ff']
for i in gold_list:
    if i == 'gold':
        print 'find it'
        continue
    print i
