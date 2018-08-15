#coding:utf-8


def read():
    words = []
    with open('filtered_words.txt', 'r') as f:
        lines = f.readlines()
        for word in lines:
            word = word.strip()
            words.append(word)
        print(words)
    return words


def replace(words):
    flag = True
    inputwords = input('please input words:')
    print(inputwords)
    # for each in inputwords:
    #     if each in words:
    # 这里的inputwords是以字符为单位的，所以如果这么写的话
    # 如输入love会逐一判断l、o、v、e是否在words里面
    for each in words:
        #        print(each)
        if each in inputwords:
            flag = False
            #            print(flag)
            break
        else:
            #            print(flag)
            continue
    if flag:
        print('Human Rights')
    else:
        print('Freedom')


if __name__ == '__main__':
    words = read()
    replace(words)