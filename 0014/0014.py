import xlwt

wb = xlwt.Workbook(encoding='UTF-8')
ws = wb.add_sheet('sheet1')


def read_txt():
    with open('0014.txt', 'r', encoding='UTF-8') as f:
        row = 0
        lines = f.readlines()
        for line in lines:
            col = 0
            line = line.replace(':', ' ')
            line = line.replace(',', ' ')
            line = line.replace('[', ' ')
            line = line.replace(']', ' ')
            line = line.replace('"', ' ')
            line = line.replace('    ', ' ')
            line = line.replace('  ', ' ')
            line = line.strip()
            line = line.split(' ')
            #            print(len(line))
            #            print(line)

            for i in range(len(line)):
                #                print(line[i])
                ws.write(row, col, line[i])
                col += 1
                wb.save('result.xls')
            row += 1


if __name__ == '__main__':
    read_txt()