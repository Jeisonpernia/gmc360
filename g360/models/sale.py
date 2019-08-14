from odoo import api, fields, models

import urllib.parse
import requests
import datetime

class SaleOrder(models.Model):
    _inherit = "sale.order"

    fecha_probable = fields.Date(string="Fecha Probable de cierre")
    plazo = fields.Char(string="Plazo")

    @api.multi
    def unlink(self):
        for order in self:
            if order.state not in ('draft','cancel','sale',):
                raise UserError(_('You can not delete a sent quotation or a confirmed sales order. You must first cancel it.'))
        return super(SaleOrder, self).unlink()
