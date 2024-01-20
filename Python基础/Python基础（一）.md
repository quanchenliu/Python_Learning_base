# Python基础（一）

```python
# Author	: @quanchenliu
# Time		: 2024/1/15
# Function	: guess_number/
```



## 一、猜数游戏

```python
import random

def Judge(num, x):
    if x == num:
        return True
    elif x > num:
        print('larger, please try again')
        return False
    elif x < num:
        print('smaller, please try again')
        return False

def main():
    num = random.randint(1, 100)    # 生成一个随机数
    is_done = False                 # 用于判断是否成功
    while not is_done:
        x = int(input('please enter an integer:'))  # input输入的是字符，因此需要转换成int
        if 1 <= x <= 100:
            is_done = Judge(num, x)
        else:
            print('The integer is error!')
    print('Success! The answer is {}'.format(num))


if __name__ == "__main__":
    main()

```

![image-20240115205517286](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240115205517286.png)

## 二、数与数制

```python
num1 = 42
num2 = 42.5
a = bin(num1)       # 二进制
b = oct(num1)       # 八进制
c = hex(num1)       # 十六进制
d = float(num1)     # 浮点数
e = int(num2)       # 整数
print(a,b,c,d,e)
```

![image-20240115211403562](C:\Users\DELL\AppData\Roaming\Typora\typora-user-images\image-20240115211403562.png)



## 三、闰年

```python
def main():
    year = int(input('请输入年份:'))

    if (year % 400) == 0:  # 能被400整除
        print('{}是一个闰年'.format(year))
    elif (year % 4) == 0 and (year % 100) != 0:  # 能被4整除，且不能被100整除
        print('{}是一个闰年'.format(year))
    else:
        print('{}不是闰年'.format(year))


if __name__ == "__main__":
    main()

```

## 四、分解因式

```python
def factorize(number):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number /= divisor  # 除法
        else:
            divisor += 1

    return factors


def main():
    try:
        user_input = int(input("请输入一个小于1000的整数: "))
        if 0 < user_input < 1000:
            result = factorize(user_input)  # 调用因式分解函数实现因式分解

            if len(result) == 1:            # 输入的是质数
                print(f"{user_input}是质数。")
            else:
                # ' × '.join(map(str, result)) 将因数列表中的每个因数转换为字符串，然后用 '×' 连接起来，表示因式分解的形式。
                print(f"{user_input}的因数分解为: {' × '.join(map(str, result))}")

        else:                               # 输入非法数据
            print("输入无效，请输入小于1000的整数。")
    except ValueError:                      # 因式分解过程出现异常
        print("输入无效，请输入一个有效的整数。")


if __name__ == "__main__":
    main()

```

## 五、求质数

```python
import math

def prime(nums, ranges):
    for i in range(ranges + 1):  # 包括 0 到 cal_range（含）的整数
        if i == 0 or i == 1:  # 0、1 不是质数
            continue
        # 试除法来判断一个数是否为质数
        num = 2
        while num <= math.sqrt(i):  # 判断条件 num <= math.sqrt(i) 用于确保只需试除到该数的平方根即可
            if i % num == 0:  # 若出现一个能够整除的整数，则说明不是质数
                break
            else:
                num += 1
        # 如果 num 超过了平方根，说明没有小于等于平方根的因数，即该数是质数。
        if num > math.sqrt(i):
            nums.append(i)

def main():
    cal_range = int(input('请输入计算质数的范围：'))
    prime_nums = []
    prime(prime_nums, cal_range)

    for i in prime_nums:
        print(i, end=' ')


if __name__ == "__main__":
    main()
```

## 六、列表、元组、字典——词频统计

```python
p = '''
I heard the echo, from the valleys and the heart
Open to the lonely soul of sickle harvesting
Repeat outrightly, but also repeat the well-being of
Eventually swaying in the desert oasis
I believe I am
Born as the bright summer flowers
Do not withered undefeated fiery demon rule
Heart rate and breathing to bear the load of the cumbersome
Bored
'''


def count1():
    # p.strip(): 去除字符串两端的空白字符（包括空格、制表符等）
    # p.strip().split('\n'): 将字符串按照换行符 \n 进行分割，得到一个包含每行文本的列表。
    lines = p.strip().split('\n')
    words_cnt = {}  # 定义空字典{key:value}

    for line in lines:
        line = line.replace(',', '').lower()  # 删去逗号
        words = line.split(' ')  # 将字符串按照空格进行划分
        for word in words:
            # 使用 get 方法获取字典words_cnt中 word 的值，否则返回0
            words_cnt[word] = words_cnt.get(word, 0) + 1

    # zip() 创建了一个迭代器，将 words_cnt 字典的值(单词出现次数，value)和键(单词本身，key)配对，形成新的元组。
    # 通过 list() 将元组转化为列表
    # 即：words_lst 是一个列表，每个元素都是一个元组。
    words_lst = list(zip(words_cnt.values(), words_cnt.keys()))

    # sort() 方法默认对列表的第一个元素进行升序排序, reverse=True: 对元组的第一个元素进行降序排序
    words_lst.sort(reverse=True)

    for word in words_lst:
        # word[1] 表示元组中的第二个元素，即单词本身；words_cnt[word[1]] 表示该单词的出现次数
        print(word[1], word[0])  # print(word[1], words_cnt[word[1]]), 二者等价

    print("////////////////////count1 over///////////////////////")

def count2():
    lines = p.strip().split('\n')
    words_cnt = {}

    for line in lines:
        line = line.replace(',', '').lower()
        words = line.split(' ')
        for word in words:
            words_cnt[word] = words_cnt.get(word, 0) + 1

    # 将字典按照值（频率）降序排列
    # words_cnt.items()     : 返回字典 words_cnt 中包含键值对的元组列表。
    # key=lambda x: x[1]    : 指定排序的依据是元组中的第二个元素，即频率。
    # reverse=True          : 表示降序排序。
    sorted_words = sorted(words_cnt.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_words:
        print(word, count)

    print("////////////////////count2 over///////////////////////")


def main():
    count1()
    count2()


if __name__ == "__main__":
    main()

```

### （一）元组（tuple）和列表（list）

在Python中，元组（tuple）和列表（list）是两种不同的数据类型，它们有一些关键的区别：

1. **可变性：**
   - **元组是不可变的（immutable）：** 一旦创建，元组的元素不能被修改、添加或删除。你不能对元组进行任何更改。
   - **列表是可变的（mutable）：** 列表允许在创建后修改其元素，可以添加、删除或更改列表的元素。

2. **语法：**
   - **元组使用小括号 `( )`：** 例如，`my_tuple = (1, 2, 3)`。
   - **列表使用方括号 `[ ]`：** 例如，`my_list = [1, 2, 3]`。

3. **性能：**
   - **元组通常比列表更轻量，因为它们是不可变的：** 这意味着在创建后，元组不需要额外的内存来支持在运行时的修改操作。
   - **列表在需要频繁修改的情况下可能更适用：** 由于其可变性，列表允许更灵活的操作，但在一些场景下可能会导致性能开销。

4. **适用场景：**
   - **元组适用于不可变的数据集合：** 当你有一些常量数据，不希望被改变时，可以使用元组。
   - **列表适用于需要动态操作的数据集合：** 当你需要在程序运行时添加、删除或修改元素时，使用列表更合适。

总体来说，选择使用元组还是列表取决于你的具体需求。**如果你需要一个不可变的数据集合，使用元组；如果你需要一个可变的数据集合，使用列表**。

### （二）字典（dist）和列表（list）

在Python中，`dict`（字典）和`list`（列表）是两种不同的数据结构，它们有以下区别：

1. **数据结构：**
   - **dict（字典）：** 是一种键值对（key-value）的数据结构，其中每个值都与一个唯一的键相关联。字典是通过哈希表实现的，因此访问字典中的元素非常高效，其时间复杂度为 O(1)。
   - **list（列表）：** 是一个有序的集合，其中的元素可以是任意类型的。列表中的元素是按照它们在列表中的顺序存储的，因此访问列表中的元素的时间复杂度为 O(n)，其中 n 是列表的长度。

2. **索引：**
   - **dict：** 使用唯一的键来检索值，不支持索引。键可以是不可变的数据类型，如字符串、数字或元组。
   - **list：** 使用整数索引来检索列表中的元素。可以通过索引直接访问列表中的元素。

3. **可变性：**
   - **dict：** 是可变的，可以通过添加、删除或更改键值对来修改字典。
   - **list：** 是可变的，可以通过添加、删除或更改元素来修改列表。

4. **存储顺序：**
   - **dict：** 在 Python 3.7+ 中，字典开始保持插入的顺序，这意味着元素的顺序与它们添加到字典中的顺序相同。
   - **list：** 元素在列表中的顺序就是它们被添加到列表的顺序。

5. **内部实现：**
   - **dict：** 使用哈希表来实现。哈希表是一种高效的数据结构，允许在平均情况下以常数时间复杂度执行插入、删除和查找操作。
   - **list：** 使用动态数组来实现，支持动态扩展和收缩。

总的来说，`dict`适用于通过键来查找和关联值的场景，而`list`适用于需要按顺序存储和访问元素的场景。在具体使用时，根据数据的特性和访问模式选择适当的数据结构。

## 七、集合

```python
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
```

## 八、函数

```python
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
```

## 九、时间与日期

```python
import time
print(time.time())  # 1970年1月1日0分0秒至今 所经历的秒数, 又称为时间戳

t = time.localtime()
print(time.localtime())

# Y: 年份（四位数）        %y: 年份（两位数）     %m: 月份               %d: 日期
# %H: 小时（24小时制）     %I: 小时（12小时制）   %M: 分钟               %S: 秒
s = time.strftime('%a %b %d %I:%M%p %Y', t)
print(s)
print('/////////////////time model//////////////////')

from datetime import date
d = date.today()
print('今天是{}'.format(d))                              # 输出年、月、日
print('{}是星期{}'.format(d, date.weekday(d)))           # 返回该日期是星期几（0是星期一）
print('{}是星期{}'.format(d, date.isoweekday(d)))        # 返回该日期是星期几（1是星期一）
print(d.strftime("%Y-%m-%d"))                           # 将日期格式化为字符串


print('/////////////////datetime model//////////////////')
```

十、文件















