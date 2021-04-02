from odoo import models, fields, api

class fisrtModulModel(models.Model):
    _name = 'car.cars'

    name = fields.Char(string='Name')
    doors_number = fields.Integer(string='Door Number')
    hoors_power = fields.Integer(string='Hoors Power')

    driver_id = fields.Many2one(
        string='driver',
        comodel_name='res.partner',
        ondelete='restrict',
    )

    is_sport = fields.Boolean(string='Is Sport?')


class ResPartnerInherit(models.Model):

    _inherit = 'res.partner'

    age = fields.Char(string='Age')
