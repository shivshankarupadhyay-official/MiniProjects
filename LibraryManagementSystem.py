class Library:

    
    def __init__(self):
        self.books = []         
        self.no_of_books = 0     

    
    def add_book(self, book_name):
        self.books.append(book_name)   
        self.no_of_books += 1           
        print(f'"{book_name}" ADDED TO LIBRARY')


    def print_books(self):
        if self.no_of_books == 0:
            print("LIBRARY IS EMPTY")
        else:
            print("\nBOOKS IN LIBRARY:")
            for book in self.books:
                print("-", book)

    
    def get_number_of_books(self):
        return self.no_of_books



lib = Library()


n = int(input("How many books do you want to add? "))


for i in range(n):
    book_name = input(f"Enter name of book {i+1}: ")
    lib.add_book(book_name)


lib.print_books()


print("\nTOTAL NUMBER OF BOOKS:", lib.get_number_of_books())