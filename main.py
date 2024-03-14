import json
from books.book import Book

def load_books(file_name):
    with open(file_name, "r") as file:
        books = json.load(file)
    return [Book(book["judul"], book["penulis"], book["tahunterbit"]) for book in books]

def add_book(books, judul, penulis, tahunterbit):
    books.append(Book(judul, penulis, tahunterbit))
    save_books(books)

def save_books(books, file_name="data/books.json"):
    with open(file_name, "w") as file:
        json.dump([{"judul": book.judul, "penulis": book.penulis, "tahunterbit": book.tahunterbit} for book in books], file)

def search_book(books, judul):
    for book in books:
        result = book.search(judul)
        if result:
            return result
    return None

def display_books(books):
    for book in books:
        print("=============================================================")
        print("Judul Buku : " +book.judul)
        print("Nama Penulis: " +book.penulis)
        print("Tahun Terbit Buku: " +str(book.tahunterbit))
        print("=============================================================")

if __name__ == "__main__":
    books = load_books("data/books.json")
    while True:
        Print("Perpustakaan Mulays")
        print("\n1. Tambah Judul Buku")
        print("2. Cari Buku")
        print("3. Lihat Data Buku")
        print("4. Exit")
        option = int(input("Masukkan Pilihan Kamu: "))
        if option == 1:
            judul = input("Masukkan Judul Buku: ")
            penulis = input("Masukkan Penulis Buku: ")
            tahunterbit = int(input("Masukkan Tahun Terbit Buku: "))
            add_book(books, judul, penulis, tahunterbit)
            print("Buku Berhasil Ditambahkan")
        elif option == 2:
            judul = input("Masukkan Judul Buku Yang Ingin Dicari: ")
            result = search_book(books, judul)
            if result:
                print(f"Buku Tersedia: {result}")
            else:
                print("Buku Belum Tersedia")
        elif option == 3:
            display_books(books)
        elif option == 4:
            break
        else:
            print("Mohon maaf pilihan ada tidak ada, NT")