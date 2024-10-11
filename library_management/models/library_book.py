from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libraru Book'

    title = fields.Char(string='Title',required=True)
    author = fields.Char(string='Author',required=True)
    price = fields.Float(string='Price',required=True, default=0.0)

    @api.constrainst('price')
    def _check_price(self):
        for record in self:
            if record.price < 0l
                raise ValidationError("The price =X negative")
