class Bitmap:
    def __init__(self, size):
        # 初始化位图，size表示位图的大小
        self.size = size
        self.bitmap = [0] * ((size + 31) // 32)  # 每个元素32位

    def set_bit(self, index):
        # 将指定位置的比特位设为1
        if index < 0 or index >= self.size:
            raise ValueError("Index out of range")

        word_index = index // 32
        bit_index = index % 32
        self.bitmap[word_index] |= (1 << bit_index)

    def clear_bit(self, index):
        # 将指定位置的比特位设为0
        if index < 0 or index >= self.size:
            raise ValueError("Index out of range")
        word_index = index // 32
        bit_index = index % 32
        self.bitmap[word_index] &= ~(1 << bit_index)

    def get_bit(self, index):
        # 获取指定位置的比特位值
        if index < 0 or index >= self.size:
            raise ValueError("Index out of range")
        word_index = index // 32
        bit_index = index % 32
        return (self.bitmap[word_index] & (1 << bit_index)) != 0

    def sort_numbers(self):
        # 输出排序后的数字列表
        sorted_result = []
        for i in range(self.size):
            if self.get_bit(i):
                sorted_result.append(i)
        return sorted_result

def main():
    # 示例用法
    bitmap_size = 64
    bitmap = Bitmap(bitmap_size)

    bitmap.set_bit(3)
    bitmap.set_bit(10)
    bitmap.set_bit(25)

    print(bitmap.get_bit(3))    # 输出 True
    print(bitmap.get_bit(5))    # 输出 False
    print(bitmap.get_bit(10))   # 输出 True

    unsorted_nums = [5, 3, 8, 1, 7, 9, 4, 2, 6, 0]
    max_num = max(unsorted_nums)            # 取数据中的最大值为位图的 size
    bm = Bitmap(max_num + 1)                # 数据从 0 开始，因此要 +1 才能保证取到 max_num
    for n in unsorted_nums:                 # 设置位图
        bm.set_bit(n)
    sorted_nums = bm.sort_numbers()         # 通过位图完成排序，并返回排序结果
    print("Sorted Numbers:", sorted_nums)

if __name__ == "__main__":
    main()
