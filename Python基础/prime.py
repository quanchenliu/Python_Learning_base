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
