# -*- coding: utf-8 -*-
from odoo import models, fields, api


class library_book(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order      = 'date_release desc, name'
    _rec_name   = 'short_name'

    name = fields.Char('Title', required=True)
    short_name = fields.Char(string='Short Title', required=True)
    date_release = fields.Date(string='Release Date')
    author_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Authors'
        )
