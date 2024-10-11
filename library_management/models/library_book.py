import requests
import requests_cache
from odoo import models, fields, api
from odoo.exceptions import ValidationError 

requests_cache.install_cache('openlibrary_cache',expire_after=86400)

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libraru Book'

    title = fields.Char(string='Title',required=True)
    author = fields.Char(string='Author',required=True)
    price = fields.Float(string='Price',required=True, default=0.0)
    category = fields.Selection([('fiction',Fiction),('non_fiction','Non-Fiction'),('science','Science'),('biography','Biography')],string='Category',required=True)
    isbn = fields.Char(string='ISBN')
    publication_year = fields.Integer(string='Publication Year')

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

    def fetch_additional_details(self):
        for record in self:
            if not record.title:
                continue
            try:
                response = requests.get('http://openlibrary.org/search.json',params={'title':record.title},timeout=10)
                response.raise_for_status()
                data = response.json()
                if data['numFound'] > 0;
                    first_result = data['docs'][0]
                    record.isbn = first_result.get('isbn',['']) [0] if first_result.get('isbn') else ''
                    record.publication_year = first_result.get('first_publish_year',0)
                else:
                    record.message.post(body="Tidak ada info lain untuk buku ini")
            except
                request.exceptions.RequestExceptions as 0:
                record.message_post(body=f"Failed:{str(e)}")

    def calculate_total_books_per_category(self):
        category_totals = self.read_group([('category','!=',False)],['category'],['category'])
        messages= []
        for category_total in category_totals: 
            category = dict(self._fields['category']:selection).get(category_total['category'],'Unknown')
            total_books = category_total['category_count']

        messages.append(f"Total books category '{category}':{total_books}")
            if messages:
                self.message_post(body="\n".join(messages))
            else:
                self.message_post(body="Category tidak ditemukan.")