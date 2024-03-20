class BookDetails:
    def __init__(self):
        self.num_pages = 0
        self.year_published = 0

my_book = BookDetails()

print('Book details (before):', end=' ')
print(f'{my_book.num_pages} pages,', end=' ')
print(f'published in {my_book.year_published}')

my_book.num_pages = int(input("Enter number of pages: "))
my_book.year_published = int(input("Enter year published: "))

print('Book details (after):', end=' ')
print(f'{my_book.num_pages} pages,', end=' ')
print(f'published in {my_book.year_published}')
