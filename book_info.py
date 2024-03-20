class BookInfo:
    def __init__(self):
        self.num_pages = 0
        self.year_published = 0
        self.genre = 'unknown'

book = BookInfo()
book.num_pages = int(input("Enter number of pages: "))
book.year_published = int(input("Enter year: "))
book.genre = input("Enter genre: ")

print('Book info:', end=' ')
print(f'{book.num_pages} pages,', end=' ')
print(f'published in {book.year_published},', end=' ')
print(f'{book.genre}')
