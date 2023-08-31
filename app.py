
import json
class books:
    """Blueprint to make instances from this class"""
    def __init__(self,title,author):

        self.title=title
        self.author=author

class library:
    def __init__(self):
    #To store the book ojects
        self.books=[]
        
        self.load_from_json() 

#To load the json file and to append to the books=[]
    def load_from_json(self):
        try:
            with open('books.json','r', encoding='utf-8') as json_file:
                data=json.load(json_file)
                for entry in data:
                    book=books(entry['title'],entry['author'])
                    self.books.append(book)
        except FileNotFoundError:
            pass
#TO write the book data into the json file
    def save_to_json(self):
        with open('books.json','w', encoding='utf-8') as json_file:
            datas=[]
            for book in self.books:
                data={"title": book.title, "author": book.author}
                datas.append(data)
            
            json.dump(datas,json_file)
#This Adds book obj to the books list
    def add_books(self,book):
        self.books.append(book)
#Displays the list of books with authors
    def display(self):
        for book in self.books:
            print(f"Title :{book.title} ,Author :{book.author}")

def main():
    lib=library()

    while True:
        print("1.ADD BOOKS")    
        print("2.DISPLAY BOOKS")    
        print("3.EXIT")
        Choice=input("Enter Your Choice :")

        if Choice=="1":
            title=input("Enter the Title of the Book :")    
            author=input("Enter the author of the Book :")
            book=books(title,author)
            lib.add_books(book)
            lib.save_to_json() 
            

        elif Choice=="2":
            if not lib.books:
                print("its empty")
            else: 
                lib.display()    

        elif Choice=="3":
            break    

        else:
            print("Enter a valid Option")

if __name__=="__main__":
    main()
        