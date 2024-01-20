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
