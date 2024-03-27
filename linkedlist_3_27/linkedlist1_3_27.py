# 给定n本书的名称和定价，本题要求编写程序，查找并输出其中定价最高和最低的书的名称和定价。
#
# 输入格式:
# 输入第一行给出正整数n（<10），随后给出n本书的信息。每本书在一行中给出书名，即长度不超过30的字符串，随后一行中给出正实数价格。题目保证没有同样价格的书。
#
# 输出格式:
# 在一行中按照“价格, 书名”的格式先后输出价格最高和最低的书。价格保留2位小数。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 3
# Programming in C
# 21.5
# Programming in VB
# 18.5
# Programming in Delphi
# 25.0
#
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 25.00, Programming in Delphi
# 18.50, Programming in VB

def find_highest_lowest_books(books):
    highest_price = float('-inf')
    lowest_price = float('inf')
    highest_book = ""
    lowest_book = ""

    for book, price in books.items():
        if price > highest_price:
            highest_price = price
            highest_book = book
        if price < lowest_price:
            lowest_price = price
            lowest_book = book

    return highest_book, highest_price, lowest_book, lowest_price


# 输入书的数量
n = int(input())

# 初始化书的信息
books = {}

# 输入每本书的信息并保存在字典中
for _ in range(n):
    book_name = input()
    book_price = float(input())
    books[book_name] = book_price

# 查找最高价和最低价的书籍
highest_book, highest_price, lowest_book, lowest_price = find_highest_lowest_books(books)

# 输出结果
print("{:.2f}, {}".format(highest_price, highest_book))
print("{:.2f}, {}".format(lowest_price, lowest_book))
