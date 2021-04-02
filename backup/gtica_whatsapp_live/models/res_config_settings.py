# -*- coding: utf-8 -*-

import logging
import urllib
import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Website(models.Model):

    _inherit = "website"

    activate_whatsapp = fields.Boolean(string="Active Chat live Whatsapp", default=True)
    whatsapp_number = fields.Char(string="Number Whatsapp", default=lambda self: self.env.company.phone)
    cta_whatsapp = fields.Text(string="Call to action whatsapp", default="Do you have any questions about our products or services? Ask and we will answer you as soon as possible")
    message_whatsapp = fields.Text(string="Message default whatsapp", default="Hello, I would like more information about your products and services")
    url_whatsapp = fields.Char(compute="_compute_url_whatsapp", help="Remember to enter mobile number with the international code")

    @api.onchange('number_whatsapp','message_whatsapp')
    def _compute_url_whatsapp(self):
        for record in self:
            movil = record.whatsapp_number or '00-01'
            array_int = re.findall("\d+", movil)
            whatsapp_number = ''.join(str(e) for e in array_int)
            messege_prepare = u'{}'.format(record.message_whatsapp)
            messege_encode = urllib.parse.quote(messege_prepare.encode('utf8'))
            whatsapp_url = 'https://wa.me/{}?text={}'.format(whatsapp_number, messege_encode)

            record.url_whatsapp = whatsapp_url




class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    activate_whatsapp = fields.Boolean(related="website_id.activate_whatsapp", string="Active Chat live Whatsapp", readonly=False)
    whatsapp_number = fields.Char(related='website_id.whatsapp_number', readonly=False)
    cta_whatsapp = fields.Text(related="website_id.cta_whatsapp", string="Call to action whatsapp", readonly=False)
    message_whatsapp = fields.Text(related="website_id.message_whatsapp", string="Message default whatsapp", readonly=False)

    @api.constrains('activate_whatsapp', 'whatsapp_number', 'cta_whatsapp')
    def _check_fields_whatsapp(self):
        for record in self:
            if record.activate_whatsapp and  record.cta_whatsapp == '':
                raise ValidationError("Field Whatsapp Call to action must not be empty")
            if record.activate_whatsapp and  not record.whatsapp_number:
                raise ValidationError("Field Whatsapp number must not be empty")
