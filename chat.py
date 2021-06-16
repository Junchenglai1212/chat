# 當遇到'\ufeff' 要輸入 encoding='utf-8-sig'
# 以下程式碼是要讀取出文件裡面的文字包含格式然後去掉\n
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:  # r = 讀取模式
        for line in f:
            lines.append(line.strip())
    return lines

# 以下程式碼是要印出一行一行的對話格式
def convert(lines):  #轉換
    new = []
    person = None  # python程式 None = 虛無的 (其他語言稱null)
    for line in lines:
        if line == 'Allen':   # 如果這行完全等於Allen
            person = 'Allen' # 我們就把Allen存進person這個變數
            continue #跳到下一個迴圈
        elif line == 'Tom':  # 如果這行完全等於Tom
            person = 'Tom'  # 我們就把Tom存進person這個變數
            continue
# 意味著原本文件裡面開頭的人名讀取到就跳過，所以他不會在新組合裡面成立
        if person:  #如果Person有值的話才執行下面這行
            new.append(person + ': ' + line) # 成立一個新的組合字句
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')



def main():
    lines = read_file('input.txt')
    lines = convert(lines) 
    write_file('output.txt', lines)


main()
