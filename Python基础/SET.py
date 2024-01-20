x = set('abcd')
print(x)

y = set([1, 2, 3, 4, 5])        # 集合的初始化，会自动拆分字符串和列表
print(y)

x.add('hello world')            # add() 方法添加的元素是一个整体，不会被拆分
print(x)
x.remove('a')
print(x)

y.add(6)
print(y)
y.remove(5)
print(y)
print('///////////////////////////////////////////')
a = set('abcd')
b = set('cdef')
print(a-b, b-a)     # 求差集
print(a&b)          # 求交集
print(a|b)          # 求并集
