
def main():
    sum = 0
    i = 1

    while i <= 100:                     # 计算1~100的和
        sum += i
        i += 1
    print('1~100的和为:{}'.format(sum))

    total = 0
    j = 1
    while j <= 100:
        if j % 3 == 0:
            total += j
        j +=1
    print('1~100内能被3整除的整数之和:{}'.format(total))


if __name__ == "__main__":
    main()
