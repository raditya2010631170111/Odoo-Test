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
        
        def test_button_calculate_total_books_per_category(self):
            """ Membuat books di kategori berbeda dan tes button calculate books per category """
            self.library_book.create({'title': 'Book 1','author':'Author 1','price':10.0,'category':'fiction'})
            self.library_book.create({'title': 'Book 2','author':'Author 2','price':11.0,'category':'fiction'})
            self.library_book.create({'title': 'Book 3','author':'Author 3','price':12.0,'category':'science'})
            
                # Test button
                book = self.library_book.search([('category','=','fiction')],limit=1)
                    
            book.calculate_total_books_per_category()
            self.assertTrue(book.message_ids) #cek message dipost