import xlwt


def read_txt():
    with open('0016.txt', 'r', encoding='UTF-8') as f:
        words = []
        content = f.read()
        word = eval(content)
        for each in word:
            words.append(each)
        print(words)
    return words


def write_xls(words):
    wb = xlwt.Workbook('UTF-8')
    ws = wb.add_sheet('sheet1')
    for i in range(len(words)):
        for j in range(len(words[i])):
            ws.write(i, j, words[i][j])
    wb.save('numbers.xls')


if __name__ == '__main__':
    write_xls(read_txt())