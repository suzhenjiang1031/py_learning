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

n = int(input())
books = {}

for _ in range(n):
    book_name = input()
    book_price = float(input())
    books[book_name] = book_price

highest_book, highest_price, lowest_book, lowest_price = find_highest_lowest_books(books)

print("{:.2f}, {}".format(highest_price, highest_book))
print("{:.2f}, {}".format(lowest_price, lowest_book))
