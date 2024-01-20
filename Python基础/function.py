# def 函数名(*参数): ‘*参数’ 的作用是一次可以传入多个参数并保存在一个元组中
def test_collect1(*params):
    print(params)
test_collect1(1, 2, 3)                      # 输出: (1, 2, 3)


def test_collect2(name, *params):
    print(name, params)
test_collect2('Alpha', 1, 2, 3)             # 输出: Alpha (1, 2, 3)


def test_collect3(*params, name):
    print(name, params)
# test_collect3(1, 2, 3, 'Alpha')           # 发生异常
# test_collect3((1, 2, 3), 'Alpha')         # 发生异常
test_collect3(1, 2, 3, name='Alpha')        # 输出: Alpha (1, 2, 3)


# def 函数名(**参数): ‘**参数’ 的作用是一次可以传入多个参数并保存在一个字典中
def test_collect4(**params):
    print(params)
# 在调用此函数时，必须指明对应关键字的值
test_collect4(a=1, b=2)                     # 输出:{'a': 1, 'b': 2}


def test_collect5(a, *b, **c):
    print(a)
    print(b)
    print(c)
test_collect5(1, 2, 3, 4, x=5, y=6)         # 输出: 1     (2, 3, 4)       {'x': 5, 'y': 6}

# 使用 global 关键字声明全局变量
