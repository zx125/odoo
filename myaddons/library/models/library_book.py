# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import Warning


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    _order = 'name, date_published desc'

    _sql_constraints = [
        ('library_book_name_date_uq', # 约束唯一标识符
        'UNIQUE (name, date_published)', # 约束 SQL 语法
        'Book title and publication date must be unique'), # 消息
        ('library_book_check_date',
        'CHECK (date_published <= current_date)',
        'Publication date must not be in the future.'),
    ]

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    copies = fields.Integer(default=1)
    avg_rating = fields.Float('Average Rating', (3,2))
    price = fields.Monetary('Price', 'currency_id')
    currency_id = fields.Many2one('res.currency')
    book_type = fields.Selection(
        [('paper', 'Paperback'),
        ('hard', 'Hardcover'),
        ('electronic', 'Electronic'),
        ('other', 'Other')],
        'Type')
    notes = fields.Text('Internal Notes')
    descr = fields.Html('Description')

    last_borrow_date = fields.Datetime(
        'Last Borrowed On',
        default=lambda self: fields.Datetime.now())

    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')
    publisher_country_id = fields.Many2one(
        'res.country', string='Publisher Country',
        compute='_compute_publisher_country',
        # store = False, # 默认不在数据库中存储
        inverse='_inverse_publisher_country',
        search='_search_publisher_country',
    )

    @api.depends('publisher_id.country_id')
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    @api.multi
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' % book.name)
            return True

    def _inverse_publisher_country(self):
        for book in self:
            book.publisher_id.country_id = book.publisher_country_id

    def _search_publisher_country(self, opearator, value):
        return [('publisher_id.country_id', opearator, value)]

