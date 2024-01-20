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
