def sort_word_better(word_list):
    # 使用列表推导式和字典来计算每个单词的出现次数
    # 同时将单词转换为小写并移除标点符号
    word_count = {}
    for word in word_list:
        # 移除标点符号并转换为小写
        cleaned_word = ''.join(char for char in word if char.isalpha()).lower()
        if cleaned_word:  # 确保单词非空
            word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    # 按字母顺序排序并打印
    for word in sorted(word_count):
        print(word, word_count[word])

# 测试
if __name__ == '__main__':
    sentence = "This is! a... nice day~."
    sort_word_better(sentence.split())

