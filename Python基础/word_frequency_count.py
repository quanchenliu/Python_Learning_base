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
        line = line.replace(',', '').lower()  # replace() 删去逗号, lower() 将大写字符转为小写
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
