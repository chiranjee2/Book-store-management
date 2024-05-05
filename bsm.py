class Book:
    def __init__(self):
        self.author = ""
        self.title = ""
        self.publisher = ""
        self.price = 0.0
        self.stock = 0

    def feedData(self):
        self.author = input("Enter Author Name: ")
        self.title = input("Enter Title Name: ")
        self.publisher = input("Enter Publisher Name: ")
        self.price = float(input("Enter Price: "))
        self.stock = int(input("Enter Stock: "))

    def editData(self):
        self.author = input("Enter Author Name: ")
        self.title = input("Enter Title Name: ")
        self.publisher = input("Enter Publisher Name: ")
        self.price = float(input("Enter Price: "))
        self.stock = int(input("Enter Stock: "))

    def showData(self):
        print("\nAuthor Name:", self.author)
        print("Title Name:", self.title)
        print("Publisher Name:", self.publisher)
        print("Price:", self.price)
        print("Stock:", self.stock)

    def search(self, tbuy, abuy):
        return self.title == tbuy and self.author == abuy

    def buyBook(self):
        count = int(input("\nEnter Number Of Books to buy: "))
        if count <= self.stock:
            self.stock -= count
            print("Books Bought Successfully")
            print(f"Amount: Rs. {self.price * count:.2f}")
        else:
            print("Required Copies not in Stock")

def main():
    books = []
    while True:
        print("\n\nBook Store Management System")
        print("-----------------------------")
        print("1. Entry of New Book")
        print("2. Buy Book")
        print("3. Search For Book")
        print("4. Edit Details Of Book")
        print("5. Exit")
        choice = int(input("\nEnter your Choice: "))

        if choice == 1:
            book = Book()
            book.feedData()
            books.append(book)
        elif choice == 2:
            titleBuy = input("Enter Title Of Book: ")
            authorBuy = input("Enter Author Of Book: ")
            found = False
            for book in books:
                if book.search(titleBuy, authorBuy):
                    book.buyBook()
                    found = True
                    break
            if not found:
                print("This Book is Not in Stock")
        elif choice == 3:
            titleBuy = input("Enter Title Of Book: ")
            authorBuy = input("Enter Author Of Book: ")
            found = False
            for book in books:
                if book.search(titleBuy, authorBuy):
                    print("Book Found Successfully")
                    book.showData()
                    found = True
                    break
            if not found:
                print("This Book is Not in Stock")
        elif choice == 4:
            titleBuy = input("Enter Title Of Book: ")
            authorBuy = input("Enter Author Of Book: ")
            found = False
            for book in books:
                if book.search(titleBuy, authorBuy):
                    print("Book Found Successfully")
                    book.editData()
                    found = True
                    break
            if not found:
                print("This Book is Not in Stock")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
