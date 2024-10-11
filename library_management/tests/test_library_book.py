from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestLibraryBook(TransactionCase):
    def setUp(self):
        super(TestLibraryBook, self)setUp()
        self.library_book = self.env['library.book']

        def test_negative_price_constraint(self):
            with self.assertRaises(ValidationError):
                self.library_book.create({'title':'Invalid Book','author':'Test Author','price': -10.0})

        def test_positive_price_constraint(self):
            book = self.library_book.create({'title':'Valid Book','author':'Test Author','price': 25.0})

                self.assertEqual(book.price,25.0)

        def test_category_not_blank(self):
            """
            ValidationError ketika category kosong
            """
            with self.assertRaises(ValidationError):
                self.library_book.create({'title': 'Book without category','author': 'Test AUthor', 'price': 10.0, 'category': None})

        def test_fetch_additional_details_success(self):
            """ Fetched successfully OpenLibrary API. """
            book = self.library_book.create({'title':'1984','author':'George Orwell','price':12.50,'category':'fiction'})
                book.fetch_additional_details()
                self.assertTrue(book.isbn)
                self.assertTrue(book.publication_year)

        def test_fetch_additional_details_no_results(self):
            """ Fetched failed OpenLibrary API. """
            book = self.library_book.create({'title':'Judul Buku Tidak ada','author':'Penulis tidak diketahui','price':20.20,'category':'science'})
                book.fetch_additional_details()
                self.assertFalse(book.isbn)
                self.assertEqual(book.publication_year, 0)
                self.assertTrue(book.message_ids)

        def test_button_calculate_total_books_per_category(self):
            """ Membuat books di kategori berbeda dan tes button calculate books per category """
            self.library_book.create({'title': 'Book 1','author':'Author 1','price':10.0,'category':'fiction'})
            self.library_book.create({'title': 'Book 2','author':'Author 2','price':11.0,'category':'fiction'})
            self.library_book.create({'title': 'Book 3','author':'Author 3','price':12.0,'category':'science'})
            
                # Test button
                book = self.library_book.search([('category','=','fiction')],limit=1)
                    
            book.calculate_total_books_per_category()
            self.assertTrue(book.message_ids) #cek message dipost

            messages = book.message_ids.mapped('body')
            self.assertIn("Total books category 'Fiction': 2", messages)
            self.assertIn("Total books category 'Science':1", messages)