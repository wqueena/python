def read():
    words = []
    with open('filtered_words.txt', 'r', encoding='UTF-8') as f:
        line = f.readlines()
        for word in line:
            word = word.strip()
            words.append(word)
        print(words)
    return words


def replace(words):
    inputwords = input('请输入文字：')
    print(inputwords)
    for each in words:
        if each in inputwords:
            inputwords = inputwords.replace(each, len(each) * '*')
    print(inputwords)


if __name__ == '__main__':
    replace(read())