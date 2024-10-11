# 
def get_book_titles(book_list):
    titles = [book.get('title') for book in book_list if 'title' in book]
    return titles

book_list = [{'title': 'The Catcher in the Rye'}, 
            {'name': '1984'}, # 'title'
            {'title': 'To Kill a Mockingbird'}]
print(get_book_titles(book_list))

# case sensitive: get_author_books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})

    def get_author_books(self, author_name):
        author_name_lower = author_name.lower() 
        return [book['title'] for book in self.books if 'author' in book and book['author'].lower() == author_name_lower]

library = Library()
library.add_book('The Catcher in the Rye', 'J.D. Salinger')
library.add_book('1984', 'George Orwell')
library.add_book('To Kill a Mockingbird', 'Harper Lee')
print(library.get_author_books('george orwell'))

# TypeError discount = string, Validasi discount = float
def calculate_discounted_price(prices, discount):
    if not isinstance(discount, (int, float)):
        raise ValueError("Discount = numeric.")

    if not 0 <= discount < 1:
        raise ValueError("Discount = antara 0 (inklusif) dan 1 (eksklusif).")

    total = sum(price * (1 - discount) for price in prices)
    return total

prices = [100, 200, 300]
discount = "0.1" #float
print(calculate_discounted_price(prices, discount))

# class LibraryBook terulang
from odoo import models, fields, api

# class LibraryBook(models.Model):
#     _name = 'library.book'
#     _description = 'Library Book'

#     title = fields.Char(string='Title')
#     author_id = fields.Many2one('library.author', string='Author')
#     price = fields.Float(string='Price')

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Author Name', required=True)
    total_books = fields.Integer(string='Total Books', compute='_compute_total_books', store=True)

    @api.depends('book_ids')
    def _compute_total_books(self):
        for author in self:
            author.total_books = len(author.book_ids)
            # author.total_books = len(self.env['library.book'].search([('author_id', '=', self.id)]))

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('library.author', string='Author', required=True, ondelete='cascade')
    price = fields.Float(string='Price', default=0.0)
    is_discounted = fields.Boolean(string='Is Discounted', compute='_compute_is_discounted', store=True)
    discount_threshold = fields.Float(string='Discount Threshold', default=50.0)

    @api.depends('price')
    def _compute_is_discounted(self):
        for book in self:
            book.is_discounted = book.price < book.discount_threshold

            # if book.price > 50:
            #     book.is_discounted = False
            # else:
            #     book.is_discounted = True


    @api.model
    def create(self, vals):
        return super(LibraryBook, self).create(vals)

    @api.multi
    def write(self, vals):
        return super(LibraryBook, self).write(vals)