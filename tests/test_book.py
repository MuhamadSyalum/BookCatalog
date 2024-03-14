import unittest
from books.book import Book

class TestBook(unittest.TestCase):

    def test_init(self):
        book = Book("rindu", "tere liye", 2014)
        self.assertEqual(book.judul, "rindu")
        self.assertEqual(book.penulis, "tere liye")
        self.assertEqual(book.tahunterbit, 2014)

    def test_search(self):
        book = Book("rindu", "tere liye", 2014)
        result = book.search("rindu")
        self.assertIsNotNone(result)
        self.assertEqual(result.judul, "rindu")
        self.assertEqual(result.penulis, "tere liye")
        self.assertEqual(result.tahunterbit, 2014)

if __name__ == '__main__':
    unittest.main()