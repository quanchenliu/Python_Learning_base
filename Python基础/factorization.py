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
