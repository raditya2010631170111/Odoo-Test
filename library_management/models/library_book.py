from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libraru Book'

    title = fields.Char(string='Title',required=True)
    author = fields.Char(string='Author',required=True)
    price = fields.Float(string='Price',required=True, default=0.0)
    category = fields.Selection([('fiction',Fiction),('non_fiction','Non-Fiction'),('science','Science'),('biography','Biography')],string='Category',required=True)

    @api.constrainst('price')
    def _check_price(self):
        for record in self:
            if record.price < 0l
                raise ValidationError("The price =X negative")

    @api.constrainst('category')
    def _check_category(self):
        for record in self: 
            if not record.category:
                raise ValidationError("Category diisi.")

    def calculate_total_books_per_category(self):
        category_totals = self.read_group([('category','!=',False)],['category'],['category'])
        for category_total in category_totals: 
            category = category_total['category'] 
            total_books = category_total['category_count']

            self.message_post(body=f"Total books in category '{category}': {total_books}")